<template>
	<div class="pm_r3">
		<div class="pm_r3_top">
			<div class="pm_r3_title">我的关注</div>
			<div class="pm_r3_right">共<span>{{follow_data.length}}</span>人</div>
		</div>
		<div class="pm_r3_msg">
			<div class="pm_r3_msg_each" v-for="(item,i) in follow_data" :key="i">
				<div class="pm_r3_msg_each_each1">
					<a href="javascript:;">
						<div class="pm_r3_msg_each_each1_img">
							<img :src="item.follow.img_link" width="46" height="46" style="border-radius: 6px;" :alt="item.follow.username">
						</div>
						<div class="pm_r3_msg_each_each1_msg">{{item.follow.username}}</div>
						<div class="pm_r33_msg_each_each3">{{item.add_time.replace("T", " ").split(".")[0]}}</div>
					</a>
				</div>
				<div class="pm_r3_msg_each_each2" @click="deletefollow(item.id)">取消关注</div>
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
		name:'PM_right3',
		data() {
			return {
				follow_data: ''
			}
		},
		methods: {
			get_guanzhu() {
				userfollow_msgs({
					user_ids: getCookie("user_id")
				}).then((response) => {
					this.follow_data = response.data;
				}).catch(function(error){
					console.log(error)
				})
			},
			deletefollow(id){
				if(confirm("确认取消关注吗？")){
					userfollow_msgs({
						delete_user_id: id
					}).then((response) => {
						this.get_guanzhu();
					}).catch(function(error){
						console.log(error)
					})
				}
			}
		},
		created(){
			this.get_guanzhu();
		}
	}
</script>

<style scoped="scoped">
	.pm_r33_msg_each_each3{
		float: right;
		height: 50px;
		/* line-height: 50px; */
		width: 153px;
		color: lightgray;
		font-size: 14px;
		margin-left: 65px;
	}
	.pm_r3{
		float: left;
		width: 770;
		margin-left: 30px;
		margin-top: 20px;
		/* border: 1px solid lightgray; */
		font-family: "microsoft yahei";
		text-align: left;
	}
	.pm_r3_top{
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
	.pm_r3_title{
		float: left;
		height: 73px;
		line-height: 73px;
		width: 406px;
		/* border-bottom: 1px solid lightgray; */
	}
	.pm_r3_right{
		float: right;
		height: 73px;
		line-height: 73px;
		width: 80px;
		font-weight: normal;
		font-size: 15px;
		text-align: right;
		margin-right: 1px;
	}
	.pm_r3_msg{
		float: left;
		width: 726px;
		height: 500px;
		
	}
	.pm_r3_msg_each{
		float: left;
		width: 726px;
		height: 70px;
		line-height: 70px;
		border-bottom: 1px dashed lightgray;
		font-size: 15px;
	}
	.pm_r3_msg_each_each1{
		float: left;
		height: 70px;
		line-height: 70px;
		width: 605px;
		transition: all 0.8s ease;
	}
	.pm_r3_msg_each_each1_img{
		float: left;
		width: 35px;
		height: 35px;
		line-height: 104px;
	}
	.pm_r3_msg_each_each1_msg{
		float: left;
		width: 300px;
		line-height: 70px;
		height: 70px;
		margin-left: 22px;
	}
	.pm_r3_msg_each_each1 span{
		font-size: 12px;
		color: darkgray;
	}
	.pm_r3_msg_each_each1 a{
		transition: all 0.8s ease;
	}
	.pm_r3_msg_each_each1 a:hover{
		text-decoration: none;
		color: royalblue;
		font-size: 16px;
	}
	.pm_r3_msg_each_each2{
		float: right;
		height: 36px;
		line-height: 36px;
		width: 80px;
		border: 1px solid lightgray;
		cursor: pointer;
		text-align: center;
		margin-top: 17px;
		border-radius: 6px;
		font-size: 13px;
		transition: all 0.9s ease;
	}
	.pm_r3_msg_each_each2:hover{
		background: lightgrey;
		color: white;
	}
	.pm_r3_msg_each_each3{
		float: left;
		height: 60px;
		line-height: 60px;
		width: 100px;
		color: lightgray;
		font-size: 14px;
		margin-left: 65px;
	}
		
</style>
