<template>
  <div v-if="local_user !== {}" class="row" style="height: 40px;">
      <div class="col-md-5">
        {{local_user.email}}
      </div>
      <div class="col-md-5">
        <div style="width: 80px; float:left; margin-left: 10px;"
             v-for="role in roles">
              <checkbox :editable="editable" :value="local_user.roles.includes(role)" @input="updateRole(role, $event)"></checkbox>
        </div>
      </div>
      <div class="col-md-2">
        <div v-if="editable" class="button" @click="delete_user">X</div>
      </div>
  </div>
</template>

<script>
import Checkbox from "./Checkbox";
export default {
  name: "UserList.vue",
  components: {Checkbox},
  data() {
    return {
      local_user: {},
      current_user_email: '',
    }
  },
  props: {
    user: {required: true},
    roles: {required: true}
  },
  mounted() {
    this.local_user = this.user;
    this.current_user_email = $('#current_user_email').val()
  },
  watch: {
    user(val) {
      this.local_user = this.user;
    }
  },
  computed: {
    editable () {
      return this.local_user.email !== this.current_user_email;
    }
  },
  methods: {
    updateRole(role, value) {
      let user_roles = this.local_user.roles;
      let this2 = this;
      if(value) {
        user_roles.push(role);
        $.post('/add-role', {user:this.local_user.email, role: role}, function (data) {});
      }
      else {
        user_roles = user_roles.filter(function(value){
          return value !== role;
        });
        $.post('/remove-role', {user:this.local_user.email, role: role}, function (data) {});
      }
      this.$set(this.local_user, 'roles', user_roles);
    },
    delete_user () {
      this.$emit('delete_user', this.local_user)
    }
  }
}
</script>

<style scoped>

</style>