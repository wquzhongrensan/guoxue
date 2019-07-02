<template>
	<div class="pm_r2">
		<div class="pm_r2_top">
			<div class="pm_r2_title">我的收藏</div>
			<div class="pm_r2_right">共<span>{{fav_data.length}}</span>条</div>
		</div>
		<div class="pm_r2_msg">
			<div class="pm_r2_msg_each" v-for="(item,i) in fav_data" :key="i">
				<div class="pm_r2_msg_each_each1"><router-link :to="'/Forum/Forum_detail?id='+item.topic.id">{{item.topic.title}}<span>({{item.topic.author.username}})</span></router-link></div>
				<div class="pm_r2_msg_each_each2" @click="deleteFav(item.id)">取消收藏</div>
				<div class="pm_r2_msg_each_each3">{{item.add_time.replace("T", " ").split(".")[0]}}</div>
			</div>
			
		</div>
	</div>
</template>

<script>
	import {
		userfav_msgs,
	} from '@/api/api';
	
	import {getCookie} from '@/utils/cookies';
	
	export default{
		name:'PM_right2',
		data() {
			return {
				fav_data: '',
				del_i: 0,

			}
		},
		methods: {
			get_user_favdata() {
				userfav_msgs({
					userss:getCookie("user_id")
				}).then((response) => {
					this.fav_data = response.data
				})
				.catch(function (error) {
					console.log(error);
				});
			},
			deleteFav(id){
				if(confirm('确认取消收藏吗？')){
					userfav_msgs({
						fav_id: id,
					}).then((response) => {
						this.get_user_favdata();
						console.log("取消收藏成功")
					})
					.catch(function (error) {
						console.log(error);
					});
				}
				
			}
		},
		created(){
			this.get_user_favdata();
		}
	}
</script>

<style scoped="scoped">
	.pm_r2{
		float: left;
		width: 770;
		margin-left: 30px;
		margin-top: 20px;
		font-family: "microsoft yahei";
		text-align: left;
	}
	.pm_r2_top{
		float: left;
		width: 726px;
		height: 73px;
		font-size: 25px;
		font-weight: 600;
		font-family: "microsoft yahei";
		line-height: 65px;
		overflow: hidden;
		border-bottom: 1px solid lightgray;
	}
	.pm_r2_title{
		float: left;
		height: 73px;
		line-height: 73px;
		width: 406px;
		/* border-bottom: 1px solid lightgray; */
	}
	.pm_r2_right{
		float: right;
		height: 73px;
		line-height: 73px;
		width: 80px;
		font-weight: normal;
		font-size: 15px;
		text-align: right;
		margin-right: 1px;
	}
	.pm_r2_msg{
		float: left;
		width: 726px;
		height: 500px;
		
	}
	.pm_r2_msg_each{
		float: left;
		width: 726px;
		height: 50px;
		line-height: 50px;
		border-bottom: 1px dashed lightgray;
		font-size: 15px;
	}
	.pm_r2_msg_each_each1{
		float: left;
		height: 50px;
		line-height: 50px;
		width: 400px;
		transition: all 0.8s ease;
	}
	.pm_r2_msg_each_each1 span{
		font-size: 12px;
		color: darkgray;
	}
	.pm_r2_msg_each_each1 a{
		transition: all 0.8s ease;
	}
	.pm_r2_msg_each_each1 a:hover{
		text-decoration: none;
		color: royalblue;
		font-size: 16px;
	}
	.pm_r2_msg_each_each2{
		float: right;
		height: 36px;
		line-height: 36px;
		width: 80px;
		border: 1px solid lightgray;
		cursor: pointer;
		text-align: center;
		margin-top: 7px;
		border-radius: 6px;
		transition: all 0.9s ease;
		font-size: 13px;
	}
	.pm_r2_msg_each_each2:hover{
		background: lightgrey;
		color: white;
	}
	
	.pm_r2_msg_each_each3{
		float: left;
		height: 50px;
		line-height: 50px;
		width: 153px;
		color: lightgray;
		font-size: 14px;
		margin-left: 65px;
	}
		
</style>
