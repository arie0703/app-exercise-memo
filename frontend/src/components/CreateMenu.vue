<template>
    <v-container>
        <v-col>
            <v-dialog
            v-model="dialog"
            max-width="700px"
            scrollable
            >
                <template v-slot:activator="{ on, attrs }">
                    <v-btn
                    color="indigo"
                    dark
                    v-bind="attrs"
                    v-on="on"
                    >
                    セットメニューを作成
                    </v-btn>
                </template>
                <v-card>
                    <v-card-title>
                        メニューを作成
                    </v-card-title>
                    <v-divider></v-divider>
                    <v-card-actions>
                        <v-col cols="6" xs="12">
                            <v-text-field
                                label="タイトル"
                                v-model="template_title"
                                outlined
                                hide-details="auto"
                            ></v-text-field>
                        </v-col>
                        <v-btn
                        class="mx-2"
                        dark
                        small
                        color="indigo"
                        @click="addMenu()"
                        >
                            種目を追加
                        </v-btn>
                    </v-card-actions>
                    <v-card-text style="height: 500px;">
                        <v-col>
                            <v-row v-for="(_, i) in menu_index" v-bind:key="i" style="align-items: center">
                                <v-col cols="4" xs="12" align-self="center">
                                <v-select
                                    v-model="workout_info[i]"
                                    :items="workouts"
                                    item-text="name"
                                    label="種目"
                                    outlined
                                    return-object
                                    hide-details="auto"
                                ></v-select>
                                </v-col>
                                <v-col cols="2" xs="12">
                                    <v-text-field
                                        type="number"
                                        v-model="reps[i]"
                                        label="回数"
                                        outlined
                                        hide-details="auto"
                                    >
                                    </v-text-field>
                                </v-col>
                                <v-col cols="2" xs="12">
                                    <v-text-field
                                        type="number"
                                        v-model="weight[i]"
                                        label="重量"
                                        outlined
                                        hide-details="auto"
                                    >
                                    </v-text-field>
                                </v-col>
                                <v-col cols="2" xs="12">
                                    <v-text-field
                                        type="number"
                                        v-model="set_count[i]"
                                        label="セット"
                                        outlined
                                        hide-details="auto"
                                    >
                                    </v-text-field>
                                </v-col>
                                <v-col cols="2" xs="12">
                                    <v-btn
                                    class="mx-2"
                                    fab
                                    dark
                                    small
                                    @click="deleteMenu(i)"
                                    >
                                    <v-icon dark>
                                        mdi-minus
                                    </v-icon>
                                    </v-btn>
                                </v-col>
                            </v-row>
                        </v-col>
                    </v-card-text>
                    <v-divider></v-divider>
                    <v-card-actions>
                        {{msg}}
                        <v-col cols="3" xs="12">
                            <v-btn
                                @click="createTemplate()"
                            >
                                Create
                            </v-btn>
                        </v-col>
                    </v-card-actions>
                </v-card>
            </v-dialog>
        </v-col>
    </v-container>
</template>

<style scoped>


</style>

<script>
    import axios from 'axios'
    export default {
        name: 'CreateMenu',

        data: () => ({
            workouts: {},
            workout_info: [],
            reps: [],
            set_count: [],
            weight: [],
            template_id: null,
            template_title: "",
            menu_index: [0],
            msg : "",
        }),
        mounted () {
            axios.get('http://localhost:5000/api/workouts')
            .then(res =>
                this.workouts = res.data.workouts
            );
        },
        methods: {
            addMenu () {
                this.menu_index.push(this.menu_index.length)
            },
            deleteMenu (index) {
                this.menu_index.splice(index,1)
                this.workout_info.splice(index, 1)
                this.reps.splice(index, 1)
                this.set_count.splice(index, 1)
                this.weight.splice(index, 1)
            },
            createTemplate () {
                if (this.workout_info.length < this.menu_index.length || this.workout_info.includes(null)) {
                    this.msg = "入力が正しくないよ！"
                    return
                }

                axios.post('http://localhost:5000/api/templates/create', {
                    title: this.template_title
                }).then(res => {
                    this.template_id = res.data.template.id
                    for (const i in this.menu_index) {
                        axios.post('http://localhost:5000/api/menus/create', {
                            workout_id: this.workout_info[i].id,
                            reps: this.reps[i] ??= 0,
                            set_count: this.set_count[i] ??= 0,
                            weight: this.weight[i] ??= 0,
                            template_id: this.template_id,
                        }).then(res => {
                            console.log(res.data.menu)
                            this.msg = "送信完了したよ！"
                        })
                    }
                })
            }
        }
    }
</script>
