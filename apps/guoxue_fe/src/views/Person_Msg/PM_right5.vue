<template>
	<div class="pm_r5">
		<div class="pm_r5_title"><div>我的论坛</div></div>
		<div class="pm_r5_msg">
			<div class="pm_r5_msg_top">
				<div class="pm_r5_msg_top_title">
					<div>战绩详情</div>
				</div>
				<div class="pm_r5_msg_bottom">
					<div class="pm_r5_msg_bottom_title">
						<div class="pm_r5_msg_bottom_title1">
							总积分
						</div>
						<div class="pm_r5_msg_bottom_title1">
							当前排名
						</div>
						<div class="pm_r5_msg_bottom_title1">
							发帖数
						</div>
						<div class="pm_r5_msg_bottom_title1">
							回帖数
						</div>
						<div class="pm_r5_msg_bottom_title1">
							关注数
						</div>
						<div class="pm_r5_msg_bottom_title1">
							粉丝数
						</div>
					</div>
					<div class="pm_r5_msg_bottom_msg">
						<div class="pm_r5_msg_bottom_msg1">{{person_msgss.total_grade}}</div>
						<div class="pm_r5_msg_bottom_msg1">{{person_msgss.current_sort}}</div>
						<div class="pm_r5_msg_bottom_msg1">{{person_msgss.publish_post}}</div>
						<div class="pm_r5_msg_bottom_msg1">{{person_msgss.publish_reply}}</div>
						<div class="pm_r5_msg_bottom_msg1">{{person_msgss.attention}}</div>
						<div class="pm_r5_msg_bottom_msg1">{{person_msgss.fans}}</div>
					</div>
				</div>
				<div class="pm_r5_msg_bottom2">
					<div class="pm_r5_msg_bottom2_title">
						<router-link to="/Person_Msg/PM_right5/PM_right5_1?t=5"><div @click="pm5_choose_status1_change" :class="['pm_r5_msg_bottom2_title_each', {'pm_r5_msg_bottom2_title_each_choose': pm5_choose_status1}]">已发帖</div></router-link>
						<router-link to="/Person_Msg/PM_right5/PM_right5_2?t=5"><div @click="pm5_choose_status2_change" :class="['pm_r5_msg_bottom2_title_each', {'pm_r5_msg_bottom2_title_each_choose': pm5_choose_status2}]">已回帖</div></router-link>
						<router-link to="/Person_Msg/PM_right5/PM_right5_3?t=5"><div @click="pm5_choose_status3_change" :class="['pm_r5_msg_bottom2_title_each', {'pm_r5_msg_bottom2_title_each_choose': pm5_choose_status3}]">hot帖</div></router-link>
					</div>
					<div class="pm_r5_msg_bottom2_msg">
						<router-view></router-view>
					</div>
				</div>
			</div>
		</div>
	</div>
</template>

<script>
	import {person_info, forum_detail_msgs} from '@/api/api';
	import {getCookie} from '@/utils/cookies';
	export default{
		name:'PM_right5',
		data(){
			return {
				pm5_choose_status1: true,
				pm5_choose_status2: false,
				pm5_choose_status3: false,
				person_msgss: '',
				p: 1,
				page_size: 7,
				page_range: [],
				ordering: '-id',
				forums_data_list: [],
			}
		},
		methods: {
			pm5_choose_status1_change() {
				if(!this.pm5_choose_status1){
					this.pm5_choose_status1 = true;
					this.pm5_choose_status2 = false;
					this.pm5_choose_status3 = false;
				}
			},
			pm5_choose_status2_change() {
				if(!this.pm5_choose_status2){
					this.pm5_choose_status1 = false;
					this.pm5_choose_status2 = true;
					this.pm5_choose_status3 = false;
				}
			},
			pm5_choose_status3_change() {
				if(!this.pm5_choose_status3){
					this.pm5_choose_status1 = false;
					this.pm5_choose_status2 = false;
					this.pm5_choose_status3 = true;
				}
			},
			get_info(){
				// 获取个人信息
				person_info({
					username: getCookie("username"),
				}).then((response) => {
					this.person_msgss = response.data[0];
				})
				.catch(function (error) {
					console.log(error);
				});
			},
			
		},
		created(){
			this.get_info();
			const route_params = this.$route.path.split("/")[3];
			if(route_params == "PM_right5_1"){
				this.pm5_choose_status1 = true;
				this.pm5_choose_status2 = false;
				this.pm5_choose_status3 = false;
			}else if(route_params == "PM_right5_2"){
				this.pm5_choose_status1 = false;
				this.pm5_choose_status2 = true;
				this.pm5_choose_status3 = false;
			}else if(route_params == "PM_right5_3"){
				this.pm5_choose_status1 = false;
				this.pm5_choose_status2 = false;
				this.pm5_choose_status3 = true;
			}
		}
	}
