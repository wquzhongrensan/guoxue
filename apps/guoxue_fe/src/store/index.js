import Vue from 'vue'
import Vuex from 'vuex'

import moudle1 from './moudle/moudle1'
import login_status from './moudle/login_status'

Vue.use(Vuex)

export default new Vuex.Store({
  modules: {
    moudle1: moudle1,
		login_status:login_status,
  }
})
