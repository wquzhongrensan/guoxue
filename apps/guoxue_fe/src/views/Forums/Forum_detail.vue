<template>
	<div>
		<div class="fd_nav">
			<el-breadcrumb separator="/">
				<el-breadcrumb-item :to="{ path: '/Forum' }">论坛首页</el-breadcrumb-item>
				<el-breadcrumb-item :to="{ path: '/Forum/Forum_list' }">板块详情</el-breadcrumb-item>
				<el-breadcrumb-item :to="{ path: '/Forum/Forum_detail' }">论坛详情</el-breadcrumb-item>
			</el-breadcrumb>
		</div>
		<div class="fd_bottom_all">
			<div class="fd_bottom_left">
				<div class="fd_bottom_left_top">
					题目：<span>{{forum_detail.title}}</span>  
				</div>
				<div class="fd_bottom_left_top1">
					<div class="fd_bottom_left_top1_left">
						<div class="fd_bottom_left_top1_left_top1">
							查看:{{forum_detail.browse_count}}  回复:{{forum_detail.reply_count}}
						</div>
					</div>
					<div class="fd_bottom_left_top1_right">
						<div class="fd_bottom_left_top1_right_top1">
							<div class="fd_bottom_left_top1_right_top11">
								<router-link  :to="{path:'/Forum/forum_detail?id='+this.$route.query.id+'#reply_place'}" >回复</router-link>
							</div>
							<div class="fd_bottom_left_top1_right_top12">
								<a href="javascript:void(0);" @click="user_fav_handle()">收藏</a>
							</div>
						</div>
					</div>
					<div class="fd_bottom_left_top1_left_top1_per">
						<div class="fd_bottom_left_top1_left_top1_per1">
							<div class="fd_bottom_left_top1_left_top1_per1_left">
								<div class="fd_bottom_left_top1_left_1">
									<div class="fd_bottom_left_top1_left_1_img">
										<img style="border-radius: 50%;" width="80" height="80" :src="forum_detail.author.img_link" :alt="forum_detail.author.username">
									</div>
									<div class="fd_bottom_left_top1_left_1_title">
										{{forum_detail.author.username}}  <br><span @click="follow_handle(forum_detail.author.username)" style="color: blue;font-size: 11px;cursor: pointer;margin-top: -13px;float: left;font-weight: 600;margin-left: 60px;">关注</span>
									</div>
								</div>
							</div>
							<div class="fd_bottom_left_top1_right ">
								<div class="fd_bottom_left_top1_right_1">
									<div class="fd_bottom_left_top1_left_top1_per_right">
										<div v-html="forum_detail.forum_content[0].content"></div>
										<div class="fd_left_adv">
											<div>
												这是一个充满<span>正</span>能量的广告位
											</div>
										</div>
									</div>
									<div class="fd_bottom_left_top1_left_top1_per_right">
										<div class="fd_bottom_left_top1_left_top1_per_right_bottom_msg">
											<div class="fd_bottom_left_top1_left_top1_per_right_bottom_msg_left">
												<div><a href="javascript:void(0);" @click="dianzan_handle()">点赞</a></div>
												<div><a href="javascript:void(0);" @click="user_fav_handle()">收藏</a></div>
												<div><router-link  :to="{path:'/Forum/forum_detail?id='+this.$route.query.id+'#reply_place'}" >回复</router-link></div>
											</div>
											<div class="fd_bottom_left_top1_left_top1_per_right_bottom_msg_right">
												<div>{{forum_detail.add_time.replace("T", " ").split(".")[0]}}</div>
											</div>
										</div>
									</div>
								</div>
							</div>
						</div>
						
						<div class="fd_bottom_left_top1_left_top1_per1" v-for="(item, i) in forum_reply_datas" :key="i">
							<div class="fd_bottom_left_top1_left_top1_per1_left">
								<div class="fd_bottom_left_top1_left_1">
									<div class="fd_bottom_left_top1_left_1_img">
										<img style="border-radius: 50%;" width="80" height="80" :src="reply_avatars[i]['img']" :alt="reply_avatar[i]['username']">
									</div>
									<div class="fd_bottom_left_top1_left_1_title">
										{{reply_avatar[i]["username"]}} <br><span @click="follow_handle(reply_avatar[i]['username'])" style="color: blue;font-size: 11px;cursor: pointer;margin-top: -13px;float: left;font-weight: 600;margin-left: 60px;">关注</span>
									</div>
								</div>
							</div>
							<div class="fd_bottom_left_top1_right ">
								<div class="fd_bottom_left_top1_right_1">
									<div class="fd_bottom_left_top1_left_top1_per_right">
										<div v-html="item.content"></div>
										<div class="fd_left_adv">
											<div>
												这是一个充满<span>正</span>能量的广告位
											</div>
										</div>
									</div>
									<div class="fd_bottom_left_top1_left_top1_per_right">
										<div class="fd_bottom_left_top1_left_top1_per_right_bottom_msg">
											<div class="fd_bottom_left_top1_left_top1_per_right_bottom_msg_right">
												<div>{{item.add_time.replace("T", " ").split(".")[0]}}</div>
											</div>
										</div>
									</div>
								</div>
							</div>
						</div>
						<div v-if="session_status">
							<div class="fp_article_2">
								<div @click="showedit" :class="{choose_status: editstatus}"><a href="javascript:;" id="reply_place">编辑</a></div>
								<div @click="getUEContent" :class="{choose_status: !editstatus}">预览</div>
								<div @click="gotop" style="float: right;height: 23px;width: 80px;border: 0px;margin-top: 4px;line-height: 23px;color: blue;cursor: pointer;">
									回到顶部
								</div>
							</div>
							<div class="fd_bottom_left_top1_left_fuwenben" v-show="editstatus">
								<UE :defaultMsg=defaultMsg :config=config ref="ue" style="margin-left: 0px;height: 100px;"></UE>
							</div>
							<div class="fd_bottom_left_top1_left_fuwenben"  style="border:1px solid lightgray; margin-bottom: 10px; height:277px !important;overflow:auto !important;" v-show="!editstatus" v-html="content"></div>
							<div class="fp_article_3">
								<div @click="reply" class="choose_status">回复</div>
							</div>
						</div>
						<div class="fp_article_4" v-if="!session_status">
							匿名用户不能进行回复，麻烦您先行<span @click="logins" style="cursor: pointer;color: red;font-weight: 600;font-size: 15px;">登录</span>
						</div>
						<div class="fd_bottom_left_top1_left_qita_title">
							相关推荐
						</div>
						<div class="fd_bottom_left_top1_left_qita">
							<div class="fd_bottom_left_top1_left_qita_each" v-for="(item, i) in forum_part_data2" :key="i">
								<div class="fd_bottom_left_top1_left_qita_each_title"><router-link :to="'/Forum/Forum_detail?id='+item.id">{{item.title}}</router-link></div>
								<div class="fd_bottom_left_top1_left_qita_each_msg">作者: {{item.author}}  &nbsp;&nbsp;创建时间： {{item.add_time.replace("T", " ").split(".")[0]}}&nbsp;&nbsp;浏览量： {{item.browse_count}}</div>
							</div>
						</div>
					</div>
				</div>
			</div>
			
			<div class="fd_bottom_right">
				<div class="f_msg_right_top1">
					<div class="f_msg_right_top1_top2">
						<div>热议榜</div>
						<span><router-link to="/Forum/Forum_sort">查看榜单</router-link></span>
					</div>
					
					<div class="f_msg_right_top2_bottom">
						<div :key="i" v-for="(item, i) in forum_hot" style="background: white;" class="f_msg_right_top2_bottom_each1">
							<span :class="{f_msg_right_top2_bottom_paiming: i<=2, f_msg_right_top2_bottom_paiming1: i>2}">{{i+1}}</span>
							<span class="f_msg_right_top2_bottom_name" style="cursor: pointer;" @click="goother(item.id)">{{maxSlice(item.title, 10)}}</span>
							<span style="color: lightgrey; font-size: 12px;" class="f_msg_right_top2_bottom_count">{{item.browse_count}}</span>
						</div>
					</div>
						
				</div>
				
				<div class="f_msg_right_top1"  style="height: 385px;">
					<div class="f_msg_right_top1_top2" >
						<div>推荐</div>
					</div>
					
					<div class="f_msg_right_top2_bottom" style="height: 400px !important;">
						<span class="f_msg_right_top2_bottom_each" v-for="(item, i) in forum_part_data1" :key="i">
							<div style="font-size: 14px; font-weight: 400;color: black;margin-top:10px;margin-bottom: 4px;"><router-link :to="'/Forum/Forum_detail?id='+item.id">{{maxSlice(item.title, 15)}}</router-link></div>
							<div>{{item.add_time.replace("T", " ").split(".")[0]}} &nbsp;&nbsp;浏览量:{{item.browse_count}}</div>
						</span>
						
					</div>
						
				</div>
						
			</div>
		</div>
		
	</div>
	
