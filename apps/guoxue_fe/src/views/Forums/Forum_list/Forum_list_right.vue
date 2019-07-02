<template>
	<div class="flr_all">
		<div class="flr_top">
			<div class="flr_top_title">
				{{fl_titles}}
			</div>
			<div class="flr_top_msg">
				主要讨论有关最近发生的有关{{fl_titles}}的内容.
			</div>
		</div>
		<div class="flr_bottom">
			<div class="flr_bottom_top">
				<router-link to="/Forum/Forum_publish"><div class="flr_bottom_top_left_button">发帖</div></router-link>
				<div class="flr_bottom_top_right_page">
					<div class="flr_bottom_top_right_page_count">共{{Math.ceil(page_count/page_size)}}页</div>
					<div v-if="previous" @click="get_previous_page()" :class="['flr_bottom_top_right_page_tiao', {flr_choose: previous}]">上一页</div>
					<div v-else class="flr_bottom_top_right_page_tiao">上一页</div>
					<div @click="get_page(i+1, ordering)" :class="['flr_bottom_top_right_page_num', {flr_bottom_top_right_page_num_choose: i+1==p}]" v-for="(item, i) in page_range" :key="i">{{i+1}}</div>
					<div v-if="next" class="flr_bottom_top_right_page_tiao flr_choose" @click="get_next_page()">下一页</div>
					<div v-else class="flr_bottom_top_right_page_tiao">下一页</div>
				</div>
			</div>
			<div class="flr_bottom_title">
				<div @click="change_current_forums_data_list('jinghua')" :class="{flr_choose_status: current_choose==1}">推荐精华</div>
				<div @click="change_current_forums_data_list('last')" :class="{flr_choose_status: current_choose==2}">最新</div>
				<div @click="change_current_forums_data_list('hot')" :class="{flr_choose_status: current_choose==3}">最热</div>
			</div>
			<div class="flr_bottom_title_desc">
				<div class="flr_bottom_title_desc_left">板块主题</div>
				<div class="flr_bottom_title_desc_right">
					<div class="flr_bottom_title_desc_right1">作者</div>
					<div class="flr_bottom_title_desc_right2">回复/查看</div>
					<div class="flr_bottom_title_desc_right3">最后发表</div>
				</div>
			</div>
			<div class="flr_bottom_msg">
				<div class="flr_bottom_msg_each" v-for="(item, i) in forums_data_list" :key="i">
					<div class="flr_bottom_msg_each_left">
						<div class="flr_bottom_msg_each_left_img">
							<img width="20" height="20" src="../../../static/img/国学论坛/文章.png" alt="文章">
						</div>
						<div class="flr_bottom_msg_each_left_title">
							<span>[<a href="/#/Forum/Forum_list">{{item.forum_type.title}}</a>]</span>
							<div><router-link :to="'/Forum/Forum_detail?id='+item.id">{{item.title}}</router-link></div>
						</div>
					</div>
					<div class="flr_bottom_msg_each_right">
						<div class="flr_bottom_msg_each_right_each1">
							<div class="flr_bottom_msg_each_right_each1_div1"><a href="item.author_link" style="color: #0000FF;">{{item.author.username}}</a></div>
							<div class="flr_bottom_msg_each_right_each1_div2">{{item.add_time.replace("T", "").split(".")[0]}}</div>
						</div>
						<div class="flr_bottom_msg_each_right_each2">
							{{item.reply_count}}/{{item.browse_count}}
						</div>
						<div class="flr_bottom_msg_each_right_each1">
							<div class="flr_bottom_msg_each_right_each1_div1"><a href="" style="color: #0000FF;">{{item.forum_reply ? item.forum_reply : item.author.username}}</a></div>
							<div class="flr_bottom_msg_each_right_each1_div2">{{item.last_reply_time.replace("T", "").split(".")[0]}}</div>
						</div>
					</div>
				</div>
			</div>
			<div class="flr_bottom_top1">
				<router-link to="/Forum/Forum_publish"><div class="flr_bottom_top1_left_button">发帖</div></router-link>
				<!-- <div class="flr_bottom_top1_left_button"><router-link to="/Forum/Forum_publish">发帖</router-link></div> -->
				<div class="flr_bottom_top1_right_page">
					<div class="flr_bottom_top1_right_page_count">共{{Math.ceil(page_count/page_size)}}页</div>
					<div v-if="previous" @click="get_previous_page()" :class="['flr_bottom_top1_right_page_tiao', {flr_choose: previous}]">上一页</div>
					<div v-else class="flr_bottom_top1_right_page_tiao">上一页</div>
					<div @click="get_page(i+1, ordering)" :class="['flr_bottom_top1_right_page_num', {flr_bottom_top1_right_page_num_choose: i+1==p}]" v-for="(item, i) in page_range" :key="i">{{i+1}}</div>
					<div v-if="next" class="flr_bottom_top1_right_page_tiao flr_choose" @click="get_next_page()">下一页</div>
					<div v-else class="flr_bottom_top1_right_page_tiao">下一页</div>
				</div>
			</div>
		</div>
	</div>
