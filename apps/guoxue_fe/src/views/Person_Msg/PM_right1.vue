<template>
	<div class="pm_r1">
		<div class="pm_r1_title"><div>个人资料</div></div>
		<div class="pm_r1_msg">
			<div class="pm_r1_mag_left">
				<div class="pm_r1_mag_left_img">
					<img :src="person_msg.img_link" style="border-radius: 50%;" width="120" height="120" alt="用户头像">
				</div>
				<div class="pm_r1_mag_left_name">
					<input @change="upload_ava($event)" style="width: 155px;font-size: 12px;margin-left: -12px;" type="file" name="avatar" value="修改用户头像">
				</div>
			</div>
			<div class="pm_r1_msg_right">
				<div class="pm_r1_msg_right_top">
					<div class="pm_r1_msg_right_top_left">
						<div class="pm_r1_msg_right_top_left_each1">ID: {{person_msg.username}}</div>
						<div class="pm_r1_msg_right_top_left_each2">关注： {{person_msg.attention}}  粉丝： {{person_msg.fans}}</div>
					</div>
				</div>
				<div class="pm_r1_msg_right_bottom">
					<div class="pm_r1_msg_right_bottom_left">
						<div class="pm_r1_msg_right_bottom_left_each2">实名：{{person_msg.name}}</div>
						<div class="pm_r1_msg_right_bottom_left_each2">性别：{{person_msg.gender == 'male' ? '男' : '女'}}</div>
						<div class="pm_r1_msg_right_bottom_left_each2">生日：{{dateFormat(person_msg.birthday)}}</div>
						<div class="pm_r1_msg_right_bottom_left_each2">邮箱：{{person_msg.email}}</div>
						<div class="pm_r1_msg_right_bottom_left_each2">地区：{{person_msg.area}}</div>
						<div class="pm_r1_msg_right_bottom_left_each2">简介：{{person_msg.introduce}}</div>
					</div>
					<div class="pm_r1_msg_right_bottom_right">
						<!-- <router-link to="">修改资料>></router-link> -->
						<el-button type="text" @click="dialogFormVisible = true" style="color:blue">修改资料>></el-button>
					</div>
					<el-dialog title="个人资料修改" :visible.sync="dialogFormVisible">
						<el-form ref="form" :model="person_msg" label-width="80px">
						    <el-form-item label="昵称" >
								<el-input v-model="person_msg.name" style="width: 200px;"></el-input>
							</el-form-item>
							<el-form-item label="邮箱" >
								<el-input v-model="person_msg.email" style="width: 200px;"></el-input>
							</el-form-item>
							<el-form-item label="性别">
								<el-radio-group v-model="person_msg.gender">
								    <el-radio label="male"></el-radio>
								    <el-radio label="female"></el-radio>
								</el-radio-group>
							</el-form-item>
							<el-form-item label="出生日期">
								<el-col :span="11">
									<el-date-picker type="date" placeholder="选择日期" v-model="person_msg.birthday" style="width: 100%;"></el-date-picker>
								</el-col>
							</el-form-item>
							<el-form-item label="地区">
								<el-input v-model="person_msg.area" style="width: 200px;"></el-input>
							</el-form-item>
							<el-form-item label="简介">
								<el-input type="textarea" v-model="person_msg.introduce"></el-input>
							</el-form-item>
						</el-form>
					  
					  <div slot="footer" class="dialog-footer">
						<el-button @click="dialogFormVisible = false">取 消</el-button>
						<el-button type="primary" @click="get_person_infos" style="background: gray;border: 1px solid gray;">确 定</el-button>
					  </div>
					</el-dialog>
				</div>
			</div>
		</div>
	</div>
</template>

