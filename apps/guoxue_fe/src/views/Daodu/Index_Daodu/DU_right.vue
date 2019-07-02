<template>
	<div class="d_du_right">
		<div class="d_du_right_title">
			<div class="d_du_right_title_left">
				<strong v-text="d_du_titles"></strong>
				<span>本类别主要讲述的是有关{{d_du_titles}}方面的内容</span>
			</div>
			<!-- <div class="d_du_right_title_right">
				<a href="">更多>></a>				
			</div> -->
		</div>
		<div class="d_du_right_msg" style="background: white;border-radius: 14px;">
			<div class="d_du_center_left_msg">
				<transition
				  name="custom-classes-transition"
				  enter-active-class="animated tada"
				  leave-active-class="animated fadeOutLeft">
				<ul>
					<div v-if="d_du_r_m_msg_lists.length > 0">
						<li v-for="(item,i) in d_du_r_m_msg_lists" :key="i"  class="list-item">
							<div class="du_list_style_div">
								<div class="du_list_style_left">
									<div>
										<router-link :to="'/Daodu/D_detail?id='+item.id"><img width="75" height="95" :src="item.img_link" alt="daodu_易经"></router-link>
									</div>
								</div>
								<div class="du_list_style_right">
									<div class="du_list_style_right_name" style="font-size: 14px;"><router-link :to="'/Daodu/D_detail?id='+item.id">{{item.name}}</router-link></div>
									<div class="du_list_style_right_author"><router-link :to="'/Daodu/D_detail?id='+item.id">{{item.author.name}}</router-link></div>
									<div class="du_list_style_right_jianjie">{{item.desc}}</div>
								</div>
							</div>
						</li>
					</div>
					<div v-if="d_du_r_m_msg_lists.length == 0">
							<div class="du_list_style_div2">
								暂无相关的书籍推荐
							</div>
					</div>
				</ul>
				</transition>
			</div>
			
			<div class="h_s_center_right_msg_bottom_pag_div" v-if="d_du_r_m_msg_lists.length < 0">
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
		getBookTypes,
	} from '@/api/api';
	
	export default{
		name: 'DU_right',
		data(){
			return {
				d_du_title: '',
				d_du_r_m_msg_list: [
				],
			}
		},
		methods: {
			
			getroutedata(){
				// 函数里面获取路由数据
				console.log(this.$route.query.t)
				if(this.$route.query.t == "xiaoxue"|this.d_du_title == ''){
					this.d_du_title = "小学";
					// 下面这一步份就是去通过ajax请求获取数据然后填充数据的
					this.getBookDetailATData(77);
				}
				// else if(this.$route.query.t == "yuanjing"){
// 					this.d_du_title = "原始经济";
// 				}
			},
			getBookDetailATData(id){
				getBookTypes({
					id: id,
				}).then((response) => {
					this.d_du_r_m_msg_list = response.data.book;
				})
				.catch(function (error) {
					console.log(error);
				});
			},
		},
		created(){
			this.getroutedata()
		},
		computed: {
			d_du_r_m_msg_lists(){
				return this.d_du_r_m_msg_list;
			},
			d_du_titles() {
				if(this.$route.query.t == "xiaoxue"|this.d_du_title == ''){
					this.d_du_title = "小学";
					this.getBookDetailATData(77);
					// 下面这一步份就是去通过ajax请求获取数据然后修改数据然后数据驱动视图改变
				}else if(this.$route.query.t == "yilei"){
					this.d_du_title = "易类";
					this.getBookDetailATData(78);
				}else if(this.$route.query.t == "shilei"){
					this.d_du_title = "诗类";
					this.getBookDetailATData(79);

				}else if(this.$route.query.t == "shulei"){
					this.d_du_title = "书类";
					this.getBookDetailATData(80);

				}else if(this.$route.query.t == "lilei"){
					this.d_du_title = "礼类";
					this.getBookDetailATData(81);

				}else if(this.$route.query.t == "chunqiu"){
					this.d_du_title = "春秋";
					this.getBookDetailATData(82);

				}else if(this.$route.query.t == "xiaojing"){
					this.d_du_title = "孝经";
					this.getBookDetailATData(83);

				}else if(this.$route.query.t == "shijing"){
					this.d_du_title = "石经";
					this.getBookDetailATData(84);

				}else if(this.$route.query.t == "wujing"){
					this.d_du_title = "五经";
					this.getBookDetailATData(85);

				}else if(this.$route.query.t == "sishu"){
					this.d_du_title = "四书";
					this.getBookDetailATData(86);

				}else if(this.$route.query.t == "yuelei"){
					this.d_du_title = "乐类";
					this.getBookDetailATData(87);

				}else if(this.$route.query.t == "shisanjing"){
					this.d_du_title = "十三经";
					this.getBookDetailATData(87);

				}else if(this.$route.query.t == "zhengshi"){
					this.d_du_title = "正史";
					this.getBookDetailATData(89);

				}else if(this.$route.query.t == "biannian"){
					this.d_du_title = "编年";
					this.getBookDetailATData(90);

				}else if(this.$route.query.t == "zashi"){
					this.d_du_title = "杂史";
					this.getBookDetailATData(91);

				}else if(this.$route.query.t == "bieshi"){
					this.d_du_title = "别史";
					this.getBookDetailATData(92);

				}else if(this.$route.query.t == "zhuanji"){
					this.d_du_title = "传记";
					this.getBookDetailATData(93);

				}else if(this.$route.query.t == "zaiji"){
					this.d_du_title = "载记";
					this.getBookDetailATData(94);

				}else if(this.$route.query.t == "dili"){
					this.d_du_title = "地理";
					this.getBookDetailATData(95);

				}else if(this.$route.query.t == "zhiguan"){
					this.d_du_title = "职官";
					this.getBookDetailATData(96);

				}else if(this.$route.query.t == "zhengshu"){
					this.d_du_title = "政书";
					this.getBookDetailATData(97);

				}else if(this.$route.query.t == "rujia"){
					this.d_du_title = "儒家";
					this.getBookDetailATData(101);

				}else if(this.$route.query.t == "daojai"){
					this.d_du_title = "道家";
					this.getBookDetailATData(102);

				}else if(this.$route.query.t == "fajia"){
					this.d_du_title = "法家";
					this.getBookDetailATData(103);

				}else if(this.$route.query.t == "yijia"){
					this.d_du_title = "医家";
					this.getBookDetailATData(104);

				}else if(this.$route.query.t == "bingjia"){
					this.d_du_title = "兵家";
					this.getBookDetailATData(105);

				}else if(this.$route.query.t == "nongjia"){
					this.d_du_title = "农家";
					this.getBookDetailATData(106);

				}else if(this.$route.query.t == "chuci"){
					this.d_du_title = "楚辞";
					this.getBookDetailATData(108);

				}else if(this.$route.query.t == "bieji"){
					this.d_du_title = "别集";
					this.getBookDetailATData(109);

				}else if(this.$route.query.t == "zongji"){
					this.d_du_title = "总集";
					this.getBookDetailATData(110);

				}else if(this.$route.query.t == "ciqu"){
					this.d_du_title = "词曲";
					this.getBookDetailATData(111);

				}else if(this.$route.query.t == "yuanqu"){
					this.d_du_title = "元曲";
					this.getBookDetailATData(112);

				}
				
				return this.d_du_title;
			}
		
		},
	}
