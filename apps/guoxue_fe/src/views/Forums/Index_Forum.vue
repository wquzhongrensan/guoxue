<template>
	<div>
		<div class="f_msg">
			<div class="f_msg_left">
				<div class="f_msg_left_center_top" style="text-shadow: 2px 2px 2px rgba(0,0,0,0.5) ;">
					论坛精选
				</div>
				<div class="f_msg_left_top_msg">
					<div class="f_msg_left_top_msg_left">
						<Silde_Car_Forum></Silde_Car_Forum>
					</div>
					<forum_top></forum_top>
				</div>
				<div class="f_msg_left_center">
					<div class="f_msg_left_center_top" style="text-shadow: 2px 2px 2px rgba(0,0,0,0.5) ;">
						正在热议
					</div>
					<div class="f_msg_left_center_title" style="margin-top: -1px;border-radius:5px;border:1px solid lightgray;">
						<div class="f_msg_left_center_title_1">标题</div>
						<div>回复数</div>
						<div>人气</div>
						<div>提问人</div>
					</div>
					<div class="f_msg_left_center_msg" style="background: white;border:1px solid lightgray;margin-top:-2px">
						<div class="f_msg_left_center_msg_each" v-for="(item, i) in forum_detail_msg1" :key="i">
							<div class="f_msg_left_center_msg_1">
								<span ><a href="/Forum/Forum_list" style="color: indianred;">{{item.forum_type.title}}</a></span>
								<span style="font-weight: 0; font-size: 15px;"><router-link :to="'/Forum/Forum_detail?id=' + item.id" class="f_msg_left_center_msg_each_msg_link">{{item.title}}</router-link></span>
							</div>
							<div>{{item.reply_count}}</div>
							<div>{{item.browse_count}}</div>
							<div><a href="javascript:;">{{item.author.username}}</a></div>
						</div>
					</div>
				</div>
				<div class="f_msg_left_adv" style="margin-top: 10px;margin-bottom: 10px;">
					<div>
						这有一个充满<span>正</span>能量的广告位
					</div>
				</div>
				
				<div class="f_msg_left_bottom">
					<div class="f_msg_left_bottom_top" style="text-shadow: 2px 2px 2px rgba(0,0,0,0.5) ;">
						主要论坛分类
					</div>
					<div class="f_msg_left_bottom_bottom" style="background: white">
						<div :class="{f_msg_left_bottom_bottom_each: i<4, f_msg_left_bottom_bottom_each111: i>=4}" v-for="(item, i) in forum_type" :key="i">
							<strong class="f_msg_left_bottom_bottom_each_strong">{{item.title}}</strong>
							<div v-for="(item1, i1) in item['sub_forum']" :key="i1">{{item1.title}}</div>
						</div>
					</div>
				</div>
			</div>
			<div class="f_msg_right">
				<div class="f_msg_right_top1" style="background: white;">
					<div class="f_msg_right_top1_top" style="background: #F5F5F5;">
						个人信息
					</div>
					<div class="f_msg_right_top1_img">
						<img style="border-radius: 50%;margin-top:10px" width="80" height="80" src="../../static/img/经典导读/daodu_作者头像.gif" alt="">
					</div>
					<div class="f_msg_right_top1_msg">
						{{person_msg.username}}
					</div>
					<div class="f_msg_right_top1_bottom">
						<div class="">
							<span class="f_msg_right_top1_bottom1">
								总积分
							</span>
							<span class="f_msg_right_top1_bottom2">
								{{person_msg.total_grade}}
							</span>
						</div>
						<div class="">
							<span class="f_msg_right_top1_bottom1">
								发帖量
							</span>
							<span class="f_msg_right_top1_bottom2">
								{{person_msg.publish_post}}
							</span>
						</div>
						<div class="">
							<span class="f_msg_right_top1_bottom1">
								回帖量
							</span>
							<span class="f_msg_right_top1_bottom2">
								{{person_msg.publish_reply}}
							</span>
						</div>
						<div class="">
							<span class="f_msg_right_top1_bottom1">
								当前排名
							</span>
							<span class="f_msg_right_top1_bottom2">
								{{person_msg.current_sort ? person_msg.current_sort : 0}}
							</span>
						</div>
						<div class="">
							<span class="f_msg_right_top1_bottom1">
								粉丝数
							</span>
							<span class="f_msg_right_top1_bottom2">
								{{person_msg.fans}}
							</span>
						</div>
						<div class="">
							<span class="f_msg_right_top1_bottom1">
								关注数
							</span>
							<span class="f_msg_right_top1_bottom2">
								{{person_msg.attention >0 ? person_msg.attention : 0}}
							</span>
						</div>
					</div>
				</div>
				
				<div class="f_msg_right_top1" style="background: white;">
					<div class="f_msg_right_top1_top2" style="background: #F5F5F5;">
						荣誉榜
					</div>
					<div class="f_msg_right_top2_bottom">
						<div v-for="(item, i) in forum_honor_data.slice(0,6)" :key="i">
							<span :class="{f_msg_right_top2_bottom_paiming: i<=2, f_msg_right_top2_bottom_paiming1: i>2}">{{i+1}}</span>
							<span style="font-family: 'microsoft sans serif';font-weight: 10;font-size: 15px;" class="f_msg_right_top2_bottom_name">{{item.username}}</span>
							<span style="color: lightgrey; font-size: 12px;" class="f_msg_right_top2_bottom_count">{{item.total_grade}}</span>
						</div>
					</div>
				</div>
			</div>
		</div>
	</div>