<script>
	import { getCookie, setCookie } from '@/utils/cookies'
	import {host, person_infos, person_info, person_avatars} from '@/api/api';
	import axios from '@/axios/http';
	
	export default{
		name:'PM_right1',
		data(){
			return {
				dialogFormVisible: false,
				form: {
				  nickname: '',
				  realname: '',
				  sex: '',
				  date1: '',
				  area: '',
				  desc: ''
				},
				formLabelWidth: '100px',
				person_msg: ''
			}
		},
		methods: {
			edit_msg() {
				this.dialogFormVisible = false;
				alert(this.form.nickname+"11"+this.form.realname+"11"+this.form.sex+"11"+this.dateFormat(this.form.date1)+"11"+this.form.desc);
				// 在这里就可发送axiso请求修改数据
			},
			dateFormat(dataStr){
				var dt = new Date(dataStr);
				// yyyy-mm-dd
				var y = dt.getFullYear();
				var m = dt.getMonth() + 1;
				var d = dt.getDate();
				var hh = dt.getHours();
				var mm = dt.getMinutes();
				var ss = dt.getSeconds();
				return y + "-" + m + "-" + d ;
			},
			get_person_info(){
				person_info({
					username: getCookie("username"),
				}).then((response) => {
					this.person_msg = response.data[0]
					console.log(this.person_msg )

				})
				.catch(function (error) {
					console.log(error);
				});
			},
			get_person_infos(){
				person_infos({
					method: "put",
					id: getCookie("user_id"),
					name: this.person_msg.name,
					email: this.person_msg.email,
					gender: this.person_msg.gender,
					birthday: this.person_msg.birthday,
					area: this.person_msg.area,
					introduce: this.person_msg.introduce
				}).then(response => {
					this.dialogFormVisible = false;
					this.person_msg = response.data
				})
				.catch(function (error) {
					console.log(error);
				});
			},
			// 修改用户头像
			upload_ava(e){
			    let file = e.target.files[0];           
				let param = new FormData(); //创建form对象
				param.append('img_link',file,file.name);//通过append向form对象添加数据
				param.append('chunk','0');//添加form表单中其他数据
				console.log(param.get('img_link')); //FormData私有类对象，访问不到，可以通过get判断值是否传进去
				let config = {
					headers:{'Content-Type':'multipart/form-data'}
				};  //添加请求头
				axios.patch(host+'/person_infos/'+getCookie("user_id")+'/',param,config)
				.then(response=>{
					this.person_msg.img_link = response.data.img_link;
				})        
			}
		},
		created(){
			this.get_person_info();
		}
	}
</script>

<style scoped="scoped">
	.pm_r1{
		float: left;
		width: 726px;
		margin-left: 30px;
		margin-top: 20px;
		/* border: 1px solid lightgray; */
		font-family: "microsoft yahei";
		text-align: left;
		font-size: 14px;
	}
	.pm_r1_title{
		float: left;
		width: 726px;
		height: 73px;
		font-size: 25px;
		font-weight: 600;
		font-family: "microsoft yahei";
		line-height: 65px;
		/* text-indent: 20px; */
		/* margin-left: 20px; */
	}
	.pm_r1_title div{
		float: left;
		height: 73px;
		line-height: 73px;
		width: 726px;
		border-bottom: 1px solid lightgray;
	}
	.pm_r1_msg{
		float: left;
		width: 726px;
		margin-top: 10px;
		height: 500px;
	}
	.pm_r1_mag_left{
		float: left;
		width: 120px;
		height: 190px;
		/* border: 1px solid lightgray; */
	}
	.pm_r1_mag_left_img{
		float: left;
		width: 120px;
		height: 70px;
	}
	
	.pm_r1_mag_left_name{
		float: left;
		width: 120px;
		height: 30px;
		margin-top: 58px;
		text-align: center !important;
	}
	.pm_r1_mag_left_name a{
		color: blue;
	}
	.pm_r1_msg_right{
		float: right;
		width: 616px;
		margin-right: -43px;
		height: 500px;
	}
	.pm_r1_msg_right_top{
		float: left;
		width: 570px;
		height: 60px;
		border-bottom: 1px solid lightgray;
	}
	.pm_r1_msg_right_top_left{
		float: left;
		width: 300px;
		height: 60px;
	}
	.pm_r1_msg_right_top_left_each1{
		float: left;
		width: 300px;
		height: 30px;
		line-height: 30px;
	}
	.pm_r1_msg_right_top_left_each2{
		float: left;
		width: 300px;
		line-height: 30px;
		height: 30px;
		color: black;
	}
	.pm_r1_msg_right_bottom{
		float: left;
		width: 570px;
		height: 60px;
	}
	.pm_r1_msg_right_bottom_left{
		float: left;
		width: 300px;
		height: 60px;
	}
	.pm_r1_msg_right_bottom_left_each1{
		float: left;
		width: 300px;
		height: 30px;
		line-height: 30px;
	}
	.pm_r1_msg_right_bottom_left_each2{
		float: left;
		width: 300px;
		line-height: 30px;
		height: 30px;
		color: black;
	}
	.pm_r1_msg_right_bottom_right{
		float: right;
		width: 80px;
		height: 60px;
		line-height: 60px;
		color: blue;
	}
	.pm_r1_msg_right_bottom_right a{
		color: blue;
	}
		
</style>
