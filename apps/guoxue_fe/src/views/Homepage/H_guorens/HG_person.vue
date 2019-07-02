<template>
	<div>
		<div class="h_g_nav">
			<el-breadcrumb separator="/">
				<el-breadcrumb-item :to="{ path: '/' }">首页</el-breadcrumb-item>
				<el-breadcrumb-item :to="{ path: '/H_guoren' }">国学人物</el-breadcrumb-item>
				<el-breadcrumb-item :to="{ path: '/H_guoren/HG_person' }">人物介绍</el-breadcrumb-item>
			</el-breadcrumb>
		</div>
		<div class="hg_p_bottom"   v-if="GuorenData">
			<div class="hg_p_bottom_top" style="background: white;">
				<div class="hg_p_bottom_top_left">
					<div>
						<img :src="GuorenData.img_link" :alt="GuorenData.name">
					</div>
				</div>
				<div class="hg_p_bottom_top_right">
					<p>{{GuorenData.name}}</p>
					<div>生卒：{{GuorenData.life_time}}</div>
					<div>籍贯：{{GuorenData.birth_place}}</div>
					<div>简评：{{GuorenData.desc}}</div>
				</div>
			</div>
			<div class="hg_p_bottom_center_line"></div>
			<div class="hg_p_bottom_bottom" style="background: white;">
				<div class="hg_p_bottom_bottom_title">
					<strong>人物生平</strong>
				</div>
				<div class="hg_p_bottom_bottom_msg" v-html="GuorenData.person_content[0].content">
				</div>
				<div class="hg_p_bottom_bottom_other">
					<!-- <div>点击量：<span>{{GuorenData.browse_count}}</span></div> -->
					<!-- <div>发布时间：<span>{{GuorenData.add_time.split("T")[0]}}</span></div> -->
				</div>
			</div>
			<div class="hg_p_bottom_center_line2"></div>
		</div>
		<div v-else style="
			width: 1000px;
			height: 40px;
			line-height: 40px;
			background: white;
			border-radius: 10px;
			margin-top: 10px;
			font-size: 15px;
		">还没有添加相关的数据，请您耐心等待数据的更新，谢谢您的配合</div>
	</div>
	
</template>

<script>
	import {
		getGuoRenDetailMsgs,
	} from '@/api/api';
	
	function scroll_to_top(){
		window.scrollTo(0,0);
	}
	export default{
		name: 'HG_person',
		data(){
			return {
				GuorenData: ''
			}
		},
		methods: {
			getGuoRenDetailDatas(id){
				getGuoRenDetailMsgs({
					id:id
				}).then((response) => {
					this.GuorenData = response.data;
				})
				.catch(function (error) {
					console.log(error);
				});
			},
		},
		created(){
			scroll_to_top();
			this.getGuoRenDetailDatas(this.$route.params.id);
		},
	}
</script>

<style scoped="">
	.h_g_nav{
		margin-top: 4px;
		margin-left: 4px;
		margin-bottom: 7px;
	}
	.hg_p_bottom{
		border-top:1px solid lightgray;
		width: 1000px;
		/* height: 2000px; */
		margin: 0 auto;
	}
	.hg_p_bottom_top{
		width: 932px;
		height: 200px;
		margin: 0px auto;
		margin-top: 15px;
		margin-left: 34px;
		margin-bottom: 10px;
	}
	.hg_p_bottom_top_left{
		float: left;
		width: 130px;
		height: 180px;
		margin-left: 20px;
		margin-top: 11px;
		border: 1px dotted lightgray;
	}
	.hg_p_bottom_top_left:hover{
		border: 1px solid lightgray;
	}
	.hg_p_bottom_top_left div{
		margin: 4px auto;
	}
	.hg_p_bottom_top_right{
		float: right;
		width: 767px;
		height: 200px;
		margin-left: -30px;
	}
	.hg_p_bottom_top_right p{
		float: left;
		margin-top: 33px;
		font-size: 19px;
		font-weight: 580;
		color: darkred;
		width: 780px;
		text-align: left;
		margin-bottom: 20px;
	}
	.hg_p_bottom_top_right div{
		float: left;
		width: 780px;
		font-size: 14px;
		text-align: left;
		margin-top: 5px;
		font-family: "microsoft yahei";
		color: black;
	}
	.hg_p_bottom .hg_p_bottom_center_line, .hg_p_bottom_center_line2{
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
	.hg_p_bottom_bottom{
		display: inline-block;
		width: 930px;
		margin-top: 10px;
	}
	.hg_p_bottom_bottom .hg_p_bottom_bottom_title{
		display: inline-block;
		width: 900px;
		height: 30px;
		text-align: center;
		line-height: 30px;
		margin-top: 8px;
	}
	.hg_p_bottom_bottom_title strong{
		font-size: 17px;
		font-weight: 700;
		font-family: 'microsoft yahei';
		color: black;
	}
	.hg_p_bottom_bottom_msg{
		width: 880px;
		margin: 6px auto;
		text-align: justify;
		line-height: 25px;
	}
	.hg_p_bottom_bottom_msg p{
		font-size: 14px;
		line-height: 25px;
		font-family: 宋体, 'Lucida Grande', Verdana, Arial, Sans-Serif;
		color: black;
		/* 设置文本段落左右同时对其 */
		text-align: justify !important
	}
	p{
		display: block;
		margin-block-start: 1em;
		margin-block-end: 1em;
		margin-inline-start: 0px;
		margin-inline-end: 0px;
	}
	.hg_p_bottom_center_line2{
		margin-top:5px;
		margin-bottom: 5px;
	}
	.hg_p_bottom_bottom_other{
		width: 930px;
		/* border: 1px solid lightgray; */
		height: 50px;
		/* margin-right: 40px; */
		margin-top: 20px;
	}
	.hg_p_bottom_bottom_other div{
		float: right;
		margin-right: 25px;
	}
	
</style>
