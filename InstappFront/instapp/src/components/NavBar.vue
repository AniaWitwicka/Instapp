<template>
  <v-app-bar elevation="4">
    <v-app-bar-nav-icon></v-app-bar-nav-icon>
    <v-toolbar-title>Instapp</v-toolbar-title>
    <v-spacer></v-spacer>
    <v-menu bottom left>
      <template v-slot:activator="{ on, attrs }">
        <v-btn icon v-bind="attrs" v-on="on">
          <v-icon>mdi-dots-vertical</v-icon>
        </v-btn>
      </template>

      <v-list>
        <v-list-item @click="$emit('add_access_token')">
          <v-list-item-content>
            <v-list-item-title>add access token</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
        <v-list-item @click="$emit('add_ig_user_id')">
          <v-list-item-content>
            <v-list-item-title>add instagram user id</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-menu>
  </v-app-bar>
</template>

<script>
export default {
  name: "NavBar",
  data() {
    return {};
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped></style>
