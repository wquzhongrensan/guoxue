<template>
	<div class="fp_all">
		<div style="margin-bottom: 10px;margin-left: 21px;">
			<el-breadcrumb separator="/">
				<el-breadcrumb-item :to="{ path: '/Forum' }">论坛首页</el-breadcrumb-item>
				<el-breadcrumb-item :to="{ path: '/Forum/Forum_publish' }">发帖中</el-breadcrumb-item>
			</el-breadcrumb>
		</div>
		<div class="fp_title_real">
			我要发帖
		</div>
		<div class="fp">
			<div class="fp_title">
				<div class="fp_title_1">
					<div style="border-bottom:1px solid lightgray;margin-top:5px;width:35px;">标题</div>
				</div>
				<div class="fp_title_input_div">
					<input type="text" v-model="title" class="fp_title_input" placeholder="请输入标题">
				</div>
			</div>
			<div class="fp_article">
				<div class="fp_article_1">
					<div style="border-bottom:1px solid lightgray;margin-top:5px;width:35px;">文本</div>
				</div>
				<div class="fp_article_2">
					<div @click="show_edit" :class="{choose_status: edit_status}">编辑</div>
					<div @click="getUEContent" :class="{choose_status: !edit_status}">预览</div>
				</div>
				<div class="fp_article_fuwenben" v-show="edit_status" style="height: auto !important;">
					<UE :defaultMsg=defaultMsg :config=config ref="ue" style="margin-left: 0px;"></UE>
				</div>
				<div class="fp_article_fuwenben" v-show="!edit_status" v-html="contents"  style="height:300px !important;width:700px !important;overflow:auto !important;text-align: left !important;"></div>
				<div class="fp_article_3">
					<div>主题板块</div>
					<div class="fp_article_32">
						<select v-model="forum_type_val" name="fssaf" id="" style="width: 120px; height: 30px;" @change="get_sub_forum">
							<option :value="item.id" v-for="(item, i) in forum_type" :key="i">{{item.title}}</option>
						</select>
					</div>
					<div class="fp_article_32">
						<select v-model="sub_forum_type_val" name="fssaf" id="" style="width: 120px; height: 30px;">
							<option :value="item.id" selected = "selected"  v-for="(item, i) in sub_forum_type" :key="i">{{item.title}}</option>
						</select>
					</div>
				</div>
				<div class="fp_pulish" style="height: 45px;">
					<div @click="publish_forum" class="fp_pulish_button" style="margin-left:12px;width: 76px; height: 80px；line-height：30px; background: darkgray; color: white; padding: 10px 20px; font-size: 16px;">发帖</div>
				</div>
				
			</div>
			<div style="height: 45px;">
			</div>
		</div>
	</div>
</template>

<script>
	import UE from '@/components/UE';
	import { mapState } from 'vuex'
	import {forum_type_msgs, publish_forum_topics} from '@/api/api';

	function scroll_to_top(){
		window.scrollTo(0,0);
	}
	export default{
		name:'Forum_publish',
		components: {
			UE,
		},
		data() {
			return {
				edit_status: true,
				defaultMsg: '发表你的评论吧',
				config: {
					initialFrameWidth: 698,
					initialFrameHeight: 300,
					autoClearinitialContent: true
				},
				forum_type: '',
				sub_forum_type: '',
				forum_type_val: '',  //主分类
				sub_forum_type_val: '',  //次分类
				title: '',   //标题
				content: '',   //内容
			}
		},
		methods: {
			show_edit(){
				this.edit_status = !this.edit_status;
			},
			getUEContent() {
				this.edit_status = !this.edit_status;
				let content = this.$refs.ue.getUEContent();
				this.content = content;
				console.log(this.content);
			},
			get_info(){
				forum_type_msgs({
				}).then((response) => {
					this.forum_type = response.data;
					this.sub_forum_type = this.forum_type[0]["sub_forum"]
				})
				.catch(function (error) {
					console.log(error);
				});
			},
			get_sub_forum(){
				for (var i=0;i<this.forum_type.length;i++)
				{
					if(this.forum_type[i]["id"] == this.forum_type_val){
						this.sub_forum_type = this.forum_type[i]["sub_forum"]
					}
				}
			},
			publish_forum(){
				const _this = this;
				if(confirm("确认提交吗？")){
					publish_forum_topics({
						content: this.$refs.ue.getUEContent(),
						title: this.title,
						forum_type: this.sub_forum_type_val + "",
						author: this.username
					}).then((response) => {
						console.log(response.data)
						_this.$router.push({path: '/Forum/Forum_detail/?id='+response.data.id})
					})
					.catch(function (error) {
						console.log(error);
						alert(error["content"][0])
					});
				}
				
				
				
			}
		},
		computed: {
			contents() {
				return this.content
			},
			...mapState({
					username: state => state.login_status.username,
			}),
		},
		created(){
			this.get_info();
			scroll_to_top();
		}
	}
	
</script>

