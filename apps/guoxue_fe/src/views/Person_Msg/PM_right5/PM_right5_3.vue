<template>
	<div class="pmr_1">
		<div class="pmr_bottom_title_desc">
			<div class="pmr_bottom_title_desc_left">板块主题</div>
			<div class="pmr_bottom_title_desc_right">
				
				<div class="pmr_bottom_title_desc_right2">回复/查看</div>
				<div class="pmr_bottom_title_desc_right3">最后发表</div>
				<div class="pmr_bottom_title_desc_right1">管理</div>
			</div>
		</div>
		
		<div class="pmr_bottom_msg">
			<div class="pmr_bottom_msg_each" v-for="(item, i) in forums_data_list" :key="i">
				<div class="pmr_bottom_msg_each_left">
					<div class="pmr_bottom_msg_each_left_img">
						<img width="20" height="20" src="../../../static/img/国学论坛/文章.png" alt="文章">
					</div>
					<div class="pmr_bottom_msg_each_left_title">
						<span>[<router-link to="/Forum/Forum_list">{{item.forum_type.title}}</router-link>]</span>
						<div><router-link :to="'/Forum/Forum_detail?id=' + item.id">{{maxSlice(item.title, 16)}}</router-link></div>
					</div>
				</div>
				<div class="pmr_bottom_msg_each_right">
					
					<div class="pmr_bottom_msg_each_right_each2">
						<span style="margin-left: 17px;">{{item.reply_count}}/{{item.browse_count}}</span>
					</div>
					<div class="pmr_bottom_msg_each_right_each1">
						<div class="pmr_bottom_msg_each_right_each1_div1"><a style="color: #3131FD" href="javascript:;">{{item.author.username}}</a></div>
						<div class="pmr_bottom_msg_each_right_each1_div2">{{item.last_reply_time.replace("T", " ").split(".")[0]}}</div>
					</div>
					<div class="pmr_bottom_msg_each_right_each1">
						<div class="pmr_bottom_msg_each_right_each1_div3" @click="deleteforum(item.id)">删除</div>
					</div>
				</div>
			</div>
			<div class="pmr_page_bottom" v-if="forums_data_list">
				<div class="pmrr_bottom_top1_right_page">
					<div class="pmrr_bottom_top1_right_page_count">共{{page_range.length}}页</div>
					<div v-if="previous" @click="get_page(p-1, ordering)" :class="['pmrr_bottom_top1_right_page_tiao', {flr_choose: previous}]">上一页</div>
					<div v-else class="pmrr_bottom_top1_right_page_tiao">上一页</div>
					<div @click="get_page(i+1, ordering)" :class="['pmrr_bottom_top1_right_page_num', {pmrr_bottom_top1_right_page_num_choose: i+1==p}]" v-for="(item, i) in page_range" :key="i">{{i+1}}</div>
					<div v-if="next" class="pmrr_bottom_top1_right_page_tiao flr_choose" @click="get_page(p+1, ordering)">下一页</div>
					<div v-else class="pmrr_bottom_top1_right_page_tiao">下一页</div>
				</div>
			</div>
		</div>
		
	</div>
</template>

<script>
	import {forum_detail_msgs} from '@/api/api';
	import {getCookie} from '@/utils/cookies';
	
	export default{
		name: 'PM_right5_3',
		computed: {
			current_forums_data_lists() {
				return this.current_forums_data_list; 
			},
		},
		
		data(){
			return{
				person_msg: '',
				p: 1,
				page_size: 7,
				page_range: [],
				ordering: '-browse_count',
				forums_data_list: '',
				page_count:0,
				previous: null,
				next: null,
			}
		},
		methods: {
			get_forum_msgs(){
				forum_detail_msgs({
					author: getCookie("user_id"),
					p: this.p,
					page_size: this.page_size,
					ordering:this.ordering,
				}).then((response) => {
					this.forums_data_list = response.data.results;
					this.page_count = response.data.count;
					this.next = response.data.next;
					this.previous = response.data.previous;
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
					author: getCookie("user_id"),
					ordering: ordering
				}).then((response) => {
					this.forums_data_list = response.data.results;
					this.page_count = response.data.count;
					this.next = response.data.next;
					this.previous = response.data.previous;
					this.p = p;
					this.ordering = ordering;
					this.page_range = new Array(Math.ceil(this.page_count/this.page_size));
				})
				.catch(function (error) {
					console.log(error);
				});
			},
			deleteforum(id){
				if(confirm("确认删除吗？")){
					forum_detail_msgs({
						delete_id: id
					}).then((response) => {
						this.get_forum_msgs();
					}).catch(function(error){
						console.log(error)
					})
				}
			},
			maxSlice(content, max_length ){
				return content.length > max_length ? content.slice(0, max_length) + '...' : content;
			},
			
		},
		created(){
			this.get_forum_msgs();
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
		width: 113px;
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
