import Vue from 'vue'
import Router from 'vue-router'

import {delCookie,getCookie, setCookie} from '@/utils/cookies'
import store from '@/store/index.js'


import HelloWorld from '@/components/HelloWorld'
import test from '@/components/test'
import test1 from '@/components/test1'

import Index from '@/views/Index'

//------- homepage中的内容
import Homepage from '@/views/Homepage'
import H_tuijian from '@/views/Homepage/H_tuijian'
import H_detail from '@/views/Homepage/H_tuijian/H_detail'

//国学人物部分
import H_guoren from '@/views/Homepage/H_guoren'
import HG_person from '@/views/Homepage/H_guorens/HG_person'
import Index_Guoren from '@/views/Homepage/H_guorens/Index_Guoren'
import HG_chunqiu from '@/views/Homepage/H_guorens/HG_chunqiu'
// 诗词清话部分
import H_shiqing from '@/views/Homepage/H_shiqing'
import Index_Shiqing from '@/views/Homepage/H_shiqing/Index_Shiqing'
import HS_detail from '@/views/Homepage/H_shiqing/HS_detail'
// 经济史论部分
import H_jingshi from '@/views/Homepage/H_jingshi'
import Index_Jingshi from '@/views/Homepage/H_jingshi/Index_Jingshi'
import IJ_Right_Msg from '@/views/Homepage/H_jingshi/Index_Jingshi/IJ_Right_Msg'
import HJ_detail from '@/views/Homepage/H_jingshi/HJ_detail'
// 哲学文化
import H_zhewen from '@/views/Homepage/H_zhewen'
import Index_Zhewen from '@/views/Homepage/H_zhewen/Index_Zhewen'
import HZ_detail from '@/views/Homepage/H_zhewen/HZ_detail'

//-------- 国学司南页面
import Guide from '@/views/Guide'
import Index_Guide from '@/views/Guide/Index_Guide'
import Guide_detail from '@/views/Guide/Guide_detail'

// -----经典导读页面
import Daodu from '@/views/Daodu'
import Index_Daodu from '@/views/Daodu/Index_Daodu'
import DU_right from '@/views/Daodu/Index_Daodu/DU_right'
import D_detail from '@/views/Daodu/D_detail'

// -----资源下载界面
import Source from '@/views/Source'

//  ----论坛页面
import Forum from '@/views/Forum'
import Index_Forum from '@/views/Forums/Index_Forum'
import Forum_list from '@/views/Forums/Forum_list'
import Forum_list_right from '@/views/Forums/Forum_list/Forum_list_right'
import Forum_detail from '@/views/Forums/Forum_detail'
import Forum_publish from '@/views/Forums/Forum_publish'
import Forum_sort from '@/views/Forums/Forum_sort'

// ---个人信息页面
import Person_Msg from '@/views/Person_Msg'
import PM_right1 from '@/views/Person_Msg/PM_right1'
import PM_right2 from '@/views/Person_Msg/PM_right2'
import PM_right3 from '@/views/Person_Msg/PM_right3'
import PM_right4 from '@/views/Person_Msg/PM_right4'
import PM_right5 from '@/views/Person_Msg/PM_right5'

import PM_right5_1 from '@/views/Person_Msg/PM_right5/PM_right5_1'
import PM_right5_2 from '@/views/Person_Msg/PM_right5/PM_right5_2'
import PM_right5_3 from '@/views/Person_Msg/PM_right5/PM_right5_3'

Vue.use(Router)

