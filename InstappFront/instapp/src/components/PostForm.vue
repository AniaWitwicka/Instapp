<template>
  <div>
    <v-form v-model="form">
      <v-container>
        <v-text-field
          v-model="title"
          :counter="255"
          label="Title"
          required
        ></v-text-field>
        <v-text-field
          v-model="caption"
          :counter="2200"
          label="Caption"
          required
        ></v-text-field>
        <v-date-picker
          v-model="date"
          label="Date"
          required
          flat
        ></v-date-picker>
        <v-checkbox v-model="is_carousel_item" label="Is Carousel"></v-checkbox>
        <v-select :items="items" label="Standard"></v-select>
        <v-text-field
          v-model="access_token"
          :counter="2200"
          label="access_token"
          required
        ></v-text-field>
        <v-text-field
          v-model="ig_user_id"
          :counter="2200"
          label="ig_user_id"
          required
        ></v-text-field>
        <v-file-input truncate-length="15"></v-file-input>
        <v-btn class="mr-4" @click="$emit('submit')"> submit </v-btn>
        <v-btn @click="clear"> clear </v-btn>
      </v-container>
    </v-form>
  </div>
</template>

<script>
export default {
  name: "PostForm",
  methods:{
      clear: function (){
          this.from =this.form_clear;
      },
  },
  data() {
    return {
      items: ["VIDEO", "CAROUSEL", "IMAGE"],
      form: {
        title: "",
        // owner: "",
        caption: "",
        date: "",
        is_carousel_item: "",
        // location_id: "",
        media_type: "",
        // status: "",
        // thumb_offset: "",
        access_token: "",
        ig_user_id: "",
      },
      form_clear: {
        title: "",
        // owner: "",
        caption: "",
        date: "",
        is_carousel_item: "",
        // location_id: "",
        media_type: "",
        // status: "",
        // thumb_offset: "",
        access_token: "",
        ig_user_id: "",
      },
    };
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped></style>
