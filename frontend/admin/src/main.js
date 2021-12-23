import Vue from 'vue'
import Vuex from 'vuex'
import App from './App'
import router from './router/router'
import axios from 'axios'
import VueAxios from 'vue-axios'
import VueSimpleAlert from "vue-simple-alert";
import {guest} from './plugin/axios'
import IdleVue from 'idle-vue'

const eventsHub = new Vue()
Vue.use(IdleVue, {
  eventEmitter: eventsHub,
  idleTime: 3000,
  startAtIdle: false
})
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
Vue.component('font-awesome-icon', FontAwesomeIcon)

import VueSession from 'vue-session'
var vueOptions = {
  persist: true
}
Vue.use(VueSession, vueOptions)

Vue.use(VueSimpleAlert, { reverseButtons: true });
import VueProgressBar from 'vue-progressbar'
import VueHtml2pdf from 'vue-html2pdf'
Vue.component('VueHtml2pdf', VueHtml2pdf);


Vue.use(VueProgressBar, {
  color: 'blue',
  failedColor: 'red',
  height: '2px'
})

import MenuHeader from './layout/MenuHeader'
Vue.component('MenuHeader', MenuHeader)

import GeneralHeader from './layout/GeneralHeader'
Vue.component('GeneralHeader', GeneralHeader)

import AdminHeader from './layout/BackendHeader'
Vue.component('AdminHeader',AdminHeader)

import ApplicationHeader from './layout/ApplicationHeader'
Vue.component('ApplicationHeader',ApplicationHeader)

import PanelHeader from './layout/GeneralHeader'
Vue.component('PanelHeader',PanelHeader)

import PrintableHeader from './layout/PrintableHeader'
Vue.component('PrintableHeader',PrintableHeader)

import ProfileLayout from './layout/profileLayout'
Vue.component('ProfileLayout',ProfileLayout)

Vue.use(VueAxios, axios, Vuex)

Vue.config.productionTip = false

new Vue({
  router,
  guest,
  render: h => h(App),
}).$mount('#app')