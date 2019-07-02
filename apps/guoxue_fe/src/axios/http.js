import axios from 'axios' //引用axios
import store from '@/store/index.js'
import {getCookie} from '@/utils/cookies'
import { mapState } from 'vuex'

// axios 配置
axios.defaults.timeout = 5000; 
axios.defaults.baseURL = 'http://localhost/pjm-shield-api/public/v1/'; //这是调用数据接口
 
// http request 拦截器，通过这个，我们就可以把Cookie传到后台   ******* important
axios.interceptors.request.use(
	config => {
		if (getCookie('token')) {
		  config.headers.Authorization = 'JWT ' + getCookie('token');
		}
		return config;
	},
	error => {
		return Promise.reject(error);
	}
);
// 401拦截器
axios.interceptors.response.use(
	response => {
		return response
	},
	error => {
		if (error.response) {
			switch (error.response.status) {
				case 401:
					confirm('过期');
					if(getCookie("username")){
						delCookie("username");
					}
					if(getCookie("token")){
						delCookie("token");
					}
					store.commit('setLoginStatus', true);
					store.commit('changelLoginStatus', true);
			}
    }
    return Promise.reject(error.response.data)   // 返回接口返回的错误信息
  })
  
// http response 拦截器
// axios.interceptors.response.use(
//   response => {
// //response.data.errCode是我接口返回的值，如果值为2，说明Cookie丢失，然后跳转到登录页，这里根据大家自己的情况来设定
//     if(response.data.errCode == 2) {
//       router.push({
//         path: '/login',
//         query: {redirect: router.currentRoute.fullPath} //从哪个页面跳转
//       })
//     }
//     return response;
//   },
//   error => {
//     return Promise.reject(error.response.data)
//   });
 
export default axios;
 
/**
 * fetch 请求方法
 * @param url
 * @param params
 * @returns {Promise}
 */
export function fetch(url, params = {}) {
 
  return new Promise((resolve, reject) => {
    axios.get(url, {
      params: params
    })
    .then(response => {
      resolve(response.data);
    })
    .catch(err => {
      reject(err)
    })
  })
}
 
/**
 * post 请求方法
 * @param url
 * @param data
 * @returns {Promise}
 */
export function post(url, data = {}) {
  return new Promise((resolve, reject) => {
    axios.post(url, data)
      .then(response => {
        resolve(response.data);
      }, err => {
        reject(err);
      })
  })
}
 
/**
 * patch 方法封装
 * @param url
 * @param data
 * @returns {Promise}
 */
export function patch(url, data = {}) {
  return new Promise((resolve, reject) => {
    axios.patch(url, data)
      .then(response => {
        resolve(response.data);
      }, err => {
        reject(err);
      })
  })
}
 
/**
 * put 方法封装
 * @param url
 * @param data
 * @returns {Promise}
 */
export function put(url, data = {}) {
  return new Promise((resolve, reject) => {
    axios.put(url, data)
      .then(response => {
        resolve(response.data);
      }, err => {
        reject(err);
      })
  })
}