</template>

<script scoped>
	import UE from '@/components/UE';
	import {getCookie} from '@/utils/cookies';
	import {
		get_forum_msgs,
		reply_forums,
		userfav_msgs,
		userfollow_msgs,
		forum_detail_msgs,
		get_part_forum_forums
	} from '@/api/api';
	
	function scroll_to_top(){
		window.scrollTo(0,0);
	}
	export default{
		name: 'Forum_detail',
		components: {
			UE,
		},
		data() {
			return {
				// 判断用户是否登录的--  先假设用户已经登录
				session_status: true,
				dialogFormVisible_login: false,
				defaultMsg: '开始回复吧',
				config: {
					initialFrameWidth: 748,
					initialHeight:150,
					initialFrameHeight: 200,
					autoClearinitialContent: true,
				},
				content: '',
				editstatus: true,
				forum_detail: '',
				forum_reply_data: '',
				reply_avatar: [],
				forum_hot: [],
				forum_part_data1: '',
				forum_part_data2: '',
				img_link1: '',
				usernamess: ''
			}
		},
		methods: {
			showedit(){
				this.editstatus = true;
			},
			getUEContent() {
				this.editstatus = false;
				let content = this.$refs.ue.getUEContent();
				this.content = content;
			},
			logins(){
				this.$store.commit('changelLoginStatus', true)
			},
			getdata(){
				// 函数里面获取路由数据
				const id = this.$route.query.id;
				get_forum_msgs({
					id: id,
				}).then((response) => {
					this.forum_detail = response.data;
					this.forum_reply_data = this.forum_detail['forum_reply'];
					const _this = this;
					for(var i=0; i< this.forum_reply_data.length; i++){
						_this.img_link1 = _this.forum_reply_data[i]["author"]["img_link"];
						_this.usernamess = _this.forum_reply_data[i]["author"]["username"];
						_this.reply_avatar.push({img: _this.img_link1, username: _this.usernamess});
					}
					console.log(_this.reply_avatar)
				})
				.catch(function (error) {
					console.log(error);
				});
			},
			reply(){
				const _this = this;
				if(confirm("确认回复吗？")){
					reply_forums({
						topic: this.forum_detail.id + "",
						author: getCookie("username"),
						content: this.$refs.ue.getUEContent(),
					}).then((response) => {
						this.forum_reply_data.push(response.data);
						const _this = this;
						for(var i=0; i< this.forum_reply_data.length; i++){
							_this.img_link1 = _this.forum_reply_data[i]["author"]["img_link"];
							_this.usernamess = _this.forum_reply_data[i]["author"]["username"];
							_this.reply_avatar.push({img: _this.img_link1, username: _this.usernamess});
						};
						console.log(_this.reply_avatar)
						this.forum_detail.reply_count = this.forum_detail.reply_count + 1;
						scroll_to_top();
						this.$refs.ue.setUEContent('');
					})
					.catch(function (error) {
						console.log(error);
					});
				}
			},
			reply_msg(){
				// alert("hello")
				const height = this.$refs.reply_place.offsetHeight;
				console.log(this.$refs);
				console.log(height)
				window.scrollTo(0,1200);
			},
			goReply(selector) {
				
				 const anchor = this.$refs.reply_place;
				 alert(anchor);
				 document.body.scrollTop = this.$el.querySelector(selector).offsetTop
			},
			gotop(){
				this.$router.push({path:'/Forum/forum_detail?id='+this.$route.query.id})
				window.scrollTo(0,0);
			},
			user_fav_handle(){
				// 函数里面获取路由数据
				userfav_msgs({
					user: getCookie("username"),
					topic: this.$route.query.id
				}).then((response) => {
					console.log(response.data);
					alert(response.data.content);
				})
				.catch(function (error) {
					console.log(error);
				});
			},
			dianzan_handle(){
				alert("点赞成功");
			},
			follow_handle(user_name){
				userfollow_msgs({
					user: getCookie("username"),
					user_name: user_name
				}).then((response) => {
					alert(response.data.content);
				})
				.catch(function (error) {
					console.log(error);
				});
			},
			get_forum_hot(){
				// 获取帖子详情信息
				forum_detail_msgs({
					page_size: 6,
					ordering: '-browse_count',
				}).then((response) => {
					this.forum_hot = response.data.results;
					console.log(this.forum_hot);
				})
				.catch(function (error) {
					console.log(error);
				});
			},
			goother(id){
				this.$router.push({path: '/Forum/Forum_detail1?id='+id})
			},
			get_forum_part_data(page_size, type){
				get_part_forum_forums({
					page_size: page_size,
				}).then((response) => {
					if(type == 1){
						this.forum_part_data1 = response.data.results;
					}else{
						this.forum_part_data2 = response.data.results;						
					}
				})
				.catch(function (error) {
					console.log(error);
				});
			},
			// 控制景点多读字符串的长度
			maxSlice(content, max_length ){
				return content.length > max_length ? content.slice(0, max_length) + '...' : content;
			},
			
		},
		created(){
			this.getdata();
			scroll_to_top();
			this.get_forum_hot();
			this.get_forum_part_data(5, 1);
			this.get_forum_part_data(10, 2)
		},
		computed: {
			forum_reply_datas() {
				return this.forum_reply_data;
			},
			reply_avatars(){
				return this.reply_avatar;
			}
		},
	}
