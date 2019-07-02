<template>
	<div id="app">
		<Sub_nav_top @showlogin="getlogin" @showregister="getregister"></Sub_nav_top>
		<el-dialog title="用户登录" width="450px" style="text-align: center;font-family: 华文行楷, 'Lucida Grande', Verdana, Arial, Sans-Serif;;" :visible.sync="login_status1">
			<el-form ref="LoginForm" :rules="rule_login" :model="form">
				<el-form-item prop="username_login" label="账号" :label-width="formLabelWidth" label-fontSize="16px !important">
					<el-input v-model="form.username_login" style="width: 250px;margin-left: -40px;" autocomplete="off"></el-input>
				</el-form-item>
				<el-form-item prop="password_login" label="密码" :label-width="formLabelWidth">
					<el-input type="password" v-model="form.password_login"  style="width: 250px;margin-left: -40px;" autocomplete="off"></el-input>
				</el-form-item>
				<el-form-item prop="type" style="color: gray !important;">
					<el-checkbox-group v-model="form.login_status" style="float: left;width: 50%;">
						<el-checkbox label="记住用户" name="type" style="margin-left:30%;color: gray !important;"></el-checkbox>
					</el-checkbox-group>
					<label id="login_tp" style="margin-right: 10px;width: 40%;float: right;" @click="login_TPs">第三方登录</label>
				</el-form-item>
			</el-form>
			<div slot="footer" class="dialog-footer " style="text-align: center;">
				<el-button type="primary" @click="logins" style="border:1px solid gray;background: gray;color:white;">登 录</el-button>
				<el-button @click="change_login">取 消</el-button>
			</div>
		</el-dialog>
		<el-dialog title="用户注册" width="450px" style="text-align: center;font-family: 华文行楷, 'Lucida Grande', Verdana, Arial, Sans-Serif !important;" :visible.sync="dialogFormVisible_register">
			<el-form ref="RegisterFrom" :model="form_register" :rules="rules">
				<el-form-item label="用户名" prop="username" :label-width="formLabelWidth" label-fontSize="16px !important">
					<el-input v-model="form_register.username" style="width: 250px;margin-left: -40px;" autocomplete="off"></el-input>
				</el-form-item>
				<el-form-item label="密码" prop="password" :label-width="formLabelWidth">
					<el-input type="password" v-model="form_register.password"  style="width: 250px;margin-left: -40px;" autocomplete="off"></el-input>
				</el-form-item>
				<el-form-item label="确认密码" prop="rpassword" :label-width="formLabelWidth">
					<el-input type="password" v-model="form_register.rpassword"  style="width: 250px;margin-left: -40px;" autocomplete="off"></el-input>
				</el-form-item>
				<el-form-item label="邮箱" prop="email" :label-width="formLabelWidth">
					<el-input type="email" v-model="form_register.email"  style="width: 250px;margin-left: -40px;" autocomplete="off"></el-input>
				</el-form-item>
			</el-form>
			<div slot="footer" class="dialog-footer " style="text-align: center;">
				<el-button type="primary" @click="registers" style="border:1px solid gray;background: gray;color:white;">注 册</el-button>
				<el-button @click="dialogFormVisible_register = false">取 消</el-button>
			</div>
		</el-dialog>
		<!-- <img src="../assets/logo.png"> -->
		<!-- <router-link to="/">hello</router-link>
		<router-link to="/test">test</router-link> -->
		<router-view></router-view>
		<!-- <HelloWord></HelloWord> -->
	</div>
