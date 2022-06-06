<template>
    <v-container>
        <v-col cols="4">
            <v-select
                v-model="selected"
                :items="templates"
                v-if="Object.keys(templates).length"
                item-text="title"
                item-value="id"
                label="Select Workout"
                color="indigo"
                return-object
                outlined
            ></v-select>
            <v-progress-circular
                indeterminate
                color="indigo"
                v-if="!Object.keys(templates).length"
            ></v-progress-circular>
        </v-col>
        <v-progress-circular
            indeterminate
            color="indigo"
            v-if="isLoading"
        ></v-progress-circular>
        <OutputText v-if="formatted_text" v-bind:formatted_text = formatted_text></OutputText>
        <v-col v-if="!formatted_text">
            Select Workout Menu!
        </v-col>
    </v-container>
</template>

<script>
import axios from 'axios'
import OutputText from './OutputText.vue';
export default {
    name: 'ShowMenus',
    components: { OutputText },
    data: () => ({
        templates: {},
        menus: {},
        formatted_text: "",
        headers: {"x-hasura-admin-secret": process.env.VUE_APP_HASURA_SECRET},
        selected: {},
        isLoading: false,
    }),
    mounted () {
        axios.get(process.env.VUE_APP_HASURA_ENDPOINT + 'templates',{headers: this.headers})
        .then(res =>
        {
            this.templates = res.data.templates
            console.log(this.templates)
        }
        );
    },
    watch: {
        'selected': function() {
            this.showMenus(this.selected.id)
        }
    },
    methods: {
        showMenus(template_id) {
                this.isLoading = true;
                axios.get(
                    process.env.VUE_APP_HASURA_ENDPOINT + 'menus/template_id/' + template_id,
                    {headers: this.headers}
                    )
                .then(res => {
                    this.menus = res.data.menus
                    this.formatText()
                    this.isLoading = false;
                }
            );
        },

        formatText() {
            this.formatted_text = "";
            for (let menu of this.menus) {
                let weight = (menu.weight > 0) ? `${menu.weight} kg * ` : ""
                let reps = (menu.reps > 0) ? `${menu.reps} * ` : ""
                let set_count = (menu.set_count > 0) ? `${menu.set_count}sets ` : ""

                this.formatted_text += `- ${menu.workout} \n`

                if(weight + reps + set_count !== "") {
                    this.formatted_text += `\t- ${weight}${reps}${set_count}\n`
                }
            }
        }
    }
}
</script>