<template>
	<div style="width: 1000px;margin: 0 auto;">
		<div class="h_g_nav">
			<el-breadcrumb separator="/">
				<el-breadcrumb-item :to="{ path: '/' }">首页</el-breadcrumb-item>
				<el-breadcrumb-item :to="{ path: '/H_jingshi' }">经济史论</el-breadcrumb-item>
				<el-breadcrumb-item :to="{ path: '/H_jingshi/HJ_detail' }">详情</el-breadcrumb-item>
			</el-breadcrumb>
		</div>
		<div class="hs_d_bottom">
			
			<div class="hs_d_bottom_bottom" style="background: white;"  v-if="ArticleDMsgs">
				<div class="hs_d_bottom_bottom_title">
					<strong>{{ArticleDMsgs.title}}</strong>
				</div>
				<div class="hs_d_bottom_bottom_msg" v-html="ArticleDMsgs.article_content[0].content">
				</div>
				<div class="hs_d_bottom_bottom_other">
					<div>点击量：<span>{{ArticleDMsgs.browse_count}}</span></div>
					<div>发布时间：<span>{{ArticleDMsgs.update_time.split("T")[0]}}</span></div>
				</div>
			</div>
			<div class="hs_d_bottom_bottom_bottom_line" v-else>
				还没有添加相关的数据，请您耐心等待数据的更新，谢谢您的配合
			</div>
			
			<div class="hs_d_bottom_bottom_bottom_line" v-if="ArticleDMsgs"></div>
		</div>
	</div>
	
</template>

<script>
	import {getArticleDMsgs} from '@/api/api'
	function scroll_to_top(){
		window.scrollTo(0,0);
	}
	export default{
		name: 'HJ_detail',
		data(){
			return{
				// 文章详情的数据
				ArticleDMsgs: '',
			}
			
		},
		methods: {
			getArticleDMsgs(id){
				getArticleDMsgs({
					id: id,
				}).then((response) => {
					this.ArticleDMsgs = response.data;
				})
				.catch(function (error) {
					console.log(error);
				});
			}
		},
		created(){
			scroll_to_top();
			this.getArticleDMsgs(this.$route.params.id);
		},
		
	}
</script>

