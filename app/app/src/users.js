import Vue from 'vue';
import UserList from "./components/UserList";

window.onload = function () {
    var app = new Vue({
        el: '#app',
        components: {UserList}
    });
}