</template>
<script>
	import { mapState } from 'vuex'
	import { register, login, get_users_id } from '@/api/api'
	import Sub_nav_top from '@/components/Sub_nav_top'
	import HelloWorld from '@/components/HelloWorld'
	import {setCookie, getCookie, delCookie} from '@/utils/cookies'
	
	export default{
		name: 'Index',
		components: {
			Sub_nav_top,
			// Sub_nav_homepage,
		},
		methods: {
			getlogin(dialogFormVisible_login) {
				this.dialogFormVisible_login = dialogFormVisible_login;
			},
			getregister(dialogFormVisible_register) {
				this.dialogFormVisible_register = dialogFormVisible_register;
			},
			change_login(){
				this.$store.commit('changelLoginStatus', false)
			},
			login_TPs(){
			    if(confirm("确认通过微博登录吗？")){
			      this.$router.push({"path": 'login/weibo'});
			      this.$router.go(0);
			    }
			},
			logins(){
				this.$refs.LoginForm.validate((valid) => {
     				if(valid) {
						login({
							username: this.form.username_login,
							password: this.form.password_login, 
						}).then((response) => {
							if (response.data.err_code == "0") {
								alert("账号尚未确认，请先前往邮箱确认账号")
							}else{
								console.log(response.data.user_id);
								setCookie("user_id", response.data.user_id, 7);
								setCookie("username", this.form.username_login, 7);
								setCookie("token", response.data.token, 7);
								// 此时触发vuex保存数据
								this.$store.commit('setLoginStatus', false)
								this.$store.commit('changelLoginStatus', false)
								this.form.password_login = '';
								if(getCookie("n_url") ? getCookie("n_url") : ''){
									this.$router.push({path: getCookie("n_url")})
									delCookie("n_url")
								}
							}
							
							
// 							// 获取用户的id
// 							get_users_id({
// 								username: getCookie("username"),
// 							}).then((response) => {
// 								setCookie("user_id", response.data[0]["id"], 7);
// 							})
// 							.catch(function (error) {
// 								console.log(error);
// 							});
						})
						.catch(function (error) {
							console.log()
							alert("用户名或者密码错误，麻烦您重新确认一下！！")
							console.log(error);
						});
					}else {
						console.log('error submit');
						return false;
					}
				});
			},
			registers(){
				this.$refs.RegisterFrom.validate((valid) => {
     				if(valid) {
						if(this.form_register.password != this.form_register.rpassword){
							alert("密码与确认密码必须一致");
							return;
						}
						register({
							username: this.form_register.username,
							password: this.form_register.password, 
							rpassword: this.form_register.rpassword,
							email: this.form_register.email
						}).then((response) => {
// 							setCookie("username", response.data.username, 7);
// 							setCookie("token", response.data.token, 7);
// 							setCookie("user_id", response.data.user_id, 7);

							// 此时触发vuex保存数据
							this.$store.commit('setLoginStatus', false)
							this.dialogFormVisible_register = false;
							this.form_register.username = '';
							this.form_register.password = '';
							this.form_register.rpassword = '';
						})
						.catch(function (error) {
							console.log(error);
						});
					}else {
						console.log('error submit');
						return false;
					}
				});
			}
		},
		computed: {
			...mapState({
					login_status1: state => state.login_status.login_status,
			}),
		},
		data(){
			return{
				dialogFormVisible_login: false,
				dialogFormVisible_register: false,

				form: {
				  username_login: '',
				  password_login: '',
				  login_status: true,
				  email: '',
				},
				form_register: {
				  username: '',
				  password: '',
				  rpassword: '',
				  email: '',
				},
				formLabelWidth: '100px',
				rule_login: {
					username_login: [
						{required: true, message:'请输入账号',trigger: 'blur'}
					],
					password_login: [
						{required: true, message:'请输入密码',trigger: 'blur'}
					]
				},
				rules: {
					username: [
						{required: true, message:'请输入用户名',trigger: 'blur'}
					],
					password: [
						{required: true, message:'请输入密码',trigger: 'blur'}
					],
					rpassword: [
						{required: true,message:'确认密码不能为空',trigger: 'blur'}
					],
					email: [
						{required: true, message:'请输入邮箱',trigger: 'blur'}
					],
				}
			}
		},
	}
</script>

<style scoped="scoped">
	#login_tp:hover{
		cursor: pointer;
	}
	#app {
		font-family: 'Avenir', Helvetica, Arial, sans-serif;
		-webkit-font-smoothing: antialiased;
		-moz-osx-font-smoothing: grayscale;
		text-align: center;
		color: #2c3e50;
		width: 100%;
		
	}
	body a:active{
		color: black !important;
		text-decoration: none !important;
	}
	/* .a_header{
		background-color: greenyellow;
		opacity: 0.8;
		height: 40px;
		width: 100%;
	} */
	.el-form-item__label{
		font-size: 15px !important;
	}
	.el-dialog__title{
		font-family: 华文行楷, 'Lucida Grande', Verdana, Arial, Sans-Serif !important;
	}
	.el-checkbox:last-child {
		margin-right: 200px !important;
	}
	
	.el-checkbox__label {
		color: gray !important;
	}
	.el-checkbox__input.is-checked .el-checkbox__inner, .el-checkbox__input.is-indeterminate .el-checkbox__inner {
		background-color: gray !important;
		border-color: #409EFF;
	}
</style>
