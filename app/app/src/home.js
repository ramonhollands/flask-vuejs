import Vue from 'vue';
import Home from "./pages/Home";

window.onload = function () {
    var app = new Vue({
        el: '#app',
        components: {Home}
    });
}