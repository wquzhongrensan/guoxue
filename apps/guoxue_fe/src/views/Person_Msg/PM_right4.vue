<template>
	<div class="pm_r4">
		<div class="pm_r4_top">
			<div class="pm_r4_title">我的粉丝</div>
			<div class="pm_r4_right">共<span>{{fan_data.length}}</span>人</div>
		</div>
		<div class="pm_r4_msg">
			<div class="pm_r4_msg_each" v-for="(item,i) in fan_data" :key="i">
				<div class="pm_r4_msg_each_each1">
					<a href="javascript:;">
						<div class="pm_r4_msg_each_each1_img">
							<img :src="item.user.img_link" width="46" height="46" style="border-radius: 6px;" :alt="item.user.username">
						</div>
						<div class="pm_r4_msg_each_each1_msg">{{item.user.username}}</div>
					</a>
				</div>
			</div>
		</div>
	</div>
</template>

<script>
	import {
		userfollow_msgs,
	} from '@/api/api';
	
	import {getCookie} from '@/utils/cookies';
	export default{
		name:'PM_right4',
		data() {
			return {
				fan_data: ''
			}
		},
		methods: {
			get_guanzhu() {
				userfollow_msgs({
					follow_ids: getCookie("user_id")
				}).then((response) => {
					this.fan_data = response.data;
				}).catch(function(error){
					console.log(error)
				})
			},
		},
		created(){
			this.get_guanzhu();
		}
	}
</script>

<style scoped="scoped">
	.pm_r4{
		float: left;
		width: 770;
		margin-left: 30px;
		margin-top: 20px;
		/* border: 1px solid lightgray; */
		font-family: "microsoft yahei";
		text-align: left;
	}
	.pm_r4_top{
		float: left;
		width: 726px;
		height: 73px;
		font-size: 25px;
		font-weight: 600;
		font-family: "microsoft yahei";
		line-height: 65px;
		overflow: hidden;
		border-bottom: 1px solid lightgray;
		/* text-indent: 20px; */
		/* margin-left: 20px; */
	}
	.pm_r4_title{
		float: left;
		height: 73px;
		line-height: 73px;
		width: 406px;
		/* border-bottom: 1px solid lightgray; */
	}
	.pm_r4_right{
		float: right;
		height: 73px;
		line-height: 73px;
		width: 80px;
		font-weight: normal;
		font-size: 15px;
		text-align: right;
		margin-right: 1px;
	}
	.pm_r4_msg{
		float: left;
		width: 726px;
		height: 500px;
		
	}
	.pm_r4_msg_each{
		float: left;
		width: 726px;
		height: 70px;
		line-height: 70px;
		border-bottom: 1px dashed lightgray;
		font-size: 15px;
	}
	.pm_r4_msg_each_each1{
		float: left;
		height: 70px;
		line-height: 70px;
		width: 400px;
		transition: all 0.8s ease;
	}
	.pm_r4_msg_each_each1_img{
		float: left;
		width: 35px;
		height: 35px;
		line-height: 104px;
	}
	.pm_r4_msg_each_each1_msg{
		float: left;
		width: 300px;
		line-height: 70px;
		height: 70px;
		margin-left: 22px;
	}
	
	.pm_r4_msg_each_each1 a{
		transition: all 0.8s ease;
	}
	.pm_r4_msg_each_each1 a:hover{
		text-decoration: none;
		color: royalblue;
		font-size: 15px;
	}
	
		
</style>
