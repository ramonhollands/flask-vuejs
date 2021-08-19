<template>
  <div>
    <div class="row" style="margin-top: 20px;">
      <div class="col-md-12">
        <h4>Add new user:</h4>
      </div>
    </div>
    <div class="row">
      <div class="col-md-3">
        Email
      </div>
      <div class="col-md-6">
        <input v-model="email" type="text"><br />
      </div>
    </div>
    <div class="row">
      <div class="col-md-3">
        Username
      </div>
      <div class="col-md-6">
        <input v-model="username" type="text"><br />
      </div>
    </div>
    <div class="row">
      <div class="col-md-3">
        First name
      </div>
      <div class="col-md-6">
        <input v-model="first_name" type="text"><br />
      </div>
    </div>
    <div class="row">
      <div class="col-md-3">
        Last name
      </div>
      <div class="col-md-6">
        <input v-model="last_name" type="text"><br />
      </div>
    </div>
     <div class="row">
      <div class="col-md-12">
        <div style="float: left; margin-left: 0px; margin-top: 10px;" class="button" @click="add_user">Add</div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "AddUser.vue",
  data () {
    return {
      'email': '',
      'username': '',
      'first_name': '',
      'last_name': ''
    }
  },
  methods: {
    add_user() {
      let this2 = this;
      $.post('/add-user',
          {
            email: this.email,
            username: this.username,
            first_name: this.first_name,
            last_name: this.last_name
          }, function (data) {
            this2.$emit('update_users', data);
          });
    }
  }
}
</script>

<style scoped>

</style>