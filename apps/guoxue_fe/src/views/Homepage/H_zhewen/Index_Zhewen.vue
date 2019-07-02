<template>
	<div>
		<div class="h_z_nav">
			<el-breadcrumb separator="/">
				<el-breadcrumb-item :to="{ path: '/' }">首页</el-breadcrumb-item>
				<el-breadcrumb-item :to="{ path: '/H_zhewen' }">哲学文化</el-breadcrumb-item>
			</el-breadcrumb>
		</div>
		
		<div class="h_z_img">
			<img width="1000" height="140" src="../../../static/img/homepage/shiqing_哲学文化.jpg" alt="哲学文化">
		</div>
		
		<div class="h_z_top">
			<div class="h_z_top_left">
				<div class="h_z_top_left_title" @click="toggle_list">中国哲学</div>
				<div class="h_z_center_right_msg_real">
				<!-- <div class="h_z_center_right_msg_real" style="background: white;"> -->
					<div class="h_z_center_left_msg">
						<transition
						  name="custom-classes-transition"
						  enter-active-class="animated jello"
						  leave-active-class="animated fadeOutUp">
						<ul v-if="isShow" class="ul_list">
							 <li v-for="(item,i) in ArticleTypeData_ZZ.article" :key="i"  class="list-item">
								<router-link :to="'/H_zhewen/HZ_detail/'+item.id">
									{{item.title}}
								</router-link>
								<span>（发布 {{item.add_time.split("T")[0]}} 点击 {{item.browse_count}}）</span>
							</li>
						</ul>
						</transition>
						<div v-if="isShow" class="h_z_center_right_msg_bottom_pag_div">
							<div class="h_z_center_right_msg_bottom_pag">
								<div class="i_zz_bottom_top1_right_page">
									<div class="i_zz_bottom_top1_right_page_tiao">上一页</div>
									<div class="i_zz_bottom_top1_right_page_num i_zz_bottom_top1_right_page_num_choose">1</div>
									<div class="i_zz_bottom_top1_right_page_num">2</div>
									<div class="i_zz_bottom_top1_right_page_num">3</div>
									<div class="i_zz_bottom_top1_right_page_tiao">下一页</div>
								</div>
							</div>
						</div>
					</div>
				</div>
			</div>
			<div class="h_z_top_left"> 
				<div class="h_z_top_left_title" @click="toggle_list1">科学技术哲学</div>
				<div class="h_z_center_right_msg_real">
					<div class="h_z_center_left_msg">
						<transition
						  name="custom-classes-transition"
						  enter-active-class="animated lightSpeedIn"
						  leave-active-class="animated lightSpeedOut">
						<ul v-if="isShow1" class="ul_list">
							 <li v-for="(item,i) in ArticleTypeData_KZ.article" :key="i"  class="list-item">
								<router-link :to="'/H_zhewen/HZ_detail/'+item.id">
									{{item.title}}
								</router-link>
								<span>（发布 {{item.add_time.split("T")[0]}} 点击 {{item.browse_count}}）</span>
							</li>
						</ul>
						</transition>
						<div v-if="isShow1" class="h_z_center_right_msg_bottom_pag_div">
							<div class="h_z_center_right_msg_bottom_pag">
								<div class="i_zz_bottom_top1_right_page">
									<div class="i_zz_bottom_top1_right_page_tiao">上一页</div>
									<div class="i_zz_bottom_top1_right_page_num i_zz_bottom_top1_right_page_num_choose">1</div>
									<div class="i_zz_bottom_top1_right_page_num">2</div>
									<div class="i_zz_bottom_top1_right_page_num">3</div>
									<div class="i_zz_bottom_top1_right_page_tiao">下一页</div>
								</div>
							</div>
						</div>
					</div>
				</div>

			</div>
			<div class="h_z_top_left">
				<div class="h_z_top_left_title" @click="toggle_list2">马克思主义哲学</div>
				<div class="h_z_center_right_msg_real">
				<!-- <div class="h_z_center_right_msg_real" style="background: white;"> -->
					<div class="h_z_center_left_msg">
						<transition
						  name="custom-classes-transition"
						  enter-active-class="animated bounceInUp"
						  leave-active-class="animated bounceOutDown">
						<ul v-if="isShow2" class="ul_list">
							 <li v-for="(item,i) in ArticleTypeData_ZZ.article" :key="i"  class="list-item">
								<router-link :to="'/H_zhewen/HZ_detail/'+item.id">
									{{item.title}}
								</router-link>
								<span>（发布 {{item.add_time.split("T")[0]}} 点击 {{item.browse_count}}）</span>
							</li>
						</ul>
						</transition>
						<div v-if="isShow2" class="h_z_center_right_msg_bottom_pag_div">
							<div class="h_z_center_right_msg_bottom_pag">
								<div class="i_zz_bottom_top1_right_page">
									<div class="i_zz_bottom_top1_right_page_tiao">上一页</div>
									<div class="i_zz_bottom_top1_right_page_num i_zz_bottom_top1_right_page_num_choose">1</div>
									<div class="i_zz_bottom_top1_right_page_num">2</div>
									<div class="i_zz_bottom_top1_right_page_num">3</div>
									<div class="i_zz_bottom_top1_right_page_tiao">下一页</div>
								</div>
							</div>
						</div>
					</div>
				</div>
			</div>
			<div class="h_z_top_left"> 
				<div class="h_z_top_left_title" @click="toggle_list3">伦理学</div>
				<div class="h_z_center_right_msg_real">
				<!-- <div class="h_z_center_right_msg_real" style="background: white;"> -->
					<div class="h_z_center_left_msg">
						<transition
						  name="custom-classes-transition"
						  enter-active-class="animated jackInTheBox"
						  leave-active-class="animated rollOut">
						<ul v-if="isShow3" class="ul_list">
							 <li v-for="(item,i) in ArticleTypeData_ZZ.article" :key="i"  class="list-item">
								<router-link :to="'/H_zhewen/HZ_detail/'+item.id">
									{{item.title}}
								</router-link>
								<span>（发布 {{item.add_time.split("T")[0]}} 点击 {{item.browse_count}}）</span>
							</li>
						</ul>
						</transition>
						<div v-if="isShow3" class="h_z_center_right_msg_bottom_pag_div">
							<div class="h_z_center_right_msg_bottom_pag">
								<div class="i_zz_bottom_top1_right_page">
									<div class="i_zz_bottom_top1_right_page_tiao">上一页</div>
									<div class="i_zz_bottom_top1_right_page_num i_zz_bottom_top1_right_page_num_choose">1</div>
									<div class="i_zz_bottom_top1_right_page_num">2</div>
									<div class="i_zz_bottom_top1_right_page_num">3</div>
									<div class="i_zz_bottom_top1_right_page_tiao">下一页</div>
								</div>
							</div>
						</div>
					</div>
				</div>
			
			</div>
					
		
		</div>
	</div>