</template>

<script>
	import {
		forum_detail_msgs,
	} from '@/api/api';
	function scroll_to_top(){
		window.scrollTo(0,0);
	}
	export default{
		name: 'Forum_list_right',
		data(){
			return {
				fl_title: '',
				
				forums_data_list: [],
				page_count: 0,
				page_size: 0,
				previous: null,
				next: null,
				forum_type_id: '',
				p: 1,
				page_range: '',
				ordering:'id',
				current_choose: 1,
			}
		},
		created(){
			this.current_forums_data_list = this.forums_data_list1;
			this.getroutedata();
			scroll_to_top();
		},
		methods: {
			change_current_forums_data_list(arg) {
				if(arg == 'last'){
					this.current_forums_data_list = this.forums_data_list1;
					this.current_choose = 2;
					this.get_page(this.p, '-id');
				}else if(arg == 'jinghua'){
					this.current_forums_data_list = this.forums_data_list2;
					this.current_choose = 1;
					this.get_page(this.p, '-browse_count');
				}else if(arg == 'hot'){
					this.current_forums_data_list = this.forums_data_list2;
					this.current_choose = 3;
					this.get_page(this.p, '-browse_count');
				}
			},
			getroutedata(){
				// 函数里面获取路由数据
				console.log(this.$route.query.t)
				if(this.$route.query.t == "zhewen"|this.fl_title == ''){
					this.fl_title = "哲学文化";
					this.forum_type_id = 12;
					this.get_forum_detail_msgs(this.forum_type_id, 10, 1);
				}
			},
			get_forum_detail_msgs(forum_typy_id, page_size, p){
				forum_detail_msgs({
					page_size: page_size,
					forum_type_id: forum_typy_id,
					p: p,
				}).then((response) => {
					this.forums_data_list = response.data.results;
					this.page_count = response.data.count;
					this.next = response.data.next;
					this.previous = response.data.previous;
					this.page_size = page_size;
					this.forum_type_id = forum_typy_id;
					this.p = p;
					this.page_range = new Array(Math.ceil(this.page_count/this.page_size));
				})
				.catch(function (error) {
					console.log(error);
				});
			},
			get_previous_page(){
				forum_detail_msgs({
					page_size: this.page_size,
					p: this.p>=1 ? this.p-1 : this.p,
					forum_type_id: this.forum_type_id,
					ordering:this.ordering,
				}).then((response) => {
					this.forums_data_list = response.data.results;
					this.page_count = response.data.count;
					this.next = response.data.next;
					this.previous = response.data.previous;
					this.page_size = this.page_size;
					// this.forum_type_id = this.forum_typy_id;
					this.p = this.p>=1 ? this.p-1 : this.p;
					this.page_range = new Array(Math.ceil(this.page_count/this.page_size));
				})
				.catch(function (error) {
					console.log(error);
				});
			},
			get_next_page(){
				forum_detail_msgs({
					page_size: this.page_size,
					p: this.p+1,
					forum_type_id: this.forum_type_id,
					ordering:this.ordering,
				}).then((response) => {
					this.forums_data_list = response.data.results;
					this.page_count = response.data.count;
					this.next = response.data.next;
					this.previous = response.data.previous;
					this.page_size = this.page_size;
					// this.forum_type_id = this.forum_typy_id;
					this.p = this.p+1;
					this.page_range = new Array(Math.ceil(this.page_count/this.page_size));
				})
				.catch(function (error) {
					console.log(error);
				});
			},
			get_page(p, ordering){
				forum_detail_msgs({
					page_size: this.page_size,
					p: p,
					forum_type_id: this.forum_type_id,
					ordering: ordering
				}).then((response) => {
					this.forums_data_list = response.data.results;
					this.page_count = response.data.count;
					this.next = response.data.next;
					this.previous = response.data.previous;
					this.page_size = this.page_size;
					this.p = p;
					this.ordering = ordering;
					this.page_range = new Array(Math.ceil(this.page_count/this.page_size));
				})
				.catch(function (error) {
					console.log(error);
				});
			},
		},
		computed: {
			current_forums_data_lists() {
				return this.current_forums_data_list; 
			},
			fl_titles() {
				if(this.$route.query.t == "jinguo"){
					this.fl_title = "今日国学";
					this.forum_type_id = 2;
					this.get_forum_detail_msgs(this.forum_type_id, 10, 1);
				}else if(this.$route.query.t == "shire"){
					this.fl_title = "时事热点";
					this.forum_type_id = 3;
					this.get_forum_detail_msgs(this.forum_type_id, this.page_size, 1);
				}else if(this.$route.query.t == "guozi"){
					this.fl_title = "国学资讯";
					this.forum_type_id = 20;
					this.get_forum_detail_msgs(this.forum_type_id, this.page_size, 1);
				}else if(this.$route.query.t == "wenzi"){
					this.fl_title = "文化自信";
					this.forum_type_id = 21;
					this.get_forum_detail_msgs(this.forum_type_id, this.page_size, 1);
				}else if(this.$route.query.t == "jingjing"){
					this.fl_title = "经学经事";
					this.forum_type_id = 5;
					this.get_forum_detail_msgs(this.forum_type_id, this.page_size, 1);
				}else if(this.$route.query.t == "shishi"){
					this.fl_title = "史学实录";
					this.forum_type_id = 6;
					this.get_forum_detail_msgs(this.forum_type_id, this.page_size, 1);
				}else if(this.$route.query.t == "zidao"){
					this.fl_title = "子学道统";
					this.forum_type_id = 7;
					this.get_forum_detail_msgs(this.forum_type_id, this.page_size, 1);
				}else if(this.$route.query.t == "wenzong"){
					this.fl_title = "文学总集";
					this.forum_type_id = 8;
					this.get_forum_detail_msgs(this.forum_type_id, this.page_size, 1);
				}else if(this.$route.query.t == "shiqing"){
					this.fl_title = "诗词清话";
					this.forum_type_id = 10;
					this.get_forum_detail_msgs(this.forum_type_id, this.page_size, 1);
				}else if(this.$route.query.t == "jingshi"){
					this.fl_title = "经济史论";
					this.forum_type_id = 11;
					this.get_forum_detail_msgs(this.forum_type_id, this.page_size, 1);
				}else if(this.$route.query.t == "zhewen"|this.fl_title == ''){
					this.fl_title = "哲学文化";
					this.forum_type_id = 12;
					this.get_forum_detail_msgs(this.forum_type_id, this.page_size, 1);
				}else if(this.$route.query.t == "guoren"){
					this.fl_title = "国学人物";
					this.forum_type_id = 13;
					this.get_forum_detail_msgs(this.forum_type_id, this.page_size, 1);
				}else if(this.$route.query.t == "mingdian"){
					this.fl_title = "名人典故";
					this.forum_type_id = 15;
					this.get_forum_detail_msgs(this.forum_type_id, this.page_size, 1);
				}else if(this.$route.query.t == "baixing"){
					this.fl_title = "百家姓氏";
					this.forum_type_id = 16;
					this.get_forum_detail_msgs(this.forum_type_id, this.page_size, 1);
				}else if(this.$route.query.t == "jiefeng"){
					this.fl_title = "节日风俗";
					this.forum_type_id = 17;
					this.get_forum_detail_msgs(this.forum_type_id, this.page_size, 1);
				}
				
				return this.fl_title;
			}
					
		},
	}
