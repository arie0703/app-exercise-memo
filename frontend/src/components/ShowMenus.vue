<template>
    <v-container>
        <v-row>
            <v-col col="2" v-for="template in templates" v-bind:key="template.id">
                <v-card class="pa-2" @click="showMenus(template.id)">
                    {{template.title}}
                </v-card>
            </v-col>
        </v-row>
        <OutputText v-if="formatted_text" v-bind:formatted_text = formatted_text></OutputText>
        <v-col v-if="!formatted_text">
            Click Workout Menu!
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
    methods: {
        showMenus(template_id) {
                axios.get(
                    process.env.VUE_APP_HASURA_ENDPOINT + 'menus/template_id/' + template_id,
                    {headers: this.headers}
                    )
                .then(res => {
                    this.menus = res.data.menus
                    this.formatText()
                }
            );
        },

        formatText() {
            this.formatted_text = "";
            for (let menu of this.menus) {
                let weight = (menu.weight > 0) ? `${menu.weight} kg *` : ""
                let reps = (menu.reps > 0) ? `${menu.reps} *` : ""
                let set_count = (menu.set_count > 0) ? `${menu.set_count}sets` : ""

                this.formatted_text += `- ${menu.workout} \n`

                if(weight + reps + set_count !== "") {
                    this.formatted_text += `\t- ${weight} ${reps} ${set_count}\n`
                }
            }
        }
    }
}
</script>