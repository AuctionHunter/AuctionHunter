'use strict'
import Vue from 'vue'
import 'bootstrap';
import 'bootstrap/dist/css/bootstrap.min.css';
import App from './components/App.vue'

Vue.prototype.$eventHub = new Vue();
Vue.config.productionTip = false

new Vue({
  el: 'app',
  components: {App},
  methods: {}
})