</script>

<style scoped="scoped">
	.list-item {
	  display: inline-block;
	  margin-right: 7px;
	}
	.list-enter-active, .list-leave-active {
	  transition: all 1s;
	}
	.list-enter, .list-leave-to{
	  opacity: 0;
	  transform: translateY(30px);
	}
	
	.d_du_right{
		width: 710px;
		float: left;
	}
	.d_du_right_title{
		float: left;
		border-radius: 14px;
		width: 670px;
		height: 80px;
		text-align: left;
		margin-left: 20px;
		background: white;
		padding-bottom: 7px;
	}
	.d_du_right_title d_du_right_title_left{
		float: left;
		width: 500px;
		height: 80px;
		
	}
	.d_du_right_title d_du_right_title_right{
		float: right;
		width: 160px;
		height: 80px;
		line-height: 70px;
		
	}
	.d_du_right_title strong{
		font-size: 21px;
		font-weight: normal;
		float: left;
		width: 382px;
		margin-top: 10px;
		height: 30px;
		margin-left: 13px;
		line-height: 30px;
		font-weight: 700;
		font-family: 'Microsoft YaHei','SF Pro Display',Roboto,Noto,Arial,'PingFang SC',sans-serif!important;
	}
	.d_du_right_title span{
		/* color: #000099; */
		font-size:15px !important;
		line-height: 30px;
		margin-left: 13px;
		height: 30px;
		font-weight: normal;
		float: left;
		width: 300px;
		font-family: "Microsoft Yahei", Arial, Helvetica, sans-serif;
	}
	.d_du_right_title a{
		float: right;
		margin-right: 19px;
		margin-top:10px;
	}
	.d_du_right_msg{
		width: 670px;
		margin: 20px auto;
		float: left;
		margin-top: 10px;
		margin-left: 20px;
		overflow: hidden;
		border-right: 1px dotted lightgray;
		border-left: 1px dotted lightgray;
	}
	.d_du_right_msg_each{
		width: 640px;
		height: 100px;
		border-radius: 8px;
		border-right: 1px solid lightgray;
		border-left: 1px solid lightgray;
		margin: 17px;
		float: left
	}
	.d_du_center_left_msg{
		width: 658px;
		overflow: hidden;
	}
	.d_du_center_left_msg ul{
		list-style: none;
		padding: 0;
		width: 658px;
		margin: 7px auto 0;
		overflow: hidden;
		margin-top: 14px;
		margin-left: 15px;
		margin-bottom: 8px;
	}
	.d_du_center_left_msg ul li{
		height: 129px;
		border-radius: 3px;
		background-size: 50px 50px;
		width: 315px;
		background: #F5F5F5;
		line-height: 129px;
		float: left;
		margin-bottom: 7px;
		transition: all 0.8s ease;
	}
	.d_du_center_left_msg ul li:hover{
		box-shadow: 4px 4px 8px 2px rgba(0,0,0,0.2) ;
		background:#FBFBFB;
		opacity: 0.9;
	}
	.d_du_center_left_msg ul li span{
		margin-top: 3px;
	}
	.h_s_center_right_msg_bottom_pag_div{
		width: 640px;
		margin-top: 15px;
		height: 30px;
		float: left;
		margin-left: 220px;
		
	}
	.h_s_center_right_msg_bottom_pag{
		margin: 0 auto;
		line-height: 56px;
		margin-top: -20px;
		margin-left: -49px;
	}
	
	.du_list_style_div{
		width: 315px;
		height: 111px;
		padding-top: 8px;
		padding-top: 8px;
		margin-top: 7px;
		transition: all 0.8s ease;
	}
	.du_list_style_div2{
		width: 630px;
		height: 111px;
		line-height: 100px;
		color: #F0506E;
		background: #FEF4F6;
		text-align: center;
		padding-top: 8px;
		padding-top: 8px;
		margin-top: 7px;
		margin-bottom: 10px;
		transition: all 0.8s ease;
	}
	.du_list_style_div2:hover{
		box-shadow: 4px 4px 8px 2px rgba(0,0,0,0.2) ;
		background:#FAE8ED;
		opacity: 0.9;
	}
	.du_list_style_left{
		float: left;
		height: 110px;
		width: 100px;
		
	}
	.du_list_style_left div{
		width: 80px;
		height: 110px;
		margin: 0 auto;
	}
	.du_list_style_right{
		width: 204px;
		height: 98px;
		float: left;
		margin-top: 3px;
		text-align: left;
		margin-left: 5px;
	}
	.du_list_style_right div{
		float: left;
		width: 188px;
		overflow: hidden;
		text-align: justify;
		font-size: 12px;
		line-height: 16px;
		font-family: H-MingLiUC舊字形-98, "Droid Sans Fallback", "Yu Mincho", PMingLiU, FZXiYuan-M01, "Microsoft Yahei", Arial, sans-serif;
	}
	.du_list_style_right_name, .du_list_style_right_author{
		height: 20px;
		font-family: H-MingLiUC舊字形-98, "Droid Sans Fallback", "Yu Mincho", PMingLiU, FZXiYuan-M01, "Microsoft Yahei", Arial, sans-serif;
	}
	.du_list_style_right_name{
		font-weight: 600;
		font-size: 13px !important;
		/* font:13px/30px 'Microsoft Yahei'; */
		text-decoration: none;
	}
	.du_list_style_right_jianjie{
		height: 51px;
		overflow: hidden;
		margin-top: 3px;
		font-family: H-MingLiUC舊字形-98, "Droid Sans Fallback", "Yu Mincho", PMingLiU, FZXiYuan-M01, "Microsoft Yahei", Arial, sans-serif !important;
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