<style scoped="">
	.h_g_nav{
		margin-top: 4px;
		margin-left: 4px;
		margin-bottom: 7px;
	}
	.hs_d_bottom{
		border-top:1px solid lightgray;
		width: 1000px;
		/* height: 2000px; */
		margin: 0 auto;
	}
	.hs_d_bottom_top{
		width: 950px;
		height: 200px;
		margin: 0px auto;
		/* border: 1px solid lightgray; */
		margin-top: 15px;
	}
	.hs_d_bottom_top_left{
		float: left;
		width: 130px;
		height: 180px;
		margin-left: 20px;
		margin-top: 11px;
		border: 1px dotted lightgray;
	}
	.hs_d_bottom_top_left:hover{
		border: 1px solid lightgray;
	}
	.hs_d_bottom_top_left div{
		margin: 4px auto;
	}
	.hs_d_bottom_top_right{
		float: right;
		width: 780px;
		height: 200px;
		/* border: 1px solid lightgray; */
		margin-left: -30px;
	}
	.hs_d_bottom_top_right p{
		float: left;
		margin-top: 33px;
		font-size: 19px;
		font-weight: 580;
		color: darkred;
		width: 780px;
		text-align: left;
		margin-bottom: 20px;
	}
	.hs_d_bottom_top_right div{
		float: left;
		width: 780px;
		font-size: 14px;
		text-align: left;
		margin-top: 5px;
		font-family: "microsoft yahei";
		color: black;
	}
	.hs_d_bottom .hs_d_bottom_center_line, .hs_d_bottom_center_line2{
		box-sizing: content-box;
		padding: -16px;
		border: none;
		font: normal 13px/1 Verdana, Geneva, sans-serif;
		color: black;
		text-overflow: ellipsis;
		box-shadow: 0 0 2px 1px rgba(0,0,0,0.5) inset;
		transition: all 200ms cubic-bezier(0.6, -0.28, 0.735, 0.04) 10ms;
		height: 10px;
		width: 950px;
		margin-left: 24px;
	}
	.hs_d_bottom_bottom{
		display: inline-block;
		width: 930px;
		/* border-left: 1px solid lightgray; */
		/* border-right: 1px solid lightgray; */
		margin-top: 10px;
		/* height: 1000px; */
	}
	.hs_d_bottom_bottom .hs_d_bottom_bottom_title{
		display: inline-block;
		width: 900px;
		height: 30px;
		text-align: center;
		line-height: 30px;
		margin-top: 8px;
		
	}
	.hs_d_bottom_bottom_title strong{
		font-size: 20px;
		font-weight: 600;
		font-family: "microsoft yahei";
		color: darkred;
	}
	.hs_d_bottom_bottom_msg{
		width: 880px;
		margin: 6px auto;
		text-align: justify;
		text-justify: inter-ideograph;
		line-height: 25px;
		padding-top: 15px;
	}
	.hs_d_bottom_bottom_msg>p{
		background: red !important;
		font-size: 14px;
		line-height: 25px !important;
		font-family: 宋体, 'Lucida Grande', Verdana, Arial, Sans-Serif;
		color: black;
		/* 设置文本段落左右同时对其 */
		text-align: justify !important;
		padding-bottom: 10px;
	}
	p{
		display: block;
		line-height: 25px !important;
		margin-block-start: 1em;
		margin-block-end: 1em;
		margin-inline-start: 0px;
		margin-inline-end: 0px;
	}
	.hs_d_bottom_center_line2{
		margin-top:5px;
		margin-bottom: 5px;
	}
	.hs_d_bottom_bottom_other{
		width: 930px;
		/* border: 1px solid lightgray; */
		height: 50px;
		/* margin-right: 40px; */
		margin-top: 20px;
	}
	.hs_d_bottom_bottom_other div{
		float: right;
		margin-right: 25px;
	}
	.hs_d_bottom_bottom_bottom_line{
		margin-top:5px;
		margin-bottom: 5px;
		box-sizing: content-box;
		padding: -16px;
		border: none;
		font: normal 13px/1 Verdana, Geneva, sans-serif;
		color: black;
		text-overflow: ellipsis;
		box-shadow: 0 0 2px 1px rgba(0,0,0,0.5) inset;
		transition: all 200ms cubic-bezier(0.6, -0.28, 0.735, 0.04) 10ms;
		height: 30px;
		width: 950px;
		margin-left: 24px;
		line-height: 30px;
		font-family: "microsoft yahei";
		color: saddlebrown;
		font-weight: 600;
	}
	.hg_c_bottom_bottom_other{
		width: 930px;
		/* border: 1px solid lightgray; */
		height: 50px;
		margin-top: 20px;
	}
	.hg_c_bottom_bottom_other div{
		float: right;
		margin-right: 25px;
	}
	.hs_d_bottom_bottom_bottom_line_bottom{
		width: 920px;
		overflow: hidden;
		margin: 2px auto;
	}
	.hs_d_bottom_bottom_bottom_line_bottom ul{
		list-style: none;
		padding: 0;
		width: 1000px;
		margin: 7px auto 0;
		overflow: hidden;
		margin-top: 12px;
		margin-left: 80px;
	}
	.hs_d_bottom_bottom_bottom_line_bottom ul li{
		height:30px;
		/* border-bottom:1px solid #ddd; */
		background:url(../../../static/img/dot.gif) left center no-repeat;	
		background-size: 3px 3px;
		margin-left: 100px;
		width: 257px;
		float: left;
	}
	.hs_d_bottom_bottom_bottom_line_bottom ul li a{
		float:left;
		height:30px;			
		font:14px/30px 'Microsoft Yahei';
		text-decoration: none;
		text-indent: 8px;
		transition: all 0.8s cubic-bezier(0.25, 0.1, 0, 1.2);
	}
	.hs_d_bottom_bottom_bottom_line_bottom ul li a:hover{
		color:brown;
		font-size: 15px;
		font-weight: blod;
	}
</style>
