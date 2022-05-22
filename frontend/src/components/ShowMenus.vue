<template>
    <v-container>
        <v-row>
            <v-col col="2" v-for="template in templates" v-bind:key="template.id">
                <v-card class="pa-2" @click="showMenus(template.id)">
                    {{template.title}}
                </v-card>
            </v-col>
        </v-row>

        <v-col v-for="menu in menus" v-bind:key="menu.name" cols="4">
            <v-card>
                <v-card-title>
                    {{menu.name}}
                </v-card-title>
                <v-card-text>
                    <span v-if="menu.weight > 0">
                        {{menu.weight}}kg *
                    </span>
                    <span v-if="menu.reps > 0">
                        {{menu.reps}} *
                    </span>

                    <span v-if="menu.set_count > 0">
                        {{menu.set_count}}sets
                    </span>
                </v-card-text>
            </v-card>
        </v-col>
    </v-container>
</template>

<script>
import axios from 'axios'
export default {
    name: 'ShowMenus',

        data: () => ({
            templates: {},
            menus: {},
        }),
        mounted () {
            axios.get('http://localhost:5000/api/templates')
            .then(res =>
                this.templates = res.data.templates
            );
        },
        methods: {
            showMenus(template_id) {
                axios.get('http://localhost:5000/api/menus/template_id=' + template_id)
                .then(res => {
                    this.menus = res.data.menus
                }
                );
            }
        }
}
</script>