</template>

<script>
	import Silde_Car_Forum from '@/components/Slide_Car_Forum'
	import forum_top from '@/components/Forums/forum_top.vue'
	import {
		person_info,
		forum_type_msgs,
		forum_honor_msgs,
		forum_detail_msgs,
	} from '@/api/api';
	import {getCookie} from '@/utils/cookies'
	
	function scroll_to_top(){
		window.scrollTo(0,0);
	}
	
	export default{
		name: 'Index_Forum',
		data(){
			return {
				person_msg: {
					"attention": 0,
					"fans": 0,
					"total_grade": 0,
					"current_sort": null,
					"publish_post": 0,
					"publish_reply": 0,
				},
				forum_type: '',
				forum_detail_msg1: '',
				forum_detail_msg2: '',
				forum_honor_data :'',
				reyi_data: [
					{
						type: '经史子集',
						type_link: '',
						msg: '一阴一阳之为道？',
						msg_link: '',
						author: 'laoliang',
						author_link: '',
						visit_count: '32432',
						answer_count: '545345',
					},
					{
						type: '经史子集',
						type_link: '',
						msg: '一阴一阳之为道？',
						msg_link: '',
						author: 'laoliang',
						author_link: '',
						visit_count: '32432',
						answer_count: '545345',
					},
					{
						type: '经史子集',
						type_link: '',
						msg: '一阴一阳之为道？',
						msg_link: '',
						author: 'laoliang',
						author_link: '',
						visit_count: '32432',
						answer_count: '545345',
					},
					{
						type: '经史子集',
						type_link: '',
						msg: '一阴一阳之为道？',
						msg_link: '',
						author: 'laoliang',
						author_link: '',
						visit_count: '32432',
						answer_count: '545345',
					},
					{
						type: '经史子集',
						type_link: '',
						msg: '一阴一阳之为道？',
						msg_link: '',
						author: 'laoliang',
						author_link: '',
						visit_count: '32432',
						answer_count: '545345',
					},
					{
						type: '经史子集',
						type_link: '',
						msg: '一阴一阳之为道？',
						msg_link: '',
						author: 'laoliang',
						author_link: '',
						visit_count: '32432',
						answer_count: '545345',
					},
					{
						type: '经史子集',
						type_link: '',
						msg: '一阴一阳之为道？',
						msg_link: '',
						author: 'laoliang',
						author_link: '',
						visit_count: '32432',
						answer_count: '545345',
					},
				]
			}
		},
		components:{
			Silde_Car_Forum,
			forum_top,
		},
		methods: {
			get_info() {
				// 获取帖子详情信息
				forum_detail_msgs({
					page_size: 7,
					ordering: '-browse_count',
				}).then((response) => {
					this.forum_detail_msg1 = response.data.results;
					console.log(this.forum_detail_msg1);
				})
				.catch(function (error) {
					console.log(error);
				});
				// 获取个人信息
				person_info({
					username: getCookie("username"),
				}).then((response) => {
					this.person_msg = response.data[0];
				})
				.catch(function (error) {
					console.log(error);
				});
				// 获取论坛版块分类信息
				forum_type_msgs({
				}).then((response) => {
					this.forum_type = response.data;
				})
				.catch(function (error) {
					console.log(error);
				});
				
				// 获取荣誉榜信息
				forum_honor_msgs({
				}).then((response) => {
					this.forum_honor_data = response.data;
				})
				.catch(function (error) {
					console.log(error);
				});
			},
			
		},
		created(){
			this.get_info();
			scroll_to_top();
		}
	}