</script>

<style scoped="scoped">
	.pm_r5{
		float: left;
		width: 770;
		margin-left: 30px;
		margin-top: 20px;
		/* border: 1px solid lightgray; */
		font-family: "microsoft yahei";
		text-align: left;
	}
	.pm_r5_title{
		float: left;
		width: 726px;
		height: 73px;
		font-size: 25px;
		font-weight: 600;
		font-family: "microsoft yahei";
		line-height: 65px;
	}
	.pm_r5_title div{
		float: left;
		height: 73px;
		line-height: 73px;
		width: 726px;
		border-bottom: 1px solid lightgray;
	}
	.pm_r5_msg{
		float: left;
		width:726px;
		height: 500px;
		margin-top: 10px;
		/* border: 1px solid lightgray; */
	}
	.pm_r5_msg_top{
		float: inherit;
		width: 726px;
		height: 250px;
		line-height: 250px;
	}
	.pm_r5_msg_top_title{
		float: inherit;
		width: 726px;
		height: 50px;
		line-height: 50px;
		font-size: 15px;
		text-align: center;
		opacity: 0.55;
		border-bottom: 1px solid lightgray;
	}
	.pm_r5_msg_top_title div{
		float: left;
		width: 100px;
		opacity: 0.9;
		height: 50px;
		font-weight: 600;
		color: white;
		background: #A2A59F;
		border-top: 1px solid lightgray;
		border-right: 1px solid lightgray;
		border-left: 1px solid lightgray;
		font-family: "microsoft yahei";
		font-size: 15px;
	}
	.pm_r5_msg_top_title div:hover{
		opacity: 0.6;
	}
	.pm_r5_msg_bottom{
		float: inherit;
		width: 726px;
		height: 116px;
		border-radius: 3px;
		border-right: 1px solid lightgray;
		border-left: 1px solid lightgray;
		border-bottom: 1px solid lightgray;
	}
	.pm_r5_msg_bottom_title{
		float: left;
		height: 40px;
		line-height: 40px;
		margin-left: 20px;
		border-top: 1px solid lightgray;
		border-bottom: 1px solid lightgray;
		margin-left: 60px;
		margin-top: 15px;
		font-size: 14px;
		font-weight: 600;
	}
	.pm_r5_msg_bottom_title div{
		float: left;
		width: 100px;
		height: 40px;
		line-height: 40px;
		text-align: center;
	}
	.pm_r5_msg_bottom_msg{
		float: left;
		height: 40px;
		line-height: 40px;
		margin-left: 20px;
		border-bottom: 1px solid lightgray;
		margin-left: 60px;
		transition: all 0.8s ease;
	}
	.pm_r5_msg_bottom_msg:hover{
		background: #D8DEE0;
		opacity: 0.7;
	}
	.pm_r5_msg_bottom_msg div{
		float: left;
		width: 100px;
		height: 40px;
		line-height: 40px;
		text-align: center;
	}
	.pm_r5_msg_bottom2{
		float: inherit;
		width: 726px;
		height: 511px;
		margin-top: 10px;
		border-radius: 3px;
		overflow: hidden;
		/* border: 1px solid lightgray; */
	}
	.pm_r5_msg_bottom2_title{
		float: left;
		width: 726px;
		height: 49px;
		line-height: 50px;
		/* border-bottom: 1px solid lightgray; */
	}
	.pm_r5_msg_bottom2_title_each{
		float: left;
		width: 100px;
		height: 50px;
		line-height: 50px;
		text-align: center;
		font-size: 14px;
		font-size: 15px;
		border-right: 1px solid lightgray;
		border-top: 1px solid lightgray;
		border-left: 1px solid lightgray;
		border-bottom: 1px solid white;
	}
	.pm_r5_msg_bottom2_title_each:hover{
		border-bottom: 2px solid darkgray;
		opacity: 0.6;
	}
	.pm_r5_msg_bottom2_title_each_choose{
		background: #A2A59F;
		color: white;
		cursor: pointer;
		opacity: 0.55;
		font-weight: 600;
	}
	.pm_r5_msg_bottom2_msg{
		
		float: left;
		width: 726px;
		height: 460px;
		overflow: hidden;
		border: 1px solid lightgray;
	}
</style>