</template>

<script scoped>
	import {
		getArticleTypeMsgs, 
		get_book_jwt_test,
	} from '@/api/api';
	
	
	function scroll_to_top(){
		window.scrollTo(0,0);
	}
	export default{
		name: 'Index_Zhewen',
		created(){
			scroll_to_top();
		},
		data(){
			return {
				zhongguozhexue_status: true,
				isShow: true,
				isShow1: true,
				isShow2: true,
				isShow3: true,
				ij_r_m_msg_list: [
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
				
				// 获取中国哲学、科学技术哲学、马克思主义哲学、伦理学的信息
				ArticleTypeData_ZZ: '',
				ArticleTypeData_KZ: '',
				ArticleTypeData_MZ: '',
				ArticleTypeData_LZ: '',
			}
		},
		methods: {
			toggle_list_hide(){
				this.zhongguozhexue_status = false;
			},
			toggle_list_show(){
				this.zhongguozhexue_status = true;
			},
			toggle_list(){
				this.isShow = !this.isShow;
			},
			toggle_list1(){
				this.isShow1 = !this.isShow1;
			},
			toggle_list2(){
				this.isShow2 = !this.isShow2;
			},
			toggle_list3(){
				this.isShow3 = !this.isShow3;
			},
			getArticleRMDatas(id){
				getArticleTypeMsgs({
					id:id
				}).then((response) => {
					if(8 == id){
						this.ArticleTypeData_ZZ = response.data;
					}else if(9 == id){
						this.ArticleTypeData_KZ = response.data;
					}else if(10 == id){
						this.ArticleTypeData_MZ = response.data;
					}else if(11 == id){
						this.ArticleTypeData_LZ = response.data;
					}
				})
				.catch(function (error) {
					console.log(error);
				});
			},
		},
		created(){
			this.getArticleRMDatas(8);
			this.getArticleRMDatas(9);
			this.getArticleRMDatas(10);
			this.getArticleRMDatas(11);
		}
	}
</script>

<style>
	.h_z_nav{
		margin-top: 3px;
		margin-bottom: 7px;
	}
	.h_z_top{
		width: 960px;
		margin: 1px auto;
		margin-bottom: 350px;
		/* border: 1px solid gray; */
	}
	.h_z_top_left{
		float: left;
		width: 465px;
		/* border: 1px solid gray; */
		margin-right: 14px;
		margin-top: 20px;
		margin-bottom: 10px;
	}
	.h_z_top_left_title{
		line-height: 60px;
		cursor: pointer;
		display: block;
		box-sizing: content-box;
		float: none;
		z-index: auto;
		width: auto;
		height: auto;
		position: static;
		/* cursor: default; */
		opacity: 1;
		margin: 0;
		padding: 15px;
		overflow: visible;
		border: none;
		border-radius: 21px;
		font: normal 16px/1 "Times New Roman", Times, serif;
		color: black;
		text-overflow: ellipsis;
		background: #ecf0f1;
		box-shadow: 0 0 6px 2px rgba(0,0,0,0.5) ;
		text-shadow: none;
		transition: none;
		transform: none;
		transform-origin: 50% 50% 0;
		height: 20px;
		font-size: 26px;
		font-weight: 600px;
		font-family: 华文行楷, 'Lucida Grande', Verdana, Arial, Sans-Serif;
	}
	.h_z_top_left_title:hover{
		opacity: 0.8;
		background: darkgray;
		color: floralwhite;
	}
	.h_z_center_right_msg_real{
		width: 433px;
		border-radius: 14px;
		float: left;
		margin-left:18px;
		margin-top: 10px;
		overflow: hidden;
	}
	.h_z_center_left_msg{
		width: 423px;
		overflow: hidden;
	}
	.h_z_center_left_msg .ul_list{
		list-style:none;
		padding:0;
		width:442px;
		margin:7px auto 0;
		overflow: hidden;
		margin-top: 12px;
		margin-left: -4px;
	}
	.h_z_center_left_msg .ul_list li{
		height:30px;
		border-bottom:1px solid #ddd;
		background:url(../../../static/img/dot.gif) left center no-repeat;	
		background-size: 3px 3px;
		margin-left: 15px;
		width: 408px;
		float: left;
	}
	.ul_list{
		animate-duration: 2s;           //动画持续时间
		animate-delay: 1s;              //动画延迟时间
		animate-iteration-count: 2; 
	}
	
	.h_z_center_left_msg .ul_list li a{
		float:left;
		height:30px;			
		font:14px/30px 'Microsoft Yahei';
		text-decoration: none;
		text-indent: 8px;
		transition: all 0.8s cubic-bezier(0.25, 0.1, 0, 1.2);
	}
	.h_z_center_left_msg .ul_list li a:hover{
		color: dodgerblue;
		font-size: 15px;
		font-weight: blod;
	}
	.h_z_center_left_msg .ul_list li span{
		float: left;
		margin-top: 10px;
		margin-left: -6px;
	}
	.h_z_center_right_msg_bottom_pag_div{
		width: 332px;
		margin-top: 7px;
		height: 30px;
		float: left;
		margin-bottom: 31px;
		margin-left: 100px;
		line-height: 56px;
	}
	.h_z_center_right_msg_bottom_pag{
		
		/* margin-left: 211px; */
		/* margin: 0 auto; */
		/* margin-bottom: 0px; */
		
		
		/* background-color: rgb(245,245,245) !important; */
	}
	.i_zz_bottom_top1 .i_zz_bottom_top1_right_page{
		float: right;
		height: 57px;
		width: 315px;
		/* background: #0000FF; */
		line-height: 57px;
		font-size: 13px;
		font-family: "microsoft sans serif";
	}
	.i_zz_bottom_top1_right_page_count{
		float: left;
		width: 60px;
		height: 45px;
		color: #CCCCCC;
	}
	.i_zz_bottom_top1_right_page_num{
		float: left;
		width: 25px;
		height: 25px;
		line-height: 26px;
		margin-top: 15px;
		margin-left: 2px;
		margin-right: 2px;
	}
	.i_zz_bottom_top1_right_page .i_zz_bottom_top1_right_page_num_choose{
		background: lightgray;
		color: white;
		border-radius: 6px;
	}
	.i_zz_bottom_top1_right_page_num:hover{
		background: lightgray;
		color: white;
		border-radius: 6px;
		cursor: pointer;
	}
	.i_zz_bottom_top1_right_page_tiao{
		float: left;
		height: 45px;
		width: 40px;
		margin-left: 3px;
		margin-right: 10px;
	}
</style>