</script>

<style scoped="scoped">
	
	.fd_left_adv{
		width: 580px;
		height: 70px;
		display: inline-block;
		margin: 0px auto;
		text-align: center;
		line-height: 70px;
		border-top: 1px solid lightgray;
		border-bottom: 1px solid lightgray;
	}
	.fd_left_adv div{
		display: inline-block;
		font-size: 27px;
		color: dimgray;
		/* font-family: "microsoft sans serif"; */
		/* font-weight: 800; */
	}
	.fd_left_adv div span{
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
	.fd_nav{
		margin-top: 4px;
		margin-left: 4px;
		margin-bottom: 7px;
	}
	.fd_bottom_all{
		box-shadow: 0 0 1px 0 rgba(0,0,0,0.5) ;
		border-top:1px solid lightgray;
		width: 1000px;
		margin: 3px auto;
		color: #4D4D4D !important;
		text-align: left;
	}
	.fd_bottom_left{
		/* border-right:1px solid lightgray; */
		width: 750px;
		float: left;
		margin-top: 10px;
		/* height: 1000px; */
		border: 1px solid lightgray;
	}
	.fd_bottom_left_top{
		height: 40px;
		line-height: 40px;
		font-size: 18px;
		background: white;
		font-family: 'Microsoft YaHei','SF Pro Display',Roboto,Noto,Arial,'PingFang SC',sans-serif!important;
		border-bottom: 1px solid lightgray;
		text-indent: 20px;
		background: whitesmoke;
		font-weight: 600;
		box-shadow: 3px 3px 6px 1px rgba(0,0,0,0.2) ;
	}
	.fd_bottom_left_top span{
		text-shadow: 4px 0 9px rgba(86,170,255,0.9) ;
		color: palevioletred;
		transition: all 0.8s ease;
	}
	.fd_bottom_left_top span:hover{
		color: beige;
		font-size: 19px;
		font-style: italic;
		text-shadow: 0 0 9px rgba(40,40,40,1) ;
	}
	.fd_bottom_left_top1{
		width: 750px;
		height: 42px;
		line-height: 42px;
		margin-top: 8px;
	}
	
	.fd_bottom_left_top1_left{
		float: left;
		width: 150px;
		line-height: 42px;
	}
	.fd_bottom_left_top1_left_top1{
		width: 150px;
		height: 42px;
		text-indent: 20px;
		background: #FAFBFC;
		/* border: 1px solid lightgray; */
	}
	.fd_bottom_left_top1_left_1{
		/* border-top: 1px solid lightgray; */
		width: 150px;
		margin-top: 3px;
		background: #FAFBFC;
	}
	.fd_bottom_left_top1_left_1 .fd_bottom_left_top1_left_1_img{
		float: left;
		width: 150px;
		height: 110px;
		line-height: 200px;
		text-align: center;
	}
	.fd_bottom_left_top1_left_1 .fd_bottom_left_top1_left_1_title{
		float: left;
		width: 150px;
		height: 30px;
		line-height: 30px;
		text-align: center;
	}
		
	
	
	.fd_bottom_left_top1_right{
		float: right;
		width: 600px;
		height: auto;
		border-left: 1px dotted lightgray;
		line-height: 20px;
	}
	.fd_bottom_left_top1_right_top1{
		width: 600px;
		border-left: 1px solid lightgray;
		margin-left: -4px;
		height: 42px;
		line-height: 42px;
		background: white !important;

		/* border: 1px solid lightgray; */

	}
	.fd_bottom_left_top1_right_top1 div{
		float: right;
		width: 48px;
		height: 30px;
		line-height: 32px;
		margin-right: 10px;
		border-radius: 5px;
		margin-top: 5px;
		text-align: center;
		background: blue;
	}
	.fd_bottom_left_top1_right_top1 a{
		color: white;
	}
	.fd_bottom_left_top1_right_1{
		width: 600px;
		background: white;
		margin-top: 5px;
		padding-bottom: 15px;
		margin-bottom: 3px;
		padding-top: 10px;
	}
	.fd_bottom_right{
		width: 240px;
		float: right;
		margin-top: 10px;
		/* height: 1000px; */
		/* border: 1px solid gray; */
		font-family: "microsoft yahei" !important;
		font-size: 12px !important;
		font-weight: normal !important;
	}
	.fd_bottom_left_top1_left_top1_per{
		background: #F9FAFB;
		width: 750px;
		height: auto;
		/* border: 1px solid lightgray; */
	}
	.fd_bottom_left_top1_left_top1_per .fd_bottom_left_top1_left_top1_per1{
		width: 750px;
		/* height: 600px; */
		border: 1px solid lightgray;
		background: #F9FAFB;
		float: left;
		margin-left: -2px;

	}
	.fd_bottom_left_top1_left_top1_per1 .fd_bottom_left_top1_left_top1_per1_left{
		float: left;
		width: 147px;
		height: auto;
		border: 0px;
	}
	.fd_bottom_left_top1_right .fd_bottom_left_top1_left_top1_per_right{
		width: 580px;
		margin-left: 10px;
	    text-align: justify;
	}
	.fd_bottom_left_top1_left_top1_per_right .fd_bottom_left_top1_left_top1_per_right_bottom_msg{
		height: 38px;
		width: 580px;
		line-height: 38px;
		text-align: left;
	}
	.fd_bottom_left_top1_left_top1_per_right p{
		margin-bottom: 4px;
		font-size: 13px;
	}
	.fd_bottom_left_top1_left_top1_per_right img{
		display: inline-block;
		margin: 0 auto;
	}
	.fd_bottom_left_top1_left_top1_per_right_bottom_msg .fd_bottom_left_top1_left_top1_per_right_bottom_msg_left{
		float: left;
		
	}
	.fd_bottom_left_top1_left_top1_per_right_bottom_msg_left div{
		float: left;
		width: 50px;
		height: 32px;
		border-radius: 5px;
		line-height: 35px;
		/* height: 30px; */
		/* line-height: 32px; */
		margin-left: 6px;
		margin-top: 3px;
		text-align: center;
		background: blue;
	}
	
	.fd_bottom_left_top1_left_top1_per_right_bottom_msg_left a{
		color: white;
	}
	
	.fd_bottom_left_top1_left_top1_per_right_bottom_msg .fd_bottom_left_top1_left_top1_per_right_bottom_msg_right{
		float: right;
		
	}
	.fd_bottom_left_top1_left_top1_per_right_bottom_msg_right div{
		float: right;
		
	}
	.fd_bottom_left_top1_left_fuwenben{
		width: 748px;
		float: left;
		height: 277px;
		border-radius: 5px;
		line-height: 21px;
		margin-bottom: 10px;
		margin-top: 10px;
		background: white;
	}
	
	.f_msg_right_top1{
		width: 238px;
		height: 249px;
		overflow: hidden;
		border: 1px solid lightgray;
		border-radius: 5px;
		padding-bottom: 10px;
		margin-bottom: 15px;
	}
	.f_msg_right_top1 .f_msg_right_top1_top, .f_msg_right_top1 .f_msg_right_top1_top2{
		float: left;
		width: 238px;
		height: 37px;
		line-height: 37px;
		font-size: 19px;
		text-align: left;
		text-indent: 20px;
		box-shadow: 2px 2px 5px 0 rgba(138,185,226,0.7) inset;
	}
	.f_msg_right_top1 .f_msg_right_top1_top2 div{
		float: left;
		height: 50px;
		line-height: 41px;
		font-size: 17px;
	}
	.f_msg_right_top1 .f_msg_right_top1_top2 span{
		float: right;
		font-size: 14px;
		color: blue;
		margin-right: 10px;
		margin-top: 2px;
	}
	.f_msg_right_top1 div{
		float: left;
		width: 120px;
		height: 104px;
		line-height: 104px;
		font-size: 14px;
		/* font-weight: 600; */
	}
	.f_msg_right_top1_img{
		width: 150px;
	}
	.f_msg_right_top1_msg{
		margin-left: -31px;
	}
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
	.f_msg_right_top1 .f_msg_right_top1_top2{
		box-shadow: 4px 4px 8px 2px rgba(0,0,0,0.2) inset;
	}
	.f_msg_right_top2_bottom{
		overflow: hidden;
		width: 238px !important;
		height: 300px !important;
		border-top: 1px solid lightgray;
		border-right: 1px solid lightgray;
		
	}
	.f_msg_right_top2_bottom div{
		width: 238px;
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
	}
	.f_msg_right_top2_bottom .f_msg_right_top2_bottom_paiming1{
		float: left;
		width: 23px;
		line-height: 26px;
		height: 23px;
		/* background: orange; */
		color: lightgray;
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
	.f_msg_right_top2_bottom .f_msg_right_top2_bottom_each{
		height: 69px;
		float: left;
		border-bottom: 1px solid lightgray;
		background: white;
		transition: all 0.8s ease;
	}
	.f_msg_right_top2_bottom .f_msg_right_top2_bottom_each a:hover{
		color: orange;
	}
	.f_msg_right_top2_bottom .f_msg_right_top2_bottom_each:hover{
		background: whitesmoke;
		opacity: 0.9;
	}
	.f_msg_right_top2_bottom span div{
		float: left;
		width: 238px;
		margin-left: 10px;

		height: 19px;
		line-height: 24px;
		border-bottom: 0px;
		font-size: 12px;
		font-family: 'Microsoft YaHei','SF Pro Display',Roboto,Noto,Arial,'PingFang SC',sans-serif!important;
	}
	.fd_bottom_left_top1_left_qita_title{
		width: 748px;
		float: left;
		height: 30px;
		line-height: 30px;
		margin-top: 10px;
		background: white;
		text-indent: 20px;
		font-size: 20px;
		font-weight: 600;
		border-bottom: 1px solid lightgray;
	}
	.fd_bottom_left_top1_left_qita{
		width: 748px;
		float: left;
		/* height: 100px; */
		/* margin-top: 10px; */
		background: white;
	}
	.fd_bottom_left_top1_left_qita_each{
		height: 60px;
		float: left;
		width: 710px;
		margin-left: 19px;
		border-bottom: 1px solid lightgray;
		transition: all 0.8s ease;
	}
	.fd_bottom_left .fd_bottom_left_top1_left_qita_each:hover{
		background: whitesmoke;
		opacity: 0.9;
	}
	.fd_bottom_left_top1_left_qita_each .fd_bottom_left_top1_left_qita_each_title{
		float: left;
		width: 710px;
		height: 30px;
		line-height: 40px;
		font-size: 14px;
		color: black;
	}
	.fd_bottom_left_top1_left_qita_each .fd_bottom_left_top1_left_qita_each_title a{
		text-decoration: none;
	}
	.fd_bottom_left_top1_left_qita_each .fd_bottom_left_top1_left_qita_each_title a:hover{
		color: orange;
		text-decoration: none;
	}
	.fd_bottom_left_top1_left_qita_each .fd_bottom_left_top1_left_qita_each_msg{
		float: left;
		width: 710px;
		height: 30px;
		line-height: 27px;
	}
	.f_msg_right_top2_bottom .f_msg_right_top2_bottom_each1{
		transition: all 0.8s ease;
	}
	.f_msg_right_top2_bottom .f_msg_right_top2_bottom_each1:hover{
		box-shadow: 4px 4px 8px 2px rgba(0,0,0,0.2) !important;
		background:whitesmoke !important;
	}
	.fp_article_2{
		float: left;
		width: 747px;
		height: 30px;
		background: white;
		margin-top: 10px;
		margin-bottom: -10px;
		line-height: 30px;
	}
	.fp_article_2 div{
		float: left;
		cursor: pointer;
		width: 50px;
		height: 30px;
		text-align: center;
		font-size: 12px;
		border-top: 1px solid lightgray;
		border-right: 1px solid lightgray;
		border-left: 1px solid lightgray;
	}
	.fp_article_2 .choose_status{
		border-bottom: 2px solid darkgray !important;
	}
	.fp_article_3{
		float: left;
		width: 747px;
		height: 50px;
		background: white;
		margin-top: -10px;
		margin-bottom: 10px;
		line-height: 50px;
	}
	.fp_article_3 div{
		float: left;
		cursor: pointer;
		width: 68px;
		height: 40px;
		text-align: center;
		font-size: 12px;
		border-top: 1px solid lightgray;
		border-right: 1px solid lightgray;
		border-left: 1px solid lightgray;
		background: blue;
		color: white;
		font-size: 15px;
		line-height: 40px;
		margin-left: 20px;
	}
	.fp_article_3 .choose_status{
		border-bottom: 2px solid darkgray !important;
	}
	.fp_article_4{
		float: left;
		width: 747px;
		height: 40px;
		background: white;
		margin-top: 10px;
		line-height: 40px;
		text-align: center;
	}
</style>