<style scoped="scoped">
	.fp_all{
		width: 800px;
		float: left;
		margin-left: 100px;
		text-align: center;
		font-family: 'Microsoft YaHei','SF Pro Display',Roboto,Noto,Arial,'PingFang SC',sans-serif!important;
	}
	.fp_title_real{
		font-size: 20px;
		width: 760px;
		float: left;
		height: auto;
		margin-left: 20px;
		height: 40px;
		line-height: 40px;
		border-radius: 8px;
		text-align: center;
		background: darkgray;
		color: white;
		font-family: "microsoft yahei";
	}
	.fp{
		background: white;
		width: 760px;
		float: left;
		height: auto;
		margin-left: 20px;
		/* border: 1px dotted lightgray; */
		text-align: center;
	}
	.fp_title{
		width: 721px;
		float: left;
		height: 85px;
		margin-left: 20px;
		border-top: 1px solid lightgray;
		margin-top: 10px;
	}
	.fp_title div{
		float: left;
		width: 500px;
		height: 28px;
		text-align: left;
		font-size: 16px;
		line-height: 28px;
		margin-bottom: 10px;
		margin-left: 5px;
	}
	
	.fp_title .fp_title_input_div{
		height: 40px !important;
	}
	.fp_title_input{
		display: inline-block;
		box-sizing: content-box;
		float: none;
		z-index: auto;
		width: 400px;
		height: auto;
		position: static;
		cursor: default;
		opacity: 1;
		margin: 0;
		padding: 10px 20px;
		overflow: visible;
		border: 1px solid #b7b7b7;
		border-radius: 3px;
		font: normal 16px/normal "Times New Roman", Times, serif;
		font-family: sans-serif;

		/* color: rgba(0,142,198,1); */
		text-overflow: clip;
		background: linear-gradient(90deg, rgba(255,255,255,0) 0, rgba(255,255,255,1) 100%);
		background-position: 50% 50%;
		background-origin: padding-box;
		background-clip: border-box;
		background-size: auto auto;
		box-shadow: 1px 1px 4px 0 rgba(0,0,0,0.2) , 2px 2px 2px 0 rgba(0,0,0,0.2) inset;
		text-shadow: 1px 1px 0 rgba(255,255,255,0.66) ;
	}
	
	.fp_article{
		width:721px ;
		float: left;
		height: auto;
		margin-left: 20px;
		margin-bottom: 50px;
		border: 1px solid lightgray;
	}
	.fp_article div{
		float: left;
		width: 699px;
		/* height: 28px; */
		text-align: left;
		font-size: 16px;
		line-height: 21px;
		margin-bottom: 10px;
		margin-left: 5px;
	}
	.fp_article .fp_article_fuwenben{
		height: 300px !important;
		line-height: 24px;
		text-align: center;
		margin-top: -10px;
		margin-left: 10px;
		border: 1px solid lightgray;
		margin-bottom: 5px;
	}
	.fp_article .fp_article_fuwenben p{
		font-family: "Times New Roman", Times, serif;
	}
	.fp_article_2{
		float: left;
		width: 500px;
		height: 30px;
	}
	.fp_article_2 div{
		cursor: pointer;
		width: 50px;
		height: 30px;
		text-align: center;
		font-size: 12px;
		line-height: 29px;
		border-top: 1px solid lightgray;
		border-right: 1px solid lightgray;
		border-left: 1px solid lightgray;
	}
	.fp_article_2 .choose_status{
		border-bottom: 2px solid darkgray !important;
	}
	.fp_article .fp_article_3{
		float: left;
		width: 500px;
		height: 30px;
		margin-left: 10px;
	}
	.fp_article_3 div{
		float: left;
		width: 80px;
		line-height: 34px;
		font-size: 13px;
	}
	.fp_article_32{
		width: 120px !important;
		height: 40px !important;
		line-height: 40px !important;
		margin-top: -3px;
	}
	.fp_publish{
		float: left;
		width: 500px;
		height: 40px;
		line-height: 40px;
	}
	
	.fp_publish div{
		margin-left: 20px;
		float: left;
		box-sizing: content-box;
		z-index: auto;
		width: 36px !important;
		height: 20px;
		position: static;
		cursor: pointer;
		opacity: 1;
		margin: 0;
		padding: 10px 20px;
		overflow: visible;
		border: 1px solid #018dc4;
		border-radius: 3px;
		font: normal 16px/normal "Times New Roman", Times, serif;
		color: rgba(255,255,255,0.9);
		text-overflow: clip;
		background: #0199d9 !important;
		box-shadow: 1px 1px 4px 0 rgba(0,0,0,0.2), 2px 2px 2px 0 rgba(173,67,67,0.2);
		text-shadow: -1px -1px 0 rgba(15,73,168,0.66);
		line-height: 19px;
		margin-top: 7px;
		margin-left: 6px;
	}
	.fp_pulish_button:hover{
		cursor: pointer;
	}
</style>
