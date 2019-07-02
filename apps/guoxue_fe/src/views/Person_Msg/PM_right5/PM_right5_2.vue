<template>
	<div class="pmr_1">
		<div class="pmr_bottom_title_desc">
			<div class="pmr_bottom_title_desc_left">板块主题</div>
			<div class="pmr_bottom_title_desc_right">
				<div class="pmr_bottom_title_desc_right2">查看</div>
				<div class="pmr_bottom_title_desc_right3">最后发表</div>
				<div class="pmr_bottom_title_desc_right1" style="margin-right: 17px;margin-left: -16px;">作者</div>
			</div>
		</div>
		
		<div class="pmr_bottom_msg">
			<div class="pmr_bottom_msg_each" v-for="(item, i) in forum_data" :key="i">
				<div class="pmr_bottom_msg_each_left">
					<div class="pmr_bottom_msg_each_left_img">
						<img width="20" height="20" src="../../../static/img/国学论坛/文章.png" alt="文章">
					</div>
					<div class="pmr_bottom_msg_each_left_title">
						<span>[<a href="">{{item.topic.forum_type.title}}</a>]</span>
						<div><router-link :to="'/Forum/Forum_detail?id='+item.topic.id">{{maxSlice(item.topic.title, 16)}}</router-link></div>
					</div>
				</div>
				<div class="pmr_bottom_msg_each_right">
					<div class="pmr_bottom_msg_each_right_each2">
						{{item.topic.browse_count}}
					</div>
					<div class="pmr_bottom_msg_each_right_each1" style="width: 127px;margin-left: -20px;margin-top: 14px;">
						<div class="pmr_bottom_msg_each_right_each1_div2">{{item.topic.last_reply_time.replace("T", " ").split(".")[0]}}</div>
					</div>
					<div class="pmr_bottom_msg_each_right_each1" style="margin-top: 14px;margin-left: 1px;">
						<div class="pmr_bottom_msg_each_right_each1_div2">{{item.topic.author.username}}</div>
					</div>
					
				</div>
			</div>
			<div class="pmr_page_bottom" v-if="forum_data">
				<div class="pmrr_bottom_top1_right_page">
					<div class="pmrr_bottom_top1_right_page_count">共{{page_range.length}}页</div>
					<div v-if="previous" @click="get_page(p-1)" :class="['pmrr_bottom_top1_right_page_tiao', {flr_choose: previous}]">上一页</div>
					<div v-else class="pmrr_bottom_top1_right_page_tiao">上一页</div>
					<div @click="get_page(i+1)" :class="['pmrr_bottom_top1_right_page_num', {pmrr_bottom_top1_right_page_num_choose: i+1==p}]" v-for="(item, i) in page_range" :key="i">{{i+1}}</div>
					<div v-if="next" class="pmrr_bottom_top1_right_page_tiao flr_choose" @click="get_page(p+1)">下一页</div>
					<div v-else class="pmrr_bottom_top1_right_page_tiao">下一页</div>
				</div>
			</div>
		</div>
		
	</div>
</template>