const router = new Router({
	mode:'history',//默认是hash模式
	linkActiveClass:'menvscode-active',
	scrollBehavior(to,from,savePosition){ // 在点击浏览器的“前进/后退”，或者切换导航的时候触发。
		// console.log(to) // to：要进入的目标路由对象，到哪里去
		// console.log(from) // from：离开的路由对象，哪里来
		// console.log(savePosition) // savePosition：会记录滚动条的坐标，点击前进/后退的时候记录值{x:?,y:?}
// 		if(savePosition) {
// 			return savePosition;
// 		}else{
// 			return {x:0,y:0}
// 		}
		if(to.hash){ //先判断目标路由有没有hash值
			return {selector:to.hash}
		}
	},
    routes: [
		{
			path: '/',
			name: 'Index',
			component: Index,
			children: [
				{
					path: '',
					component: Homepage,
					children: [
						{
							path: '',
							component: H_tuijian,
						},
						{
							path: 'H_detail/:id',
							component: H_detail
						},
						{
							path: 'H_zhewen',
							component: H_zhewen,
							children: [
								{
									path: '',
									component: Index_Zhewen
								},
								{
									path: 'HZ_detail/:id',
									component: HZ_detail
								}
							]
						},
						{
							path: 'H_shiqing',
							component: H_shiqing,
							children: [
								{
									path: '',
									component: Index_Shiqing,
								},
								{
									path: 'HS_detail/:id',
									component: HS_detail
								},
							]
						},
						{
							path: 'H_jingshi',
							component: H_jingshi,
							children: [
								{
									path: '',
									component: Index_Jingshi,
									children: [
										{
											path: '',
											component: IJ_Right_Msg
										},
										{
											path: 'detail',
											component: IJ_Right_Msg
										},
										
									]
								},
								{
									path: 'HJ_detail/:id',
									component: HJ_detail
								},
								{
									path: 'HG_chunqiu/:id',
									component: HG_chunqiu
								}
							]
						},
						{
							path: 'H_guoren',
							component: H_guoren,
							children: [
								{
									path: '',
									component: Index_Guoren
								},
								{
									path: 'HG_person/:id',
									component: HG_person
								},
								{
									path: 'HG_chunqiu/:id',
									component: HG_chunqiu
								}
							]
						},
					]
				},
				{
					path: 'Forum',
					component: Forum,
					children: [
						{
							path: '',
							component: Index_Forum,
							meta:{requireAuth: true }
						},
						{
							path: 'Forum_list',
							component: Forum_list,
							children: [
								{
									path: '',
									component: Forum_list_right,
								},
							]
						},
						{
							path: 'Forum_detail',
							component: Forum_detail,
							meta:{requireAuth: true }
						},
						{
							path: 'Forum_detail1',
							component: Forum_detail,
							meta:{requireAuth: true }
						},
						{
							path: 'Forum_publish',
							component: Forum_publish,
							meta:{requireAuth: true }
						},
						{
							path: 'Forum_sort',
							component: Forum_sort,
						},
					]
				},
				{
					path: 'Daodu',
					component: Daodu,
					children: [
						{
							path: '',
							component: Index_Daodu,
							children: [
								{
									path: '',
									component: DU_right
								},
								{
									path: 'detail',
									component: DU_right
								}
							]
						},
						{
							path: 'D_detail',
							component: D_detail
						}
					]
				},
				{
					path: 'Source',
					component: Source,
				},
				{
					path: 'Guide',
					component: Guide,
					children: [
						{
							path: '',
							component: Index_Guide
						},
						{
							path: 'Guide_detail',
							component: Guide_detail
						}
					]
				},
				{
					path: 'Person_Msg',
					component: Person_Msg,
					children: [
						{
							path:'',
							component: PM_right1,
							meta:{requireAuth: true }
						},
						{
							path:'PM_right1',
							component: PM_right1,
							meta:{requireAuth: true }
						},
						{
							path:'PM_right2',
							component: PM_right2,
							meta:{requireAuth: true }
						},
						{
							path:'PM_right3',
							component: PM_right3,
							meta:{requireAuth: true }
						},
						{
							path:'PM_right4',
							component: PM_right4,
							meta:{requireAuth: true }
						},
						{
							path:'PM_right5',
							component: PM_right5,
							children: [
								{
									path: '',
									component:PM_right5_1,
									meta:{requireAuth: true }
								},
								{
									path: 'PM_right5_1',
									component: PM_right5_1,
									meta:{requireAuth: true }
								},
								{
									path:'PM_right5_2',
									component: PM_right5_2,
									meta:{requireAuth: true }
								},
								{
									path: 'PM_right5_3',
									component: PM_right5_3,
									meta:{requireAuth: true }
								}
							]
						},
					]
				}
			]
		},
		{
			path: '/test1',
			name: 'test1',
			component: test1
		},
    ]
})

// 使用 router.beforeEach 添加一个登录拦截器，判断用户是否登陆
router.beforeEach((to, from, next) => {
	if(to.meta.requireAuth) {
		if(store.state.login_status.login_status){
			next();
		}else{
			var token = store.state.login_status.token;
			if (token === 'null' || token === '') {
				router.push({path: '/'});
				if(getCookie('token')) {
				     delCookie('token');
				}
				if(getCookie('username')) {
				    delCookie('username');
				}
				if(getCookie('user_id')) {
				    delCookie('user_id');
				}
				store.commit('setLoginStatus', true);
				store.commit('changelLoginStatus', true);
				setCookie("n_url", to.path, 1);
			} else {
				next();
			}
		}
	}else{
		next();
	}
})
export default router;