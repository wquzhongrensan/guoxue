<template>
	<div class="a_header">
		<div id="head">
			<div id="head-menu">
				<div id="head-menu-body">
					<div id="head-mbL">
						<ul class="menu-list">
							<li class="s_title">
								<router-link to="/">国学之家</router-link>
							</li>
						</ul>
					</div>
					<div id="head-mbR">
						<ul class="menu-list">
							<li class="s_li_back">
								<router-link to="/" :class="{choose_style: choose_1s}">首页</router-link>
								<!-- <a href="/">首页</a> -->
							</li>
							<li class="s_li_back">
								<router-link to="/Forum" :class="{choose_style: choose_2s}">论坛</router-link>
								<!-- <a href="/text">论坛</a> -->
							</li>
							<li class="s_li_back1">
								<router-link to="/Daodu" :class="{choose_style: choose_3s}">经典导读</router-link>
							</li>
							<li class="s_li_back1">
								<router-link to="/Guide" :class="{choose_style: choose_4s}">国学司南</router-link>
							</li>
							<li class="s_li_back1">
								<!-- <router-link to="/Source" :class="{choose_style: choose_5s}">资源共享</router-link> -->
							</li>
							<li>
								<div style="width: 0px; height: 20px;	"></div>
							</li>
							<li class="s_search_text">
								<div class="s_search_2">
									<!-- <input class="s_search_text_1" type="text" value="helo"> -->
									<input class="s_search_style fl" placeholder="Search" />
									<a class="s_search fl" href="">搜索</a>
								</div>
							</li>
							<li class="s_li_back" v-show="!username">
								<a href="javascript:;" @click="show_logins">登录</a>
							</li>
							<li class="s_li_back" v-show="!username">
								<a href="javascript:;" @click="show_registers">注册</a>
							</li>
							<li class="s_li_back2" v-show="username">
								<router-link to="/Person_Msg/PM_right1?t=1" :class="{choose_style: choose_6s}">{{username}}</router-link>
							</li>
							<li class="s_li_back" v-show="username">
								<a href="javascript:;" @click="login_out">退出</a>
							</li>
						</ul>
					</div>
				</div>
			</div>
		</div>
	</div>
</template>
<script>
	import { mapState } from 'vuex'
	import { getCookie, delCookie, setCookie } from '@/utils/cookies'
	import {login_TP} from '@/api/api'
	export default{
		name: 'Sub_nav_top',
		created(){
			this.get_route_query();
		},
		methods: {
			show_logins() {
				this.$store.commit('changelLoginStatus', true)
			},
			show_registers() {
				this.dialogFormVisible_register = true
				this.$emit("showregister",this.dialogFormVisible_register);
			},
			login_out(){
				if(getCookie("username")){
					delCookie("username");
				}
				if(getCookie("token")){
					delCookie("token");
				}
				if(getCookie("user_id")){
					delCookie("user_id");
				}
				this.$store.commit('LoginOut', false);
				this.$router.push({path: '/'});
			},
			get_route_query(){
				this.route_data = this.$route.fullPath.split("/")[1];
				if(this.route_data == ""){
					this.choose_1 = true;
					this.choose_2 = false;
					this.choose_3 = false;
					this.choose_4 = false;
					this.choose_5 = false;
					this.choose_6 = false;
				}else if(this.route_data == "Forum"){
					this.choose_1 = false;
					this.choose_2 = true;
					this.choose_3 = false;
					this.choose_4 = false;
					this.choose_5 = false;
					this.choose_6 = false;
				}else if(this.route_data == "Daodu"){
					this.choose_1 = false;
					this.choose_2 = false;
					this.choose_3 = true;
					this.choose_4 = false;
					this.choose_5 = false;
					this.choose_6 = false;
				}else if(this.route_data == "Guide"){
					this.choose_1 = false;
					this.choose_2 = false;
					this.choose_3 = false;
					this.choose_4 = false;
					this.choose_5 = true;
					this.choose_6 = false;
				}else if(this.route_data == "Source"){
					this.choose_1 = false;
					this.choose_2 = false;
					this.choose_3 = false;
					this.choose_4 = false;
					this.choose_5 = true;
					this.choose_6 = false;
				}else{
					this.choose_1 = false;
					this.choose_2 = false;
					this.choose_3 = false;
					this.choose_4 = false;
					this.choose_5 = false;
					this.choose_6 = true;
				}
			}

		},
		data() {
			return {
				// session_status: false,
				session_status: true,
				dialogFormVisible_login: false,
				dialogFormVisible_register: false,
				route_data: '',
				choose_1: true,
				choose_2: false,
				choose_3: false,
				choose_4: false,
				choose_5: false,
				choose_6: false,
			}
		},
		computed: {
			...mapState({
					username: state => state.login_status.username,
			}),
			choose_1s(){
				if(this.$route.fullPath.split("/")[1] == ""){
					this.choose_1 = true;
					this.choose_2 = false;
					this.choose_3 = false;
					this.choose_4 = false;
					this.choose_5 = false;
					this.choose_6 = false;
				}
				return this.choose_1
			},
			choose_2s(){
				if(this.$route.fullPath.split("/")[1] == "Forum"){
					this.choose_1 = false;
					this.choose_2 = true;
					this.choose_3 = false;
					this.choose_4 = false;
					this.choose_5 = false;
					this.choose_6 = false;
				}
				return this.choose_2
			},
			choose_3s(){
				if(this.$route.fullPath.split("/")[1] == "Daodu"){
					this.choose_1 = false;
					this.choose_2 = false;
					this.choose_3 = true;
					this.choose_4 = false;
					this.choose_5 = false;
					this.choose_6 = false;
				}
				return this.choose_3
			},
			choose_4s(){
				if(this.$route.fullPath.split("/")[1] == "Guide"){
					this.choose_1 = false;
					this.choose_2 = false;
					this.choose_3 = false;
					this.choose_4 = true;
					this.choose_5 = false;
					this.choose_6 = false;
				}
				return this.choose_4
			},
			choose_5s(){
				if(this.$route.fullPath.split("/")[1] == "Source"){
					this.choose_1 = false;
					this.choose_2 = false;
					this.choose_3 = false;
					this.choose_4 = false;
					this.choose_5 = true;
					this.choose_6 = false;
				}
				return this.choose_5
			},
			choose_6s(){
				if(this.$route.fullPath.split("/")[1] == "Person_Msg"){
					this.choose_1 = false;
					this.choose_2 = false;
					this.choose_3 = false;
					this.choose_4 = false;
					this.choose_5 = false;
					this.choose_6 = true;
				}
				return this.choose_6
			},
		},

	}
