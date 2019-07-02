<template>
	<div class="hj_ij_right">
		<div class="hj_ij_right_title">
			<strong v-text="ij_titles"></strong>
			<a href="">更多>></a>
		</div>
		<div class="hj_ij_right_msg" style="background: white;">
			<div class="h_j_center_left_msg">
				<transition
				  name="custom-classes-transition"
				  enter-active-class="animated tada"
				  leave-active-class="animated fadeOutLeft">
				<ul v-if="ArticleTypeDatas.length > 0">
					 <li v-for="(item,i) in ArticleTypeDatas" :key="i"  class="list-item">
						<router-link :to="'/H_jingshi/HJ_detail/' + item.id">
							{{item.title}}
						</router-link>
						<span>（发布 {{item.add_time.split("T")[0]}} 点击 {{item.browse_count}}）</span>
					</li>
				</ul>
				<ul style="height: 30px;font-size:15px;line-height:20px" v-else>暂时还没有<strong>{{ij_title}}</strong>的数据，请您耐心等待数据更新，谢谢您的配合</ul>
				</transition>
			</div>
			
			<div class="h_s_center_right_msg_bottom_pag_div" v-if="ArticleTypeDatas.length > 0">
				<div class="h_s_center_right_msg_bottom_pag">
					<div class="i_ss_bottom_top1_right_page">
						<div class="i_ss_bottom_top1_right_page_count">共5页</div>
						<div class="i_ss_bottom_top1_right_page_tiao">上一页</div>
						<div class="i_ss_bottom_top1_right_page_num i_ss_bottom_top1_right_page_num_choose">1</div>
						<div class="i_ss_bottom_top1_right_page_num">2</div>
						<div class="i_ss_bottom_top1_right_page_num">3</div>
						<div class="i_ss_bottom_top1_right_page_num">4</div>
						<div class="i_ss_bottom_top1_right_page_num">5</div>
						<div class="i_ss_bottom_top1_right_page_tiao">下一页</div>
					</div>
				</div>
			</div>
		</div>
	</div>
</template>