<script>
	import {
		getCookie,
	} from '@/utils/cookies';
	import {
		get_reply_forums,
	} from '@/api/api';
	
	export default{
		name: 'PM_right5_2',
		computed: {
			current_forums_data_lists() {
				return this.current_forums_data_list; 
			},
		},
		
		data(){
			return{
				current_forums_data_list: [
					{
						type_data: '经史子集',
						type_link: '',
						msg_data: '道不可说？',
						msg_link: '/Forum/Forum_detail?id=1',
						author: 'laoliang',
						author_link: '',
						forum_create_time: '2019-04-24 10:59',
						count_of_visit: '434',
						count_of_answer: '32342',
						last_answer_author: 'laowang',
						last_answer_author_link: '',
						last_answer_time: '2019-04-24 10:00'
					},
					{
						type_data: '经史子集',
						type_link: '',
						msg_data: '何为一阴一阳之为道？',
						msg_link: '',
						author: 'laoliang',
						author_link: '',
						forum_create_time: '2019-04-24 10:59',
						count_of_visit: '434',
						count_of_answer: '32342',
						last_answer_author: 'laowang',
						last_answer_author_link: '',
						last_answer_time: '2019-04-24 10:00'
					},
					{
						type_data: '经史子集',
						type_link: '',
						msg_data: '何为一阴一阳之为道？',
						msg_link: '',
						author: 'laoliang',
						author_link: '',
						forum_create_time: '2019-04-24 10:59',
						count_of_visit: '434',
						count_of_answer: '32342',
						last_answer_author: 'laowang',
						last_answer_author_link: '',
						last_answer_time: '2019-04-24 10:00'
					},
					{
						type_data: '经史子集',
						type_link: '',
						msg_data: '何为一阴一阳之为道？',
						msg_link: '',
						author: 'laoliang',
						author_link: '',
						forum_create_time: '2019-04-24 10:59',
						count_of_visit: '434',
						count_of_answer: '32342',
						last_answer_author: 'laowang',
						last_answer_author_link: '',
						last_answer_time: '2019-04-24 10:00'
					},
					{
						type_data: '经史子集',
						type_link: '',
						msg_data: '何为一阴一阳之为道？',
						msg_link: '',
						author: 'laoliang',
						author_link: '',
						forum_create_time: '2019-04-24 10:59',
						count_of_visit: '434',
						count_of_answer: '32342',
						last_answer_author: 'laowang',
						last_answer_author_link: '',
						last_answer_time: '2019-04-24 10:00'
					},
					{
						type_data: '经史子集',
						type_link: '',
						msg_data: '何为一阴一阳之为道？',
						msg_link: '',
						author: 'laoliang',
						author_link: '',
						forum_create_time: '2019-04-24 10:59',
						count_of_visit: '434',
						count_of_answer: '32342',
						last_answer_author: 'laowang',
						last_answer_author_link: '',
						last_answer_time: '2019-04-24 10:00'
					},
					{
						type_data: '经史子集',
						type_link: '',
						msg_data: '何为一阴一阳之为道？',
						msg_link: '',
						author: 'laoliang',
						author_link: '',
						forum_create_time: '2019-04-24 10:59',
						count_of_visit: '434',
						count_of_answer: '32342',
						last_answer_author: 'laowang',
						last_answer_author_link: '',
						last_answer_time: '2019-04-24 10:00'
					},
					
				],
				forum_data: '',
				page_size: 7,
				p: 1,
				page_count: 0,
				page_range: [],
				previous: null,
				next: null
			}
		},
		methods: {
			get_reply_forums_msgs() {
				get_reply_forums({
					author:getCookie("user_id"),
					page_size: this.page_size,
					p: this.p
				}).then((response) => {
					this.forum_data = response.data.results;
					this.page_count = response.data.count;
					this.next = response.data.next;
					this.previous = response.data.previous;
					this.page_range = new Array(Math.ceil(this.page_count/this.page_size));
				}).catch(function(error){
					console.log(error)
				})
			},
			get_page(p){
				get_reply_forums({
					author:getCookie("user_id"),
					page_size: this.page_size,
					p: p
				}).then((response) => {
					this.forum_data = response.data.results;
					this.p = p;
					this.page_count = response.data.count;
					this.next = response.data.next;
					this.previous = response.data.previous;
					this.page_range = new Array(Math.ceil(this.page_count/this.page_size));
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
			this.get_reply_forums_msgs();
		}
	}
</script>

<style scoped="scoped">
	.pmr_1{
		float: left;
		width: 710px;
		height: 400px;
		/* margin-left: 10px; */
	}
	.pmr_bottom_title_desc{
		float: left;
		line-height: 30px;
		height: 30px;
		/* background: skyblue; */
		width: 724px;
		border-bottom: 1px solid lightgray;
	}
	.pmr_bottom_title_desc_left{
		float: left;
		margin-left: 12px;
	}
	.pmr_bottom_title_desc_right{
		float: right;
		margin-right: 8px;
	}
	.pmr_bottom_title_desc_right1{
		float: left;
		width: 51px;
	}
	.pmr_bottom_title_desc_right2{
		float: left;
		width: 130px;
		margin-left: 30px;
	}
	.pmr_bottom_title_desc_right3{
		float: left;
		width: 147px;
		margin-left: -28px;
	}
	.pmr_bottom_msg{
		float: left;
		height: 584px;
		width: 724px;
		overflow: hidden;
	}
	.pmr_bottom_msg_each{
		float: left;
		line-height: 53px;
		height: 53px;
		width: 724px;
		border-bottom: 1px solid lightgray;
		transition: all 0.8s ease;
	}
	.pmr_bottom_msg_each:hover{
		background: #EDEDED;
		opacity: 0.8;
	}
	.pmr_bottom_msg_each_left{
		float: left;
		line-height: 53px;
		height: 53px;
		width: 350px;
	}
	.pmr_bottom_msg_each_left_img{
		float: left;
		line-height: 63px;
		height: 53px;
		width: 40px;
		margin-left: 5px;
	}
	.pmr_bottom_msg_each_left_title{
		float: left;
		line-height: 54px;
		height: 53px;
		width: 300px;
		font-size: 13px;
	}
	.pmr_bottom_msg_each_left_title span{
		float: left;
		margin-right: 4px;
		color: #0000FF;
	}
	.pmr_bottom_msg_each_left_title span a{
		color: #0000FF;
	}
	.pmr_bottom_msg_each_left_title div{
		float: left;
		color: #4D4D4D;
	}
	.pmr_bottom_msg_each_left_title div a{
		text-decoration: none;
		transition: all 0.7s ease;
	}
	.pmr_bottom_msg_each_left_title div a:hover{
		font-size: 14px;
	}
	/* .pmr_bottom .pmr_bottom_msg_each_left */
	.pmr_bottom_msg_each_right{
		float: right;
		line-height: 53px;
		height: 53px;
		width: 306px;
		/* border-left: 1px solid lightgray; */
	}
	.pmr_bottom_msg_each_right_each1{
		float: left;
		line-height: 53px;
		height: 53px;
		width: 100px;
	}
	.pmr_bottom_msg_each_right_each1_div1{
		float: left;
		width: 100px;
		height: 25px;
		padding-top: 5px;
		margin-bottom: -2px;
		text-align: left;
		line-height: 25px;
		font-size: 12px;
	}
	.pmr_bottom_msg_each_right_each1_div1 a{
		color: #6E99ED;
	}
	.pmr_bottom_msg_each_right_each1_div2{
		float: left;
		width: 112px;
		height: 25px;
		margin-bottom: -7px;
		text-align: left;
		line-height: 25px;
		font-size: 12px;
		/* color: #0000FF; */
	}
	.pmr_bottom_msg_each_right_each2{
		float: left;
		line-height: 53px;
		height: 53px;
		width: 100px;
		margin-left: -2px;
	}
	.pmr_bottom_msg_each_right_each1_div3{
		float: left;
		width: 57px;
		height: 30px;
		margin-top: 11px;
		margin-left: 33px;
		background: #C9CBCB;
		margin-bottom: -7px;
		text-align: center;
		border-radius: 5px;
		line-height: 30px;
		font-size: 13px;
		cursor: pointer;
	}
	.pmr_page_bottom{
		float: left;
		line-height: 56px;
		height: 60px;
		width: 504px;
		margin-top: 0px;
		margin-left: 201px;
		text-align: center;
	}
	.pmrr_bottom_top1 .pmrr_bottom_top1_right_page{
		float: right;
		height: 57px;
		width: 715px;
		line-height: 57px;
		font-size: 13px;
		font-family: "microsoft sans serif";
	}
	.pmrr_bottom_top1_right_page_count{
		float: left;
		width: 60px;
		height: 45px;
		color: #CCCCCC;
	}
	.pmrr_bottom_top1_right_page_num{
		float: left;
		width: 25px;
		height: 25px;
		line-height: 26px;
		margin-top: 15px;
		margin-left: 2px;
		margin-right: 2px;
	}
	.pmrr_bottom_top1_right_page .pmrr_bottom_top1_right_page_num_choose{
		background: lightgray;
		color: white;
		border-radius: 6px;
	}
	.pmrr_bottom_top1_right_page_num:hover{
		background: lightgray;
		color: white;
		border-radius: 6px;
		cursor: pointer;
	}
	.pmrr_bottom_top1_right_page_tiao{
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
</style>
