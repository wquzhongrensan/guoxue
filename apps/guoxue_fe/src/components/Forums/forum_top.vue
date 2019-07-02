<template>
	<div class="f_msg_left_top_msg_right">
		<div class="f_msg_left_top_msg_right_top">
			<div :class="{f_msg_left_top_msg_right_top_choose:choose==1}"><a href="javascript:;" @click="change_talk_msg('last')">最新帖子</a></div>
			<div :class="{f_msg_left_top_msg_right_top_choose:choose==2}"><a href="javascript:;" @click="change_talk_msg('jinghua')">论坛精华</a></div>
		</div>
		<div class="f_msg_left_top_msg_right_bottom_msg" style="background: white; border-radius: 11px;">
			<div class="f_msg_left_top_msg_right_bottom_msg_each" v-for="(item, i) in talking_msg_msg" :key="i">
				<div class="f_msg_left_top_msg_right_bottom_msg_each_1">
					<router-link :to="'/Forum/Forum_detail?id='+item.id"><img height="50" width="60" src="../../static/img/文章灰.svg" alt="帖子详情"/></router-link>
				</div>
				<div class="f_msg_left_top_msg_right_bottom_msg_each_2">
					<div class="f_msg_left_top_msg_right_bottom_msg_each_2_div1"><span><router-link :to="'/Forum/Forum_detail?id='+item.id">{{item.title}}</router-link></span></div><br />
					<div class="f_msg_left_top_msg_right_bottom_msg_each_2_div2">
						<span><router-link to="javascript:;">{{item.author.username}}</router-link></span>&nbsp;&nbsp;
						<span v-text="item.add_time.replace('T', '').split('.')[0]"></span>
					</div>
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
		name: 'forum_top',
		data(){
			return {
				talking_msg_msg: [],
				choose: 1,
				
			}
		},
		created(){
			this.get_detail_forum_msg(4, '-id');
			scroll_to_top();
		},
		methods: {
			change_talk_msg(arg) {
				if(arg == 'last'){
					this.choose = 1;
					this.get_detail_forum_msg(4, '-id');
				}else if(arg == 'jinghua'){
					this.choose = 2;
					this.get_detail_forum_msg(4, '-browse_count');
				}
			},
			get_detail_forum_msg(page_size, ordering){
				// 获取帖子详情信息
				forum_detail_msgs({
					page_size: page_size,
					ordering: ordering,
				}).then((response) => {
					this.talking_msg_msg = response.data.results;
				})
				.catch(function (error) {
					console.log(error);
				});
			}
		},
	}
</script>

<style scoped="scoped">
	.f_msg_left_top_msg_right{
		width: 340px;
		height: 313px;
		float: right;
		/* border: 1px solid gray; */
	}
	.f_msg_left_top_msg_right_top{
		height: 33px;
		width: 340px;
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
	.f_msg_left_top_msg_right_top_choose{
		border-bottom: 2px solid red;
	}
	.f_msg_left_top_msg_right_bottom_msg{
		width: 338px;
		margin-top: 10px;
		height: 265px;
		/* border: 1px solid gray; */
	}
	.f_msg_left_top_msg_right_bottom_msg_each{
		display: inline-block;
		width: 337px;
		margin-x: auto;
		line-height: 65px;
		height: 65px;
		border: 1px solid lightgray;
		border-radius: 10px;
		transition: all 0.8s ease;
	}
	.f_msg_left_top_msg_right_bottom_msg_each div{
		display: inline-block;
		height: 57px;
	}
	.f_msg_left_top_msg_right_bottom_msg_each_1{
		float: left;
		margin-top: 7px;
		margin-left: 10px;
	}
	.f_msg_left_top_msg_right_bottom_msg_each_2{
		float: left;
		margin-left: 8px;	
		line-height: 30px;
	}
	.f_msg_left_top_msg_right_bottom_msg_each_2 div{
		float: left;
		height: 10px;
	}
	.f_msg_left_top_msg_right_bottom_msg_each_2_div1{
		font-size: 15px;
		font-weight: 400;
		margin-top:5px;
	}
	.f_msg_left_top_msg_right_bottom_msg_each a:hover{
		text-decoration: none;
		color: #D57B7B;
	}
	.f_msg_left_top_msg_right_bottom_msg_each:hover{
		box-shadow: 4px 4px 8px 2px rgba(0,0,0,0.2) ;
		background:#FBFBFB;
	}
</style>
