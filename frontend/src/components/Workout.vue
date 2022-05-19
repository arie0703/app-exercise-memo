<template>
    <v-container>
        <v-row class="text-center">
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


            <v-row v-for="(workout) in workouts" v-bind:key="workout.id" justify="center">
            {{workout.name}}
            </v-row>
            </v-col>

            <v-col
            class="mb-5"
            cols="12"
            >
            <h2 class="headline font-weight-bold mb-3">
                Important Links
            </h2>

            <v-row justify="center">
            </v-row>
            </v-col>
        </v-row>
    </v-container>
</template>

<script>
    import axios from 'axios'
    export default {
        name: 'Workout',

        data: () => ({
            workouts: []
        }),
        mounted () {
            axios.get('http://localhost:5000/api/workouts')
            .then(res =>
                this.workouts = res.data.workouts
            );
        }
    }
</script>
