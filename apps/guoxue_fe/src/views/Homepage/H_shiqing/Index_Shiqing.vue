<template>
	<div>
		<div class="h_s_nav">
			<el-breadcrumb separator="/">
				<el-breadcrumb-item :to="{ path: '/' }">首页</el-breadcrumb-item>
				<el-breadcrumb-item :to="{ path: '/H_shiqing' }">诗词清话</el-breadcrumb-item>
			</el-breadcrumb>
		</div>
		
		<div class="h_s_top">
			<img width="1000" height="140" src="../../../static/img/homepage/shiqing_诗词清话.jpg" alt="诗词清话">
		</div>
		
		<div class="h_s_center">
			<div class="h_s_center_left" style="background: white;">
				<div class="h_s_center_left_title">
					<strong>热门文章</strong>
				</div>
				<div class="h_s_center_left_msg">
					<ul>
						<li v-for="(item, i) in ArticleTypeData_ReS.article" :key="i">
							<router-link :to="'/H_shiqing/HS_detail/' + item.id">
								{{item.title}}
							</router-link>
						</li>
					</ul>
				</div>
				
			</div>
			<div class="h_s_center_right">
				<div class="h_s_center_right_title">
					<strong>诗词清话</strong>
				</div>
				<div class="h_s_center_right_msg" style="background: white;">
					<div class="h_s_center_right_msg_tmborder_bottom">
						<div class="h_s_center_right_msg_tm">
							<div class="h_s_center_right_msg_title"><span>唐诗故事</span></div>
						</div>
					</div>
					<div class="h_s_center_right_msg_real">
						<div v-for="(item, i) in ArticleTypeData_TangS.article" :key="i" class="h_s_center_right_msg_real_route">
							<div class="h_ss_top_1_right_talking h_s_center_right_msg_real_route_1">
								<router-link :to="'/H_shiqing/HS_detail/' + item.id">
									<div class="h_ss_top_1_right_talking_2">
										<div class="h_ss_top_1_right_talking_2_div1"><span>{{item.title}}</span></div><br />
										<div class="h_ss_top_1_right_talking_2_div2">
											<span >（发布 {{item.add_time.split("T")[0]}}</span>&nbsp;&nbsp;
											<span>  点击 {{item.browse_count}}）</span>
										</div>
									</div>
								</router-link>
							</div>
							<div class="h_ss_top_1_right_talking h_s_center_right_msg_real_route_2">
								<router-link :to="'/H_shiqing/HS_detail/' + item.id">
									<div class="h_ss_top_1_right_talking_2">
										<div class="h_ss_top_1_right_talking_2_div1"><span>{{item.title}}</span></div><br />
										<div class="h_ss_top_1_right_talking_2_div2">
											<span >（发布 {{item.add_time.split("T")[0]}}</span>&nbsp;&nbsp;
											<span>  点击 {{item.browse_count}}）</span>
										</div>
									</div>
								</router-link>
							</div>
						</div>
					
					</div>
					
					<div class="h_s_center_right_msg_bottom_pag_div">
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
				
				<div class="h_s_center_right_msg" style="background: white;">
					<div class="h_s_center_right_msg_tmborder_bottom">
						<div class="h_s_center_right_msg_tm">
							<div class="h_s_center_right_msg_title"><span>绝句鉴赏</span></div>
						</div>
					</div>
					<div class="h_s_center_right_msg_real">
						<div v-for="(item, i) in ArticleTypeData_JueS.article" :key="i" class="h_s_center_right_msg_real_route">
							<div class="h_ss_top_1_right_talking h_s_center_right_msg_real_route_1">
								<router-link :to="'/H_shiqing/HS_detail/' + item.id">
									<div class="h_ss_top_1_right_talking_2">
										<div class="h_ss_top_1_right_talking_2_div1"><span>{{item.title}}</span></div><br />
										<div class="h_ss_top_1_right_talking_2_div2">
											<span >（发布 {{item.add_time.split("T")[0]}}</span>&nbsp;&nbsp;
											<span>  点击 {{item.browse_count}}）</span>
										</div>
									</div>
								</router-link>
							</div>
							<div class="h_ss_top_1_right_talking h_s_center_right_msg_real_route_2">
								<router-link :to="'/H_shiqing/HS_detail/' + item.id">
									<div class="h_ss_top_1_right_talking_2">
										<div class="h_ss_top_1_right_talking_2_div1"><span>{{item.title}}</span></div><br />
										<div class="h_ss_top_1_right_talking_2_div2">
											<span >（发布 {{item.add_time.split("T")[0]}}</span>&nbsp;&nbsp;
											<span>  点击 {{item.browse_count}}）</span>
										</div>
									</div>
								</router-link>
							</div>
						</div>
											
					</div>
					
					<div class="h_s_center_right_msg_bottom_pag_div">
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
				
				<div class="h_s_center_right_msg" style="background: white;">
					<div class="h_s_center_right_msg_tmborder_bottom">
						<div class="h_s_center_right_msg_tm">
							<div class="h_s_center_right_msg_title"><span>元人小令</span></div>
						</div>
					</div>
					<div class="h_s_center_right_msg_real">
						<div v-for="(item, i) in ArticleTypeData_YuanS.article" :key="i" class="h_s_center_right_msg_real_route">
							<div class="h_ss_top_1_right_talking h_s_center_right_msg_real_route_1">
								<router-link :to="'/H_shiqing/HS_detail/' + item.id">
									<div class="h_ss_top_1_right_talking_2">
										<div class="h_ss_top_1_right_talking_2_div1"><span>{{item.title}}</span></div><br />
										<div class="h_ss_top_1_right_talking_2_div2">
											<span >（发布 {{item.add_time.split("T")[0]}}</span>&nbsp;&nbsp;
											<span>  点击 {{item.browse_count}}）</span>
										</div>
									</div>
								</router-link>
							</div>
							<div class="h_ss_top_1_right_talking h_s_center_right_msg_real_route_2">
								<router-link :to="'/H_shiqing/HS_detail/' + item.id">
									<div class="h_ss_top_1_right_talking_2">
										<div class="h_ss_top_1_right_talking_2_div1"><span>{{item.title}}</span></div><br />
										<div class="h_ss_top_1_right_talking_2_div2">
											<span >（发布 {{item.add_time.split("T")[0]}}</span>&nbsp;&nbsp;
											<span>  点击 {{item.browse_count}}）</span>
										</div>
									</div>
								</router-link>
							</div>
						</div>
											
					</div>
					
					<div class="h_s_center_right_msg_bottom_pag_div">
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
				
				<div class="h_s_center_right_msg" style="background: white;">
					<div class="h_s_center_right_msg_tmborder_bottom">
						<div class="h_s_center_right_msg_tm">
							<div class="h_s_center_right_msg_title"><span>天下楹联</span></div>
						</div>
					</div>
					<div class="h_s_center_right_msg_real">
						<div v-for="(item, i) in ArticleTypeData_TianS.article" :key="i" class="h_s_center_right_msg_real_route">
							<div class="h_ss_top_1_right_talking h_s_center_right_msg_real_route_1">
								<router-link :to="'/H_shiqing/HS_detail/' + item.id">
									<div class="h_ss_top_1_right_talking_2">
										<div class="h_ss_top_1_right_talking_2_div1"><span>{{item.title}}</span></div><br />
										<div class="h_ss_top_1_right_talking_2_div2">
											<span >（发布 {{item.add_time.split("T")[0]}}</span>&nbsp;&nbsp;
											<span>  点击 {{item.browse_count}}）</span>
										</div>
									</div>
								</router-link>
							</div>
							<div class="h_ss_top_1_right_talking h_s_center_right_msg_real_route_2">
								<router-link :to="'/H_shiqing/HS_detail/' + item.id">
									<div class="h_ss_top_1_right_talking_2">
										<div class="h_ss_top_1_right_talking_2_div1"><span>{{item.title}}</span></div><br />
										<div class="h_ss_top_1_right_talking_2_div2">
											<span >（发布 {{item.add_time.split("T")[0]}}</span>&nbsp;&nbsp;
											<span>  点击 {{item.browse_count}}）</span>
										</div>
									</div>
								</router-link>
							</div>
						</div>
											
					</div>
					
					<div class="h_s_center_right_msg_bottom_pag_div">
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
			
		</div>
	</div>
