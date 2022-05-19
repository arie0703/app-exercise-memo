<template>
  <v-app>
    <v-app-bar
      app
      color="primary"
      dark
    >
      <div class="d-flex align-center">
        <h1 class="display-2 font-weight-medium">
          Workout MEMO
        </h1>
      </div>

      <v-spacer></v-spacer>

      <v-btn
        href="https://github.com/vuetifyjs/vuetify/releases/latest"
        target="_blank"
        text
      >
        <span class="mr-2">Latest Release</span>
        <v-icon>mdi-open-in-new</v-icon>
      </v-btn>
    </v-app-bar>

    <v-main>
      <Workout/>
    </v-main>
  </v-app>
</template>

<script>
import Workout from './components/Workout';

export default {
  name: 'App',

  components: {
    Workout,
  },

  data: () => ({
    //
  }),
};
</script>