<script>
	import {
		getArticleTypeMsgs, 
	} from '@/api/api';
	
	export default{
		name: 'IJ_Right_Msg',
		data(){
			return {
				ij_title: '',
				ij_r_m_msg_list: [
					{
						id: 1,
						name: '华北旧石器时代向新石器时代过渡时期文化初探',
						time: '2017-09-03',
						count: 123456
					},
					{
						id: 2,
						name: '怎样学写古诗词之炼句',
						time: '2017-09-03',
						count: 123456
					},
					{
						id: 3,
						name: '中国当代儒学“山大学派”的崛起',
						time: '2017-09-03',
						count: 123456
					},
					{
						id: 4,
						name: '捕捉火花——陪苏秉琦先生聊天',
						time: '2017-09-03',
						count: 123456
					},
					{
						id: 5,
						name: '我们该如何阅读资治通鉴？',
						time: '2017-09-03',
						count: 123456
					},
					{
						id: 6,
						name: '资治通鉴',
						time: '2017-09-03',
						count: 123456
					},
					{
						id: 7,
						name: '资治通鉴',
						time: '2017-09-03',
						count: 123456
					},
					{
						id: 8,
						name: '资治通鉴',
						time: '2017-09-03',
						count: 123456
					},
					{
						id: 1,
						name: '资治通鉴',
						time: '2017-09-03',
						count: 123456
					},
					{
						id: 9,
						name: '资治通鉴',
						time: '2017-09-03',
						count: 123456
					},
					{
						id: 10,
						name: '资治通鉴',
						time: '2017-09-03',
						count: 123456
					},
					{
						id: 11,
						name: '资治通鉴',
						time: '2017-09-03',
						count: 123456
					},
					{
						id: 12,
						name: '资治通鉴',
						time: '2017-09-03',
						count: 123456
					},
					{
						id: 12,
						name: '资治通鉴',
						time: '2017-09-03',
						count: 123456
					},
					{
						id: 13,
						name: '资治通鉴',
						time: '2017-09-03',
						count: 123456
					},
					{
						id: 12,
						name: '资治通鉴',
						time: '2017-09-03',
						count: 123456
					},
					{
						id: 15,
						name: '资治通鉴',
						time: '2017-09-03',
						count: 123456
					},
				],
				ij_r_m_msg_list1: [
					{
						id: 1,
						name: '资治通鉴',
						time: '2017-09-03',
						count: 123456
					},
					{
						id: 2,
						name: '怎样学写古诗词之炼句',
						time: '2017-09-03',
						count: 123456
					},
					{
						id: 3,
						name: '中国当代儒学“山大学派”的崛起',
						time: '2017-09-03',
						count: 123456
					},
					{
						id: 4,
						name: '捕捉火花——陪苏秉琦先生聊天',
						time: '2017-09-03',
						count: 123456
					},
					{
						id: 5,
						name: '我们该如何阅读资治通鉴？',
						time: '2017-09-03',
						count: 123456
					},
					{
						id: 6,
						name: '资治通鉴',
						time: '2017-09-03',
						count: 123456
					},
					{
						id: 7,
						name: '资治通鉴',
						time: '2017-09-03',
						count: 123456
					},
					{
						id: 8,
						name: '资治通鉴',
						time: '2017-09-03',
						count: 123456
					},
					{
						id: 1,
						name: '资治通鉴',
						time: '2017-09-03',
						count: 123456
					},
					{
						id: 9,
						name: '资治通鉴',
						time: '2017-09-03',
						count: 123456
					},
					{
						id: 10,
						name: '资治通鉴',
						time: '2017-09-03',
						count: 123456
					},
					{
						id: 11,
						name: '资治通鉴',
						time: '2017-09-03',
						count: 123456
					},
					{
						id: 12,
						name: '资治通鉴',
						time: '2017-09-03',
						count: 123456
					},
					{
						id: 12,
						name: '资治fsdaf通鉴',
						time: '2017-09-03',
						count: 123456
					},
					{
						id: 13,
						name: 'fdsaf',
						time: '2017-09-03',
						count: 123456
					},
					{
						id: 12,
						name: 'fsdfas',
						time: '2017-09-03',
						count: 123456
					},
					{
						id: 15,
						name: '资治通鉴',
						time: '2017-09-03',
						count: 123456
					},
				],
				ArticleTypeDatas: ''
			}
		},
		methods: {
			
			getroutedata(){
				console.log(this.$route.query.t)
				if(this.$route.query.t == "xiantong"|this.ij_title == ''){
					this.ij_title = "先秦通论";
					this.getArticleTypeDatas(14)
				}
			},
			getArticleTypeDatas(id){
				getArticleTypeMsgs({
					id: id,
				}).then((response) => {
					this.ArticleTypeDatas = response.data.article;
				})
				.catch(function (error) {
					console.log(error);
				});
			},
		},
		created(){
			this.getroutedata();
		},
		computed: {
			ij_titles() {
				if(this.$route.query.t == "xiantong"|this.ij_title == ''){
					this.ij_title = "先秦通论";
					this.getArticleTypeDatas(14);
				}else if(this.$route.query.t == "yuanjing"){
					this.ij_title = "原始经济";
					this.getArticleTypeDatas(15);
				}else if(this.$route.query.t == "xiaxi"){
					this.ij_title = "夏商西周";
					this.getArticleTypeDatas(16);
				}else if(this.$route.query.t == "chunzhan"){
					this.ij_title = "春秋战国";
					this.getArticleTypeDatas(17);
				}else if(this.$route.query.t == "hantong"){
					this.ij_title = "汉唐通论";
					this.getArticleTypeDatas(19);
				}else if(this.$route.query.t == "qinqin"){
					this.ij_title = "秦国秦代";
					this.getArticleTypeDatas(20);
				}else if(this.$route.query.t == "weinan"){
					this.ij_title = "魏晋南北朝";
					this.getArticleTypeDatas(21);
				}else if(this.$route.query.t == "suiwu"){
					this.ij_title = "隋唐五代";
					this.getArticleTypeDatas(22);
				}else if(this.$route.query.t == "songtong"){
					this.ij_title = "宋元通论";
					this.getArticleTypeDatas(24);
				}else if(this.$route.query.t == "beinan"){
					this.ij_title = "北宋南宋";
					this.getArticleTypeDatas(25);
				}else if(this.$route.query.t == "liaoxi"){
					this.ij_title = "辽金西夏";
					this.getArticleTypeDatas(26);
				}else if(this.$route.query.t == "mengshi"){
					this.ij_title = "蒙元史论";
					this.getArticleTypeDatas(27);
				}else if(this.$route.query.t == "mingtong"){
					this.ij_title = "明清通论";
					this.getArticleTypeDatas(29);
				}else if(this.$route.query.t == "mingshi"){
					this.ij_title = "明清史论";
					this.getArticleTypeDatas(30);
				}else if(this.$route.query.t == "qingtong"){
					this.ij_title = "清代通论";
					this.getArticleTypeDatas(31);
				}else if(this.$route.query.t == "qingqian"){
					this.ij_title = "清代前期";
					this.getArticleTypeDatas(32);
				}else if(this.$route.query.t == "jintong"){
					this.ij_title = "近代通论";
					this.getArticleTypeDatas(34);
				}else if(this.$route.query.t == "wanshi"){
					this.ij_title = "晚清史论";
					this.getArticleTypeDatas(35);
				}else if(this.$route.query.t == "minshi"){
					this.ij_title = "民国史论";
					this.getArticleTypeDatas(36);
				}else if(this.$route.query.t == "hongqu"){
					this.ij_title = "红色区域";
					this.getArticleTypeDatas(37);
				}else if(this.$route.query.t == "xiantong1"){
					this.ij_title = "现代通论";
					this.getArticleTypeDatas(39);
				}else if(this.$route.query.t == "jianchu"){
					this.ij_title = "建国初期";
					this.getArticleTypeDatas(40);
				}else if(this.$route.query.t == "wenshi"){
					this.ij_title = "文革十年";
					this.getArticleTypeDatas(41);
				}else if(this.$route.query.t == "gaikai"){
					this.ij_title = "改革开放";
					this.getArticleTypeDatas(42);
				}
				
				return this.ij_title;
			}
		},
	}