</template>

<script>
	import {
		getArticleTypeMsgs, 
	} from '@/api/api';
	
	function scroll_to_top(){
		window.scrollTo(0,0);
	}
	export default{
		name: 'Index_Shiqing',
		created(){
			scroll_to_top();
			this.getArticleSQDatas(2);
			this.getArticleSQDatas(3);
			this.getArticleSQDatas(4);
			this.getArticleSQDatas(5);
			this.getArticleSQDatas(6);
		},
		data(){
			return {
				// 获取唐诗故事、绝句鉴赏、元人小令、天下楹联、热门文章的信息
				ArticleTypeData_TangS: '',
				ArticleTypeData_JueS: '',
				ArticleTypeData_YuanS: '',
				ArticleTypeData_TianS: '',
				ArticleTypeData_ReS: '',
			}
		},
		methods: {
			getArticleSQDatas(id){
				getArticleTypeMsgs({
					id:id
				}).then((response) => {
					if(2 == id){
						this.ArticleTypeData_TangS = response.data;
					}else if(3 == id){
						this.ArticleTypeData_JueS = response.data;
					}else if(4 == id){
						this.ArticleTypeData_YuanS = response.data;
					}else if(5 == id){
						this.ArticleTypeData_TianS = response.data;
					}else if(6 == id){
						this.ArticleTypeData_ReS = response.data;
					}
				})
				.catch(function (error) {
					console.log(error);
				});
			},
		}
	}