</script>

<style scoped="scoped">
	.flr_all{
		width: 750px;
		height: 500px;
		/* border: 1px solid gray; */
	}
	.flr_top{
		width: 750px;
		height: 71px;
		border: 1px solid white;
		background: white;
	}
	.flr_all .flr_top_title{
		float: left;
		padding-top: 10px;
		marign-top: 10px;
		margin-left: 10px;
		text-align: left;
		font-family: 'Microsoft YaHei','SF Pro Display',Roboto,Noto,Arial,'PingFang SC',sans-serif!important;
		font-size: 21px;
		color: #4d4d4d;
		font-weight: 700;
	}
	.flr_top_msg{
		width: 750px;
		height: 20px;
		font-size: 14px;
		color: #999;
		margin-top: 42px;
        margin-left: 9px;
		text-align: left;
		font-family: 'Microsoft YaHei','SF Pro Display',Roboto,Noto,Arial,'PingFang SC',sans-serif!important;
	}
	.flr_bottom{
		background: white;
		width: 750px;
		height: 700px;
		margin-top: 10px;
		/* border: 1px solid gray; */
	}
	.flr_bottom .flr_bottom_title{
		float: left;
		line-height: 30px;
		height: 30px;
		/* background: #00FFFF; */
		width: 750px;
		border-bottom: 1px solid lightgray;
	}
	.flr_bottom_title div{
		float: left;
		width: 60px;
		height: 30px;
		font-size: 13px;
		margin-left: 6px;
		text-align: center;
		cursor: pointer;
		font-family: 'Microsoft YaHei','SF Pro Display',Roboto,Noto,Arial,'PingFang SC',sans-serif!important;
	}
	.flr_bottom_title div:hover{
		background: #F2F2F2;
		opacity: 0.7;
		border-bottom: 2px solid gray;
	}
	.flr_choose_status{
		background: #F2F2F2 !important;
		opacity: 0.7 !important;
		border-bottom: 2px solid gray !important;
	}
	.flr_bottom_top{
		height: 57px;
		width: 750px;
		line-height: 50px;
		border-bottom: 1px solid lightgray;
	}
	
	.flr_bottom_top_left_button{
		float: left;
		box-sizing: content-box;
		z-index: auto;
		width: 36px;
		height: 20px;
		position: static;
		cursor: pointer;
		opacity: 1;
		margin: 0;
		padding: 10px 20px;
		overflow: visible;
		border: 1px solid darkgray;
		border-radius: 3px;
		font: normal 16px/normal "Times New Roman", Times, serif;
		color: rgba(255,255,255,0.9);
		text-overflow: clip;
		background: darkgray;
		box-shadow: 1px 1px 4px 0 rgba(0,0,0,0.2), 2px 2px 2px 0 rgba(173,67,67,0.2);
		text-shadow: -1px -1px 0 rgba(15,73,168,0.66);
		line-height: 19px;
		margin-top: 7px;
		margin-left: 6px;
	}
	.flr_bottom_top_left_button a, .flr_bottom_top1_left_button a{
		color: white;
	}
	.flr_bottom_top_left_button a:hover, .flr_bottom_top1_left_button a:hover{
		color: white !important;
		text-decoration: none !important;
	}
	.flr_bottom_top1_left_button a{
		line-height: 23px;
	}
	.flr_bottom_top .flr_bottom_top_right_page{
		float: right;
		height: 57px;
		width: 315px;
		/* background: #0000FF; */
		line-height: 57px;
		font-size: 13px;
		font-family: "microsoft sans serif";
	}
	.flr_bottom_top_right_page_count{
		float: left;
		width: 60px;
		height: 45px;
		color: #CCCCCC;
	}
	.flr_bottom_top_right_page_num{
		float: left;
		width: 25px;
		height: 25px;
		line-height: 26px;
		margin-top: 15px;
		margin-left: 2px;
		margin-right: 2px;
	}
	.flr_bottom_top_right_page .flr_bottom_top_right_page_num_choose{
		background: lightgray;
		color: white;
		border-radius: 6px;
	}
	.flr_bottom_top_right_page_num:hover{
		background: lightgray;
		cursor: pointer;
		color: white;
		border-radius: 6px;
	}
	.flr_bottom_top_right_page_tiao{
		float: left;
		height: 45px;
		width: 40px;
		margin-left: 3px;
		margin-right: 10px;
	}
	
	.flr_choose{
		cursor: pointer;
	}
	.flr_choose:hover{
		color: #3737FD;
	}
	
	.flr_bottom .flr_bottom_title_desc{
		float: left;
		line-height: 30px;
		height: 30px;
		background: #DEDEDE;
		width: 750px;
		/* border-bottom: 1px solid #DEDEDE; */
	}
	.flr_bottom_title_desc_left{
		float: left;
		margin-left: 20px;
	}
	.flr_bottom_title_desc_right{
		float: right;
		margin-right: 8px;
	}
	.flr_bottom_title_desc_right1{
		float: left;
		width: 150px;
	}
	.flr_bottom_title_desc_right2{
		float: left;
		width: 52px;
		margin-left: 34px;
	}
	.flr_bottom_title_desc_right3{
		float: left;
		width: 162px;
		margin-left: -41px;
		margin-right: 11px;
	}
	.flr_bottom .flr_bottom_msg{
		float: left;
		height: 584px;
		width: 750px;
		border: 1px solid lightgray;
		overflow: hidden;
	}
	.flr_bottom .flr_bottom_msg_each{
		float: left;
		line-height: 53px;
		height: 53px;
		width: 750px;
		border-bottom: 1px solid lightgray;
		transition: all 0.8s ease;
	}
	.flr_bottom .flr_bottom_msg_each:hover{
		background: #EDEDED;
		opacity: 0.6;
	}
	.flr_bottom .flr_bottom_msg_each_left{
		float: left;
		line-height: 53px;
		height: 53px;
		width: 428px;
		/* border-right: 1px solid lightgray; */
	}
	.flr_bottom .flr_bottom_msg_each_left_img{
		float: left;
		line-height: 63px;
		height: 53px;
		width: 40px;
	}
	.flr_bottom_msg_each_left_title{
		float: left;
		line-height: 54px;
		height: 53px;
		width: 379px;
		font-size: 13px;
	}
	.flr_bottom_msg_each_left_title span{
		float: left;
		margin-right: 4px;
		color: #0000FF;
	}
	.flr_bottom_msg_each_left_title span a{
		color: #0000FF;
	}
	.flr_bottom_msg_each_left_title div{
		float: left;
		color: #4D4D4D;
	}
	.flr_bottom_msg_each_left_title div a{
		text-decoration: none;
		transition: all 0.7s ease;
	}
	.flr_bottom_msg_each_left_title div a:hover{
		font-size: 14px;
	}
	/* .flr_bottom .flr_bottom_msg_each_left */
	.flr_bottom_msg_each_right{
		float: right;
		line-height: 53px;
		height: 53px;
		width: 306px;
		/* border-left: 1px solid lightgray; */
	}
	.flr_bottom_msg_each_right_each1{
		float: left;
		line-height: 53px;
		height: 53px;
		width: 100px;
		margin-left: -8px;
	}
	.flr_bottom_msg_each_right_each1_div1{
		float: left;
		width: 100px;
		height: 25px;
		padding-top: 5px;
		margin-bottom: -2px;
		text-align: left;
		line-height: 25px;
		font-size: 12px;
	}
	.flr_bottom_msg_each_right_each1_div1 a{
		color: #6E99ED;
	}
	.flr_bottom_msg_each_right_each1_div2{
		float: left;
		width: 110px;
		height: 25px;
		margin-bottom: -7px;
		text-align: left;
		line-height: 25px;
		font-size: 12px;
		/* color: #0000FF; */
	}
	.flr_bottom_msg_each_right_each2{
		float: left;
		line-height: 53px;
		height: 53px;
		width: 100px;
		margin-left: -2px;
	}
	
	.flr_bottom .flr_bottom_top1{
		float: left;
		margin-top: 10px;
		background: white;
		height: 57px;
		width: 749px;
		line-height: 50px;
		/* border: 1px solid lightgray; */
	}
	
	.flr_bottom_top1_left_button{
		float: left;
		box-sizing: content-box;
		z-index: auto;
		width: 36px;
		height: 20px;
		position: static;
		cursor: pointer;
		opacity: 1;
		margin: 0;
		padding: 10px 20px;
		overflow: visible;
		border: 1px solid darkgray;
		border-radius: 3px;
		font: normal 16px/normal "Times New Roman", Times, serif;
		color: rgba(255,255,255,0.9);
		text-overflow: clip;
		background: darkgray;
		-webkit-box-shadow: 1px 1px 4px 0 rgba(0,0,0,0.2), 2px 2px 2px 0 rgba(173,67,67,0.2);
		box-shadow: 1px 1px 4px 0 rgba(0,0,0,0.2), 2px 2px 2px 0 rgba(173,67,67,0.2);
		text-shadow: -1px -1px 0 rgba(15,73,168,0.66);
		line-height: 19px;
		margin-top: 7px;
		margin-left: 6px;
	}
	.flr_bottom_top1 .flr_bottom_top1_right_page{
		float: right;
		height: 57px;
		width: 315px;
		/* background: #0000FF; */
		line-height: 57px;
		font-size: 13px;
		font-family: "microsoft sans serif";
	}
	.flr_bottom_top1_right_page_count{
		float: left;
		width: 60px;
		height: 45px;
		color: #CCCCCC;
	}
	.flr_bottom_top1_right_page_num{
		float: left;
		width: 25px;
		height: 25px;
		line-height: 26px;
		margin-top: 15px;
		margin-left: 2px;
		margin-right: 2px;
	}
	.flr_bottom_top1_right_page .flr_bottom_top1_right_page_num_choose{
		background: lightgray;
		color: white;
		border-radius: 6px;
	}
	.flr_bottom_top1_right_page_num:hover{
		background: lightgray;
		color: white;
		cursor: pointer;
		border-radius: 6px;
	}
	.flr_bottom_top1_right_page_tiao{
		float: left;
		height: 45px;
		width: 40px;
		margin-left: 3px;
		margin-right: 10px;
	}
</style>
