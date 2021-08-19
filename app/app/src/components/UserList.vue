<template>
  <div>
    <div class="row">
      <div v-if="users && roles" class="col-md-12">
        <div class="row" style="height: 40px;">
          <div class="col-md-5">
          </div>
          <div class="col-md-5">
            <div style="width: 80px; float:left; margin-left: 10px;" v-for="role in roles">{{ role }}</div>
          </div>
          <div class="col-md-2">
          </div>
        </div>
        <user @delete_user="delete_user($event)" v-for="user in users" :key="user.email" :roles="roles"
            :user="user"></user>
      </div>

    </div>
    <add-user @update_users="update_users"></add-user>
  </div>
</template>

<script>
import User from "./User";
import AddUser from "./AddUser";

export default {
  name: "UserList.vue",
  data() {
    return {
      'users': [],
      'roles': [],
    }
  },
  components: {User, AddUser},
  mounted() {
    let this2 = this;
    $.get('/get-users', function (data) {
      this2.$set(this2, 'users', data);
    });
    $.get('/get-roles', function (data) {
      this2.$set(this2, 'roles', data);
    });
  },
  methods: {
    update_users(users) {
      this.$set(this, 'users', users);
    },
    delete_user(user_deleted) {
      let updated_users = this.users.filter((user) => {
        return user.email !== user_deleted.email;
      });
      this.$set(this, 'users', updated_users);
      $.post('/delete-user', {user: user_deleted.email}, function (data) {
      });
    }

  }
}
</script>

<style scoped>

</style>