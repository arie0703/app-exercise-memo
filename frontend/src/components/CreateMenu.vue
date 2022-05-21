<template>
    <v-container>
        <v-row>
            <v-col cols="12">
            </v-col>

            <v-col class="mb-4">
            <h1 class="display-2 font-weight-bold mb-3">
                Workout MEMO
            </h1>

            <p class="subheading font-weight-regular">
                ワークアウトメモです
            </p>
            </v-col>

            <v-col
            class="mb-5"
            cols="12"
            >
            <h2 class="headline font-weight-bold mb-3">
                種目
            </h2>


            <v-row v-for="(workout) in workouts" v-bind:key="workout.id">
            {{workout.name}}
            </v-row>
            </v-col>

            <v-col
            class="mb-5"
            cols="12"
            >
            <h2 class="headline font-weight-bold mb-3">
                セットメニューを作成
            </h2>
            {{reps}}
            {{menu_index}}
            <v-btn
            class="mx-2"
            fab
            dark
            color="indigo"
            @click="addMenu()"
            >
            <v-icon dark>
                mdi-plus
            </v-icon>
            </v-btn>
            <v-col>
                <v-col cols="4" xs="12">
                <v-text-field
                    label="テンプレート名"
                    v-model="template_title"
                    outlined
                ></v-text-field>
                </v-col>
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
                    <v-col cols="1" xs="12">
                        <v-text-field
                            type="number"
                            v-model="reps[i]"
                            label="回数"
                            outlined
                            hide-details="auto"
                        >
                        </v-text-field>
                    </v-col>
                    <v-col cols="1" xs="12">
                        <v-text-field
                            type="number"
                            v-model="weight[i]"
                            label="重量"
                            outlined
                            hide-details="auto"
                        >
                        </v-text-field>
                    </v-col>
                    <v-col cols="1" xs="12">
                        <v-text-field
                            type="number"
                            v-model="set_count[i]"
                            label="セット"
                            outlined
                            hide-details="auto"
                        >
                        </v-text-field>
                    </v-col>
                    <v-col cols="1" xs="12">
                        <v-btn
                        class="mx-2"
                        fab
                        dark
                        small
                        color="primary"
                        @click="deleteMenu(i)"
                        >
                        <v-icon dark>
                            mdi-minus
                        </v-icon>
                        </v-btn>
                    </v-col>
                </v-row>
                {{msg}}
                <v-col cols="3" xs="12">
                    <v-btn
                        @click="createTemplate()"
                    >
                        Create
                    </v-btn>
                </v-col>
            </v-col>
            </v-col>
        </v-row>
    </v-container>
</template>

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

            axios.get('http://localhost:5000/api/templates')
            .then(res => {
                this.template_id = res.data.templates.length + 1
                console.log(res)
            }
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
