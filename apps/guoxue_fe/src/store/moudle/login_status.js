import {getCookie} from '@/utils/cookies'


const state = {
    login_status: false,
	username: getCookie('username') ? getCookie('username') : '',
	token: getCookie('token') ? getCookie('token') : '',
}

const mutations = {
	changelLoginStatus(state, str){
			state.login_status = str;
	},
	setLoginStatus(state, str){
		state.login_status = str;
		//  操作cookie
		state.username = getCookie("username") ? getCookie('username') : '';
		state.token = getCookie("token") ? getCookie('token') : '';
		// localStorage.setItem('Authorization', token);
	},
	LoginOut(state, str){
		state.login_status = str;
		//  操作cookie
		state.username = '';
		state.token = '';
		// localStorage.setItem('Authorization', token);
	}

}

export default{
	state: state,
	mutations: mutations
}