</script>
<style scoped="scoped">
	.a_header{
		background-color: black;
		opacity: 0.8;
		height: 60px;

	}
	.s_title{
		font-size: 20px;
		font-family: "microsoft yahei";
	}
	.s_search_style {
		margin-top: 16px;
	    display: inline-block;
	    box-sizing: content-box;
	    padding: 5px 15px;
	    border: 1px solid #b7b7b7;
  	    border-radius: 3px;
	    font: normal 16px/normal "Times New Roman", Times, serif;
	    color: rgba(0,142,198,1);
	    text-overflow: clip;
	    background: rgba(252,252,252,1);
	    box-shadow: 2px 2px 2px 0 rgba(0,0,0,0.2) inset;
	    text-shadow: 1px 1px 0 rgba(255,255,255,0.66) ;
	    transition: all 200ms cubic-bezier(0.42, 0, 0.58, 1);
	    transform: rotateX(-0.5729577951308232deg) rotateY(19.48056503444799deg)   ;
	}
	.s_li_back a{
		display: block;
		margin-top: 18px;
		height: 26px;
		width: 39px;
		line-height: 26px;
		border-radius: 7px;
		font-family: Arial, Helvetica, sans-serif;
		color: #ccc;
		transition: all 0.8s ease;
	}
	.s_li_back a:hover{
		text-decoration: none;
		color: white;
	}
	.choose_style{
		text-decoration: none !important;
		color: white !important;
	}
	.s_li_back1 a{
		display: block;
		margin-top: 18px;
		height: 26px;
		width: 73px;
		line-height: 26px;
		border-radius: 7px;
		font-family: Arial, Helvetica, sans-serif;
		color: #ccc;
		transition: all 0.8s ease;
	}
	.s_li_back1 a:hover{
		text-decoration: none;
		color: white;
	}
	.s_li_back2 a{
		display: block;
		margin-top: 18px;
		height: 26px;
		width: 100px;
		line-height: 26px;
		border-radius: 7px;
		font-family: Arial, Helvetica, sans-serif;
		color: #ccc;
		transition: all 0.8s ease;
	}
	.s_li_back2 a:hover{
		text-decoration: none;
		color: white;
	}


	.s_search_2{
		line-height: 60px;
	}
	.s_search {
		color: #fff;
		background-color: gray;
		height: 31px;
		margin-top: 15px;
		line-height: 31px;
		margin-left: -7px;
		width: 45px;
		border-radius: 4px;
	}
	.s_search:hover{
		background-color: gray;
		opacity: 0.8;
	}
	#head {
		color: #fff;
	    height: 60px;
	    width: 100%;
	    background-position: center;
		text-align: center;
		font-size: 14px;
		line-height: 60px;

	}
	.fl {
	    float: left;
	}
	#head-menu {
		display: inline-block;
		margin-x: auto;
	    height: 60px;
	    width: 100%;
	    background-color: rgba(255, 255, 255, 0.4);
	}
	#head-menu-body {
	    height: 60px;
	    width: 1027px;
	    margin: 0 auto;
	    position: relative;
	}
	#head-mbL {
	    float: left;
	}
	#head-mbL>ul>li{
	    line-height: 60px;
	    text-align: center;
	    float: left;
	    margin: auto 5px;
	    padding: 0 8px;
		font-family: 华文行楷, 'Lucida Grande', Verdana, Arial, Sans-Serif;
		font-size: 24px;
	}
	#head-mbL>ul>li>a{
		color: white;
		text-decoration: none;
	}
	#head-mbL>ul>li>a:hover{
		text-decoration: none;

	}
	#head-mbR {
		margin-left: 20px;
	    /* float: right; */
	}
	#head-mbR>ul>li {
	    line-height: 60px;
	    text-align: center;
	    float: left;
	    margin: auto 5px;
	    padding: 0 8px;
		margin-left: -1px;
	}

</style>