</script>

<style scoped="scoped">
	.list-item {
	  display: inline-block;
	  margin-right: 10px;
	}
	.list-enter-active, .list-leave-active {
	  transition: all 1s;
	}
	.list-enter, .list-leave-to
	/* .list-leave-active for below version 2.1.8 */ {
	  opacity: 0;
	  transform: translateY(30px);
	}
	
	.hj_ij_right{
		/* height: 1800px; */
		width: 710px;
		float: left;
		margin-left: 4px;
		/* border: 1px solid lightgray; */
		/* border-left: 0px; */
	}
	.hj_ij_right_title{
		float: left;
		width: 670px;
		text-align: left;
		margin-left: 20px;
		border-bottom: 2px solid dodgerblue;
		padding-bottom: 7px;
	}
	.hj_ij_right_title strong{
		/* color: #000099; */
		font-size:21px;
		font-weight: normal;
		float: left;
		font-family: "Microsoft Yahei", Arial, Helvetica, sans-serif;
	}
	.hj_ij_right_title a{
		float: right;
		margin-right: 6px;
		margin-top:10px;
	}
	.hj_ij_right_msg{
		width: 670px;
		border-radius: 14px;
		margin: 20px auto;
		float: left;
		margin-top: 10px;
		margin-left: 20px;
		overflow: hidden;
	}
	.hj_ij_right_msg_each{
		width: 640px;
		height: 100px;
		border-radius: 8px;
		border-right: 1px solid lightgray;
		border-left: 1px solid lightgray;
		margin: 17px;
		float: left
	}
	.h_j_center_left_msg{
		width: 640px;
		overflow: hidden;
	}
	.h_j_center_left_msg ul{
		list-style:none;
		padding:0;
		width:640px;
		margin:7px auto 0;
		overflow: hidden;
		margin-top: 12px;
		margin-left: 10px;
	}
	.h_j_center_left_msg ul li{
		height:30px;
		border-bottom:1px solid #ddd;
		background:url(../../../../static/img/dot.gif) left center no-repeat;	
		background-size: 3px 3px;
		margin-left: 15px;
		width: 640px;
		float: left;
	}
	.h_j_center_left_msg ul li a{
		float:left;
		height:30px;			
		font:14px/30px 'Microsoft Yahei';
		text-decoration: none;
		text-indent: 8px;
		transition: all 0.8s cubic-bezier(0.25, 0.1, 0, 1.2);
	}
	.h_j_center_left_msg ul li a:hover{
		color:dodgerblue;
		font-size: 15px;
		font-weight: blod;
	}
	.h_j_center_left_msg ul li span{
		float: left;
		margin-top: 10px;
	}
	.h_s_center_right_msg_bottom_pag_div{
		width: 640px;
		height: 30px;
		float: left;
		margin-left: 177px;
		line-height: 55px;
		margin-bottom: 20px;
	}
	.h_s_center_right_msg_bottom_pag{
		margin: 0 auto;
	}
	.i_ss_bottom_top1 .i_ss_bottom_top1_right_page{
		float: right;
		height: 57px;
		width: 315px;
		/* background: #0000FF; */
		line-height: 57px;
		font-size: 13px;
		font-family: "microsoft sans serif";
	}
	.i_ss_bottom_top1_right_page_count{
		float: left;
		width: 60px;
		height: 45px;
		color: #CCCCCC;
	}
	.i_ss_bottom_top1_right_page_num{
		float: left;
		width: 25px;
		height: 25px;
		line-height: 26px;
		margin-top: 15px;
		margin-left: 2px;
		margin-right: 2px;
	}
	.i_ss_bottom_top1_right_page .i_ss_bottom_top1_right_page_num_choose{
		background: lightgray;
		color: white;
		border-radius: 6px;
	}
	.i_ss_bottom_top1_right_page_num:hover{
		background: lightgray;
		color: white;
		border-radius: 6px;
		cursor: pointer;
	}
	.i_ss_bottom_top1_right_page_tiao{
		float: left;
		height: 45px;
		width: 40px;
		margin-left: 3px;
		margin-right: 10px;
	}
</style>
