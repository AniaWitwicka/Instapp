<template>
  <div>
    <nav-bar></nav-bar>
    <post-form @submit="submit" />
  </div>
</template>

<script>
import NavBar from "../components/NavBar.vue";
import PostForm from "../components/PostForm.vue";

export default {
  name: "Home",
  methods: {
    submit: function () {
      console.log("not implemented yet");
    },
  },
  components: {
    PostForm,
    NavBar,
  },
};
</script>
