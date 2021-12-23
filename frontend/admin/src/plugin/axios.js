import Vue from 'vue'
import axios from 'axios'

const guest = axios.create({
  // axios.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';
  baseURL: 'http://server.mtilagos.org.ng/app',
  // baseURL: 'http://localhost:8080/mti/backend',
  headers: {
    // "Content-Type": "application/json",
    "X-Requested-With": "XMLHttpRequest",
  } 
});
Vue.prototype.$guest = guest

export { guest }