</script>

<style scoped="scoped">
	.h_s_nav{
		margin-top: 3px;
		margin-bottom: 7px;
	}
	.h_s_center{
		width: 978px;
		margin: 10px auto;
		/* border: 1px solid lightgray; */
	}
	.h_s_center_left{
		float: left;
		width: 300px;
		border-top: 5px solid firebrick;
		margin-bottom: 4px;
	}
	.h_s_center_left_title{
		margin-top: 10px;
	}
	.h_s_center_left_title strong{
		font-size: 25px;
		color: indianred;
		font-family:  华文行楷, 'Lucida Grande', Verdana, Arial, Sans-Serif;
	}
	.h_s_center_left_msg{
		width: 267px;
		overflow: hidden;
		margin-bottom: 15px;
	}
	.h_s_center_left_msg ul{
		list-style:none;
		padding:0;
		width:257px;
		margin:7px auto 0;
		overflow: hidden;
		margin-top: 12px;
		margin-left: 10px;
	}
	.h_s_center_left_msg ul li{
		height:30px;
		border-bottom:1px solid #ddd;
		background:url(../../../static/img/dot.gif) left center no-repeat;	
		background-size: 3px 3px;
		margin-left: 10px;
		width: 257px;
		float: left;
	}
	.h_s_center_left_msg ul li a{
		float:left;
		height:30px;			
		font:14px/30px 'Microsoft Yahei';
		text-decoration: none;
		text-indent: 8px;
		transition: all 0.8s cubic-bezier(0.25, 0.1, 0, 1.2);
	}
	.h_s_center_left_msg ul li a:hover{
		color:indianred;
		font-size: 15px;
		font-weight: blod;
	}
	.h_s_center_right{
		/* border: 1px solid lightgray; */
		float: right;
		width: 660px;
	}
	.h_s_center_right_title{
		display: block;
		box-sizing: content-box;
		float: none;
		z-index: auto;
		width: auto;
		height: auto;
		position: static;
		cursor: default;
		opacity: 1;
		margin: 0;
		padding: 18px;
		overflow: visible;
		border: none;
		border-radius: 0;
		font: normal 16px/1 Arial, Helvetica, sans-serif;
		color: black;
		text-overflow: ellipsis;
		background: linear-gradient(90deg, rgba(255,255,255,0) 0, rgba(255,255,255,0.2) 50%, rgba(255,255,255,0.8) 51%, rgba(255,255,255,0.8) 100%);
		background-position: 50% 50%;
		background-origin: padding-box;
		background-clip: border-box;
		background-size: auto auto;
		box-shadow: 5px 5px 8px 2px rgba(0,0,0,0.5) inset, 2px 2px 2px 0 rgba(0,0,0,0.5) inset;
		text-shadow: none;
		transition: none;
		transform: none;
		transform-origin: 50% 50% 0;
		border-radius: 10px;
	}
	.h_s_center_right_title strong{
		font-size: 22px;
		font-family:  宋体, 'Lucida Grande', Verdana, Arial, Sans-Serif;
	}
	.h_s_center_right_msg{
		float: left;
		margin-left: 16px;
		width: 630px;
		height: 401px;
		margin-bottom: 20px;
		margin-top: 9px;
		/* border: 1px solid lightgray; */
		border-radius: 20px;
	}
	.h_s_center_right_msg_tmborder_bottom{
		/* display: inline-block; */
		width: 119px;
		height: 43px;
		/* border-bottom: 1px solid lightgray; */
		float: left;
		margin-left: 5px;
		margin-top: 4px;
		
	}
	.h_s_center_right_msg_tm{
		margin-top:4px;
		display: inline-block;
		width: 100px;
		height: 40px;
		line-height: 34px;
	}
	.h_s_center_right_msg_tm {
		box-sizing: content-box;
		padding: 9px;
		border: none;
		font: normal normal bold 19px/1 "Comic Sans MS", cursive, sans-serif;
		color: black;
		text-overflow: ellipsis;
		background: linear-gradient(8deg, rgba(193,186,186,0.7) 0, rgba(193,186,186,0.7) 16%, rgba(255,255,255,1) 100%);
		background-position: 50% 50%;
		background-origin: padding-box;
		background-clip: border-box;
		background-size: auto auto;
		text-shadow: -1px -1px 0 rgba(255,255,255,0.2) , 1px 1px 0 rgba(0,0,0,0.25) ;
		height: 22px;
		border-radius: 23px;
		margin-top: 6px;
	}
	
	
	.h_s_center_right_msg_tm span{
		display: inline-block;
		float: left;
		margin-left: 10px;
	}
	.h_s_center_right_msg_real{
		width: 618px;
		height: 291px;
		/* border-right: 1px solid lightgray; */
		/* border-left: 1px solid lightgray; */
		margin-left: 5px;
		float: left;
		margin-top: 8px;
		overflow: hidden;
	}
	.h_s_center_right_msg_real_route{
		width: 300px;
		margin-right: 4px;
		margin-left: 4px;
		margin-top: 4px;
		margin-bottom:4px;
		line-height: 65px;
		height: 65px;
		float: left;
		border: 1px dotted lightgray;
	}
	.h_ss_top_1_right_talking{
		margin-top: -2px;
		margin-left: -2px;
		width: 300px;
		line-height: 65px;
		height: 65px;
		
	}
	.h_ss_top_1_right_talking div{
		display: inline-block;
		height: 57px;
	}
	.h_ss_top_1_right_talking_1{
		float: left;
		margin-top: 7px;
		margin-left: 10px;
	}
	.h_ss_top_1_right_talking_2{
		float: left;
		margin-left: 8px;	
		line-height: 30px;
	}
	.h_ss_top_1_right_talking_2 div{
		float: left;
		height: 10px;
	}
	.h_ss_top_1_right_talking_2_div1{
		font-size: 15px;
		font-weight: 400;
		margin-top:5px;
	}
	.h_ss_top_1_right_talking a{
		display: inline-block;
		width: 290px;
	}
	.h_ss_top_1_right_talking:hover{
		
		border: 1px solid lightgray;
	}
	.h_ss_top_1_right_talking_2_div2{
		margin-left: -10px;
	}
	
	/* h_s_center_right_msg_real_router */
	.h_s_center_right_msg_real_route{
		margin-top: 3px;
		position:relative;			
		transform-style:preserve-3d;
		transform:perspective(800px) rotateY(0deg);
	}
	.h_s_center_right_msg_real_route_1,.h_s_center_right_msg_real_route_2{
		position:absolute;
		left:0;
		top:0;
		backface-visibility:hidden;
		transform:perspective(800px) rotateX(0deg);
		transition:all 500ms ease;
	}
	.h_s_center_right_msg_real_route_2{
		transform:translateZ(2px) rotateX(180deg);
	}
	
	.h_s_center_right_msg_real_route:hover .h_s_center_right_msg_real_route_1{
		background: lightgray;
		opacity: 0.7;
		transform:perspective(800px) rotateX(180deg);
	}
	
	.h_s_center_right_msg_real_route:hover .h_s_center_right_msg_real_route_2{
		background: lightgray;
		opacity: 0.7;
		transform:perspective(800px) rotateX(0deg);
	}
	.h_s_center_right_msg_bottom_pag_div{
		width: 618px;
		/* margin-top: -72px; */
		height: 30px;
		float: left;
		margin-left: 147px;
	}
	.h_s_center_right_msg_bottom_pag{
		
		/* margin-left: 211px; */
		margin: 0 auto;
		/* margin-bottom: 0px; */
		line-height: 56px;
		
		/* background-color: rgb(245,245,245) !important; */
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
