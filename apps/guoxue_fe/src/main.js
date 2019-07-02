// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import store from './store'
import ElementUI from 'element-ui'
// import axios from 'axios'

import 'element-ui/lib/theme-chalk/index.css'

import $ from 'jquery'
// 以下这种方式导入使用npm安装好的包失败，我感觉这样子导入应该是没有找到bootstrap的所在路径
// import 'bootstrap'
import './static/css/bootstrap.min.css'
// 此时如果要使用bootstrap中的字体，那么可以直接导入所在的位置的文件，如上所导入的方式
import './static/css/animate.css'
import './static/css/reset.css'

import '../static/UE/ueditor.config.js'
import '../static/UE/ueditor.all.min.js'
import '../static/UE/lang/zh-cn/zh-cn.js'
import '../static/UE/ueditor.parse.min.js'

// 把axios挂载到vue构造函数的prototype属性上，组件中通过this.axios来拿到axios
// Vue.prototype.axios = axios
Vue.config.productionTip = false

Vue.use(ElementUI)


/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>',
  store
})
