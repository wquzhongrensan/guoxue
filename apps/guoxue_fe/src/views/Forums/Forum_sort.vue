<template>
	<div class="fs_all">
		<div style="margin-bottom: 10px;margin-left: 21px;">
			<el-breadcrumb separator="/">
				<el-breadcrumb-item :to="{ path: '/Forum' }">论坛首页</el-breadcrumb-item>
				<el-breadcrumb-item :to="{ path: '/Forum/Forum_sort' }">总荣誉榜</el-breadcrumb-item>
			</el-breadcrumb>
		</div>
		<div class="fs_title_real">
			总荣誉榜
		</div>
		<div class="fs">
			<div class="fs_title">
				<div class="fs_title1">排名</div>
				<div class="fs_title2">用户</div>
				<div class="fs_title3">发帖数</div>
				<div class="fs_title3">总积分</div>
				<div class="fs_title4">热帖</div>
			</div>
			<div class="fs_msg">
				<div class="fs_msg_each" v-for="(item, i) in honor_data" :key="i">
					<div :class="{fs_msg1: i<=2, fs_msg1_other: i>2}">{{i+1}}</div>
					<div class="fs_msg2"><div class="fs_msg2_img"><img style="border-radius: 50%;" :src="item.img_link" width="25" height="25" alt=""></div><router-link to="/Forum/Forum_sort">{{item.username}}</router-link></div>
					<div class="fs_msg3">{{item.publish_post}}</div>
					<div class="fs_msg3">{{item.total_grade}}</div>
					<div class="fs_msg4" v-for="(item1, i1) in item.author_forum" :key="i1"><router-link :to="'/Forum/Forum_detail?id=' + item1.id">{{maxSlice(item1.title, 14)}}</router-link></div>
					<div class="fs_msg5">
						<div class="guanzhu" @click="follow_handle(item.id)">关注</div>
					</div>
				</div>
			</div>
		</div>
	</div>
</template>

<script>
	import {
		forum_honor_msgs,
		userfollow_msgs,
	} from '@/api/api';
	
	import {
		getCookie
	} from '@/utils/cookies';
	
	export default{
		name:'Forum_sort',
		data() {
			return {
				honor_data:''
			}
		},
		methods: {
			get_forum_honor_msgs() {
				forum_honor_msgs({
					
				}).then((response) => {
					this.honor_data = response.data;
					console.log(this.honor_data)
				})
				.catch(function (error) {
					console.log(error);
				});
			},
			follow_handle(user_id){
				userfollow_msgs({
					user: getCookie("username"),
					follow: user_id
				}).then((response) => {
					alert(response.data.content);
				})
				.catch(function (error) {
					console.log(error);
				});
			},
			maxSlice(content, max_length ){
				return content.length > max_length ? content.slice(0, max_length) + '...' : content;
			},
		},
		created(){
			this.get_forum_honor_msgs();
		}
		
	}
	
</script>

<style scoped="scoped">
	.fs_all{
		width: 800px;
		float: left;
		margin-left: 100px;
		text-align: center;
		font-family: 'Microsoft YaHei','SF Pro Display',Roboto,Noto,Arial,'PingFang SC',sans-serif!important;
	}
	.fs_title_real{
		font-size: 20px;
		width: 760px;
		float: left;
		height: auto;
		margin-left: 20px;
		height: 37px;
		line-height: 37px;
		/* border-radius: 8px; */
		text-align: center;
		background: white;
		font-family: "microsoft yahei";
	}
	.fs{
		float: left;
		width: 760px;
		margin-left: 20px;
	}
	.fs_title{
		float: left;
		width: 760px;
		height: 30px;
		background: lightgray;
		line-height: 30px;
		text-align: left;
	}
	.fs_title div{
		float: left;
		height: 30px;
		line-height: 30px;
		margin-left: 10px;
	}
	.fs_title1{
		width: 50px;
		margin-left: 30px !important;
	}
	.fs_title2{
		width: 144px;
		margin-left: 39px !important;
	}
	.fs_title3{
	    width: 77px !important;
		margin-left: 11px !important;
	}
	.fs_title4{
		width: 50px;
		margin-left: 37px !important;
	}
	.fs_msg{
		float: left;
		width: 760px;
		height: auto;
		background: white;
		text-align: left;
		padding-bottom: 50px;
	}
	.fs_msg_each{
		float: left;
		width: 730px;
		height: 40px;
		line-height: 40px;
		border-bottom: 1px dashed lightgray;
		margin-left: 20px;
		font-size: 13px;
		transition: all 0.8s ease;
	}
	.fs_msg_each:hover{
		/* background: aliceblue; */
		opacity: 0.7;
		/* border-radius: 8px; */
	}
	.fs_msg1, .fs_msg1_other, .fs_msg2, .fs_msg3, .fs_msg4{
		float: left;
		height: 40px;
		line-height: 40px;
		margin-left: 10px;
	}
	.fs_msg1{
		width: 25px !important;
		height: 25px !important;
		border-radius: 50%;
		color: white;
		background: gold;
		margin-top: 7px;
		text-align: center;
		line-height: 27px;
	}
	.fs_msg1_other{
		width: 25px !important;
		height: 25px !important;
		border-radius: 50%;
		/* color: white; */
		/* background: gold; */
		margin-top: 7px;
		text-align: center;
		line-height: 27px;
	}
	.fs_msg2{
		text-indent: 20px;
		margin-left: 18px;
		width: 200px;
		color: #DED8D8;
	}
	.fs_msg2_img{
		width: 25px;
		height: 25px;
		float: left;
		margin-top: 10px;
		margin-top: 6px;
		margin-right: 5px;
	}
	.fs_msg3{
		width: 80px;
	}
	.fs_msg4{
		margin-left: 6px;
		width: 210px;
	}
	.fs_msg5{
		width: 66px;
		text-align: center;
		position: relative;
	}
	.fs_msg5 .guanzhu{
		position: absolute;
		border: 1px solid lightblue;
		width: 60px;
		border: 1px solid lightblue;
		height: 30px;
		margin-top: 5px;
		left: 670px;
		top: -1px;
		color: white;
		line-height: 27px;
		background: blue;
	}
	.guanzhu:hover{
		cursor: pointer;
	}
	a:hover{
		color: #24BCED;
		text-decoration: none;
	}
</style>