</script>

<style scoped="scoped">
	.f_nav{
		float: left;
		margin-top: 3px;
		margin-bottom: 7px;
		line-height: 30px;
	}
	.f_top_img{
		width: 1000px;
		height: 120px;
	}
	.f_top_img div{
		float: left;
		line-height: 25px;
		margin-left: 312px !important;
	}
	.f_msg{
		float: left;
		width: 1000px;
		/* border: 1px solid gray; */
		height: 1000px;
		margin-top: 10px;
	}
	.f_msg_left{
		float: left;
		width: 730px;
		/* border: 1px solid gray; */
		height: 1000px;
	}
	
	/* h_top_adv1 */
	.f_msg_left_adv{
		width: 730px;
		height: 70px;
		display: inline-block;
		margin: 0px auto;
		text-align: center;
		line-height: 70px;
		border-top: 1px solid lightgray;
		border-bottom: 1px solid lightgray;
	}
	.f_msg_left_adv div{
		display: inline-block;
		font-size: 27px;
		color: dimgray;
		font-family: "microsoft sans serif";
		font-weight: 800;
	}
	.f_msg_left_adv div span{
		display: inline-block;
		width: 40px;
		color: white;
		height:40px;
		border-radius: 21px;
		background: red;
		line-height: 39px;
		margin-left:3px;
		margin-right: 3px;
	}
	.f_msg_left_top{
		box-sizing: content-box;
		padding: -16px;
		border: none;
		font: normal 13px/1 Verdana, Geneva, sans-serif;
		color: black;
		text-overflow: ellipsis;
		box-shadow: 0 0 2px 1px rgba(0,0,0,0.5) inset;
		transition: all 200ms cubic-bezier(0.6, -0.28, 0.735, 0.04) 10ms;
		height: 10px;
		width: 730px;
		background: #E7E9EB;
		display: inline-block;
	}
	.f_msg_left_top_msg{
		margin-bottom: 10px;
		width: 730px;
		height: 330px;
		/* border: 1px solid lightgray; */
	}
	.f_msg_left_top_msg_left{
		margin-top: 7px;
		margin-left: 6px;
		width: 370px;
		height: 300px;
		float: left;
	}
	.f_msg_left_top_msg_right{
		width: 346px;
		height: 313px;
		float: right;
		/* border: 1px solid gray; */
	}
	.f_msg_left_top_msg_right_top{
		height: 33px;
		width: 336px;
		border-bottom: 2px solid lightgray;
	}
	.f_msg_left_top_msg_right_top div{
		float: left;
		height: 33px;
		line-height: 35px;
		font-size: 17px;
		font-weight: 600;
		width: 80px;
		margin-right: 10px;
	}
	.f_msg_left_top_msg_right_top div:hover{
		border-bottom: 2px solid red;
	}
	.f_msg_left_top_msg_right_top div a:hover{
		text-decoration: none;
	}
	.f_msg_left_top_msg_right_bottom_msg{
		width: 339px;
		margin-top: 10px;
		height: 270px;
		/* border: 1px solid gray; */
	}
	.f_msg_left .f_msg_left_center{
		/* margin-top: 10px; */
		width: 730px;
		height: 317px;
		border-radius: 10px;
		/* border: 1px solid gray !important; */
	}
	.f_msg_left_center div{
		float: left;
		width: 727px;
	}
	.f_msg_left_center_top{
		box-shadow: 3px 3px 6px 1px rgba(0,0,0,0.2) inset;
		height: 40px;
		background: #E3E6E8;
		border-radius: 10px;
		text-align: left;
		text-indent: 10px;
		line-height: 40px;
		font-size: 18px;
		font-family:  华文行楷, 'Lucida Grande', Verdana, Arial, Sans-Serif;
	}
	.f_msg_left_center_title{
		height: 30px;
		text-align: left;
		text-indent: 10px;
		line-height: 30px;
		font-size: 14px;
		background: #F0F0F0;
		border-right: 1px solid lightgray;
		border-left: 1px solid lightgray;
		/* border-radius: 10px; */
		font-family:  宋体, 'Lucida Grande', Verdana, Arial, Sans-Serif;
	}
	.f_msg_left_center_msg{
		height: 246px;
		background: #F5F5F5;
		border-left: 1px solid lightgray;
		border-right: 1px solid lightgray;
		border-bottom: 1px solid lightgray;

	}
	.f_msg_left_center_title div{
		float: right;
		width: 83px;
	}
	.f_msg_left_center_title .f_msg_left_center_title_1{
		float: left;
		width: 200px;
	}
	.f_msg_left_center_msg_each{
		width: 727px;
		height: 35px;
		border-bottom: 1px solid lightgray;
		float: left;
		line-height: 35px;
	}
	.f_msg_left_center_msg_each:hover{
		box-shadow: 4px 4px 8px 2px rgba(0,0,0,0.2) ;
		background:#FBFBFB;
	}
	
	.f_msg_left_center_msg_each div{
		float: right;
		font-size: 14px;
		width: 90px;
		margin-right: 4px;
	}
	.f_msg_left_center_msg_each .f_msg_left_center_msg_1{
		float: left;
		width: 417px;
		text-align: left;
		margin-left: 8px;
	}
	.f_msg_left_center_msg_each_msg_link{
		padding-left: 10px;
	}
	.f_msg_left_center_msg_each_msg_link:hover{
		color: indianred;
		text-decoration: none;
		
	}
	.f_msg_left .f_msg_left_bottom{
		/* margin-top: 10px; */
		width: 730px;
		/* height: 317px; */
		border-radius: 10px;
		/* border: 1px solid gray !important; */
	}
	.f_msg_left_bottom div{
		float: left;
		width: 727px;
		padding-left: 9px;
	}
	.f_msg_left_bottom_top{
		box-shadow: 1px 1px 4px 0 rgba(0,0,0,0.2) inset;
		/* text-shadow: 0 0 9px rgba(20,133,255,0.7) ; */
		height: 40px;
		background: #E3E6E8;
		border-radius: 10px;
		text-align: left;
		text-indent: 10px;
		line-height: 40px;
		font-size: 18px;
		font-family:  华文行楷, 'Lucida Grande', Verdana, Arial, Sans-Serif;
	}
	.f_msg_left_bottom_bottom{
		width: 727px;
		padding-bottom: 10px;
		border-radius: 10px;
	}
	.f_msg_left_bottom_bottom .f_msg_left_bottom_bottom_each{
		width: 200px;
		height: 95px;
		border-bottom: 1px solid gray;
		float: left;
		margin: 15px;
		padding-bottom: 5px;
		transition: all 0.8s ease;
	}
	.f_msg_left_bottom_bottom .f_msg_left_bottom_bottom_each111{
		width: 200px;
		height: 95px;
		/* border-bottom: 1px solid gray; */
		float: left;
		margin: 15px;
		padding-bottom: 5px;
		transition: all 0.8s ease;
	}
	.f_msg_left_bottom_bottom .f_msg_left_bottom_bottom_each:hover{
		box-shadow: 4px 4px 8px 2px rgba(0,0,0,0.2) ;
		background:#FBFBFB;
		opacity: 0.9;
	}
	.f_msg_left_bottom_bottom_each_strong{
		float: left;
		width: 150px;
		height: 21px;
		text-align: left;
		margin-top: 5px;
		margin-bottom: 5px;
		font-size: 16px;
		color: gray;
	}
	.f_msg_left_bottom_bottom_each div{
		float: left;
		width: 87px;
		height: 27px;
		line-height: 29px;
	}
	.f_msg_right{
		float: right;
		width: 260px;
	}
	.f_msg_right_top1{
		width: 260px;
		height: 246px;
		border-radius: 8px;height: 249px;
		overflow: hidden;
		padding-bottom: 10px;
		margin-bottom: 15px;
	}
	.f_msg_right_top1 .f_msg_right_top1_top, .f_msg_right_top1 .f_msg_right_top1_top2{
		float: left;
		width: 260px;
		height: 37px;
		line-height: 37px;
		font-size: 19px;
		text-align: center;
		box-shadow: 2px 2px 5px 0 rgba(138,185,226,0.7) inset;
	}
	.f_msg_right_top1 div{
		float: left;
		width: 120px;
		height: 104px;
		line-height: 104px;
		font-size: 16px;
		font-weight: 600;
	}
	.f_msg_right_top1_img{
		width: 150px;
	}
	/* .f_msg_right_top1_msg{
		margin-left: -31px;
	} */
	.f_msg_right_top1 .f_msg_right_top1_bottom{
		width: 247px !important;
		float: left;
		margin-left: 5px;
		/* height: ; */
		border-top: 1px solid lightgrey;
	}
	.f_msg_right_top1 .f_msg_right_top1_bottom div{
		float: left;
		width: 70px;
		line-height: 49px;
		height: 49px;
		margin-top: 2px;
		margin-right: 2px;
		margin-left: 10px;
		/* border: 1px solid gray; */
	}
	.f_msg_right_top1_bottom1{
		float: left;
		height: 24px;
		width: 77px;
		line-height: 30px;
		text-align: left;
		color: #999999;
		font-size: 13px;
		font-family: "microsoft yahei";
	}
	.f_msg_right_top1_bottom2{
		float: left;
		height: 20px;
		width: 77px;
		line-height: 24px;
		font-size: 11px;
		color: #FFC552;
		text-align: left;
		font-family: "microsoft yahei";
	}
	.f_msg_right_top2_bottom{
		overflow: hidden;
		width: 260px !important;
		height: 300px !important;
	}
	.f_msg_right_top2_bottom div{
		width: 260px;
		height: 35px;
		float: left;
		line-height: 35px;
		border-bottom: 1px dotted lightgray;
		text-align: left;
		margin-right: 10px;
	}
	.f_msg_right_top2_bottom .f_msg_right_top2_bottom_paiming{
		float: left;
		width: 23px;
		line-height: 26px;
		height: 23px;
		background: orange;
		color: white;
		margin-top: 6px;
		margin-left: 7px;
		text-align: center;
		border-radius: 5px;
	}
	.f_msg_right_top2_bottom .f_msg_right_top2_bottom_paiming1{
		float: left;
		width: 23px;
		line-height: 26px;
		height: 23px;
		/* background: orange; */
		color: gray;
		margin-top: 6px;
		margin-left: 7px;
		text-align: center;
	}
	.f_msg_right_top2_bottom .f_msg_right_top2_bottom_count{
		float: right;
		text-align: center;
		margin-right: 10px;
	}
	.f_msg_right_top2_bottom .f_msg_right_top2_bottom_name{
		margin-left: 12px;
	}
	.f_msg_right_top2_bottom .f_msg_right_top2_bottom_name:hover{
		cursor: pointer;
		color: orange;
	}
</style>
