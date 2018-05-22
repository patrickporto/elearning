import Vue from 'vue/dist/vue';
import Vuetify from 'vuetify'
import Messenger from './components/Messenger.vue'
import moment from 'moment';
import VueMoment from 'vue-moment'


Vue.use(Vuetify)
Vue.use(VueMoment)

const app = new Vue({
  components: {
    'ava-messenger': Messenger,
  }
}).$mount('#app')
