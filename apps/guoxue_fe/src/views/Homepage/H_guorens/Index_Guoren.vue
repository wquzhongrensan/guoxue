<template>
	<div>
		<div class="h_g_nav">
			<el-breadcrumb separator="/">
				<el-breadcrumb-item :to="{ path: '/' }">首页</el-breadcrumb-item>
				<el-breadcrumb-item :to="{ path: '/H_guoren' }">国学人物</el-breadcrumb-item>
			</el-breadcrumb>
		</div>
		
		<div class="h_g_top">
			<img width="1000" height="140" src="../../../static/img/homepage/guowu_国学人物.jpg" alt="">
		</div>
		
		<div class="h_g_left">
			<div class="h_gg_center_msg_l1">
				<div class="h_gg_center_msg_tm">
					<div class="h_gg_center_msg_title"><span>当代人物</span></div>
					<div class="h_gg_center_msg_more"><a href="">更多>></a></div>
				</div>
				<div class="h_gg_center_msg_real" style="background: white;">
					<div v-for="(item, i) in ArticleTypeData_DR_2" :key="i">
						<div class="h_gg_center_msg_real_img">
							<router-link :to="'/H_guoren/HG_person/' + item.id">
								<img width="60" height="70" :src="item.img_link" :alt="item.name">
							</router-link>
						</div>
						<div class="h_gg_center_msg_real_msg">
							<router-link :to="'/H_guoren/HG_person/' + item.id">
								<p>
									<strong style="font-size: 16px;" v-text="item.name"></strong>  {{item.desc}}
								</p>
							</router-link>
						</div>
					</div>
					<ul class="people_name_all">
						<!-- <li v-for="(item, i) in ArticleTypeData_DR_o"><router-link :to="'/H_guoren/HG_person/' + item.id">{{item.name}}</router-link></li> -->
						<li><router-link :to="'/H_guoren/HG_person/' + ArticleTypeData_DR_o[0].id">{{ArticleTypeData_DR_o[0].name}}</router-link></li>
						<li><router-link :to="'/H_guoren/HG_person/' + ArticleTypeData_DR_o[0].id">{{ArticleTypeData_DR_o[0].name}}</router-link></li>
						<li><router-link :to="'/H_guoren/HG_person/' + ArticleTypeData_DR_o[0].id">{{ArticleTypeData_DR_o[0].name}}</router-link></li>
						<li><router-link :to="'/H_guoren/HG_person/' + ArticleTypeData_DR_o[0].id">{{ArticleTypeData_DR_o[0].name}}</router-link></li>
						<li><router-link :to="'/H_guoren/HG_person/' + ArticleTypeData_DR_o[0].id">{{ArticleTypeData_DR_o[0].name}}</router-link></li>
						<li><router-link :to="'/H_guoren/HG_person/' + ArticleTypeData_DR_o[0].id">{{ArticleTypeData_DR_o[0].name}}</router-link></li>
						<li><router-link :to="'/H_guoren/HG_person/' + ArticleTypeData_DR_o[0].id">{{ArticleTypeData_DR_o[0].name}}</router-link></li>
						<li><router-link :to="'/H_guoren/HG_person/' + ArticleTypeData_DR_o[0].id">{{ArticleTypeData_DR_o[0].name}}</router-link></li>
						<li><router-link :to="'/H_guoren/HG_person/' + ArticleTypeData_DR_o[0].id">{{ArticleTypeData_DR_o[0].name}}</router-link></li>
						<li><router-link :to="'/H_guoren/HG_person/' + ArticleTypeData_DR_o[0].id">{{ArticleTypeData_DR_o[0].name}}</router-link></li>
						<li><router-link :to="'/H_guoren/HG_person/' + ArticleTypeData_DR_o[0].id">{{ArticleTypeData_DR_o[0].name}}</router-link></li>
						<li><router-link :to="'/H_guoren/HG_person/' + ArticleTypeData_DR_o[0].id">{{ArticleTypeData_DR_o[0].name}}</router-link></li>
						<li><router-link :to="'/H_guoren/HG_person/' + ArticleTypeData_DR_o[0].id">{{ArticleTypeData_DR_o[0].name}}</router-link></li>
						<li><router-link :to="'/H_guoren/HG_person/' + ArticleTypeData_DR_o[0].id">{{ArticleTypeData_DR_o[0].name}}</router-link></li>
						<li><router-link :to="'/H_guoren/HG_person/' + ArticleTypeData_DR_o[0].id">{{ArticleTypeData_DR_o[0].name}}</router-link></li>
						<li><router-link :to="'/H_guoren/HG_person/' + ArticleTypeData_DR_o[0].id">{{ArticleTypeData_DR_o[0].name}}</router-link></li>
						<li><router-link :to="'/H_guoren/HG_person/' + ArticleTypeData_DR_o[0].id">{{ArticleTypeData_DR_o[0].name}}</router-link></li>
						<li><router-link :to="'/H_guoren/HG_person/' + ArticleTypeData_DR_o[0].id">{{ArticleTypeData_DR_o[0].name}}</router-link></li>
						<li><router-link :to="'/H_guoren/HG_person/' + ArticleTypeData_DR_o[0].id">{{ArticleTypeData_DR_o[0].name}}</router-link></li>
						<li><router-link :to="'/H_guoren/HG_person/' + ArticleTypeData_DR_o[0].id">{{ArticleTypeData_DR_o[0].name}}</router-link></li>
						<li><router-link :to="'/H_guoren/HG_person/' + ArticleTypeData_DR_o[0].id">{{ArticleTypeData_DR_o[0].name}}</router-link></li>
						<li><router-link :to="'/H_guoren/HG_person/' + ArticleTypeData_DR_o[0].id">{{ArticleTypeData_DR_o[0].name}}</router-link></li>
						<li><router-link :to="'/H_guoren/HG_person/' + ArticleTypeData_DR_o[0].id">{{ArticleTypeData_DR_o[0].name}}</router-link></li>
						<li><router-link :to="'/H_guoren/HG_person/' + ArticleTypeData_DR_o[0].id">{{ArticleTypeData_DR_o[0].name}}</router-link></li>
					</ul>
				</div>
			</div>
			
			<div class="h_gg_center_msg_l1">
				<div class="h_gg_center_msg_tm">
					<div class="h_gg_center_msg_title"><span>近现代人物</span></div>
					<div class="h_gg_center_msg_more"><a href="">更多>></a></div>
				</div>
				<div class="h_gg_center_msg_real" style="background: white;">
					<div v-for="(item, i) in ArticleTypeData_JR_2" :key="i">
						<div class="h_gg_center_msg_real_img">
							<router-link :to="'/H_guoren/HG_person/' + item.id">
								<img width="60" height="70" :src="item.img_link" :alt="item.name">
							</router-link>
						</div>
						<div class="h_gg_center_msg_real_msg">
							<router-link :to="'/H_guoren/HG_person/' + item.id">
								<p>
									<strong style="font-size: 16px;" v-text="item.name"></strong>  {{item.desc}}
								</p>
							</router-link>
						</div>
					</div>
					<ul class="people_name_all">
						<li><a href="">曾仕强</a></li>
						<li><a href="">曾仕强</a></li>
						<li><a href="">曾仕强</a></li>
						<li><a href="">曾仕强</a></li>
						<li><a href="">曾仕强</a></li>
						<li><a href="">曾仕强</a></li>
						<li><a href="">曾仕强</a></li>
						<li><a href="">曾仕强</a></li>
						<li><a href="">曾仕强</a></li>
						<li><a href="">曾仕强</a></li>
						<li><a href="">曾仕强</a></li>
						<li><a href="">曾仕强</a></li>
						<li><a href="">曾仕强</a></li>
						<li><a href="">曾仕强</a></li>
						<li><a href="">曾仕强</a></li>
						<li><a href="">曾仕强</a></li>
						<li><a href="">曾仕强</a></li>
						<li><a href="">曾仕强</a></li>
						<li><a href="">曾仕强</a></li>
						<li><a href="">曾仕强</a></li>
						<li><a href="">曾仕强</a></li>
						<li><a href="">曾仕强</a></li>
						<li><a href="">曾仕强</a></li>
						<li><a href="">曾仕强</a></li>
					</ul>
				</div>
			</div>
			<div class="h_gg_center_msg_l1">
				<div class="h_gg_center_msg_tm">
					<div class="h_gg_center_msg_title"><span>古代人物</span></div>
					<div class="h_gg_center_msg_more"><a href="">更多>></a></div>
				</div>
				<div class="h_gg_center_msg_real" style="background: white;">
					<div v-for="(item, i) in ArticleTypeData_GR_2" :key="i">
						<div class="h_gg_center_msg_real_img">
							<router-link :to="'/H_guoren/HG_person/' + item.id">
								<img width="60" height="70" :src="item.img_link" :alt="item.name">
							</router-link>
						</div>
						<div class="h_gg_center_msg_real_msg">
							<router-link :to="'/H_guoren/HG_person/' + item.id">
								<p>
									<strong style="font-size: 16px;" v-text="item.name"></strong>  {{item.desc}}
								</p>
							</router-link>
						</div>
					</div>
					<ul class="people_name_all">
						<li><a href="">曾仕强</a></li>
						<li><a href="">曾仕强</a></li>
						<li><a href="">曾仕强</a></li>
						<li><a href="">曾仕强</a></li>
						<li><a href="">曾仕强</a></li>
						<li><a href="">曾仕强</a></li>
						<li><a href="">曾仕强</a></li>
						<li><a href="">曾仕强</a></li>
						<li><a href="">曾仕强</a></li>
						<li><a href="">曾仕强</a></li>
						<li><a href="">曾仕强</a></li>
						<li><a href="">曾仕强</a></li>
						<li><a href="">曾仕强</a></li>
						<li><a href="">曾仕强</a></li>
						<li><a href="">曾仕强</a></li>
						<li><a href="">曾仕强</a></li>
						<li><a href="">曾仕强</a></li>
						<li><a href="">曾仕强</a></li>
						<li><a href="">曾仕强</a></li>
						<li><a href="">曾仕强</a></li>
						<li><a href="">曾仕强</a></li>
						<li><a href="">曾仕强</a></li>
						<li><a href="">曾仕强</a></li>
						<li><a href="">曾仕强</a></li>
					</ul>
				</div>
			</div>
			
		</div>
		<div class="h_g_right">
			<div class="h_g_right_title">
				人物春秋
			</div>
			<div class="h_g_right_bottom" style="padding-bottom: 18px;border-radius: 14px;background: white;margin-left: 14px;width: 252px;margin-top: 10px;">
				<div class="h_gg_top_1_center_msg">
					<ul>
						<li v-for="(item, i) in ArticleTypeData_FL" :key="i">
							<router-link :to="'/H_guoren/HG_chunqiu/' + item.id">
								{{item.title}}
							</router-link>
						</li>
					</ul>
				</div>
			</div>
		</div>
	</div>
</template>

<script>
	import {
		getArticleTypeMsgs, 
		getGuoRenMsgs,
	} from '@/api/api';
	
	function scroll_to_top(){
		window.scrollTo(0,0);
	}
	export default{
		name: 'Index_Guoren',
		created(){
			scroll_to_top();
			this.getArticleGRDatas(44);
			this.getGuoRenDatas(45);
			this.getGuoRenDatas(46);
			this.getGuoRenDatas(47);
		},
		data(){
			return {
				ArticleTypeData_FL: '',
				ArticleTypeData_GR_2: '',
				ArticleTypeData_GR_o: '',
				ArticleTypeData_JR: '',
				ArticleTypeData_JR_2: '',
				ArticleTypeData_JR_o: '',
				ArticleTypeData_DR: '',
				ArticleTypeData_DR_2: '',
				ArticleTypeData_DR_o: ''

			}
		},
		methods: {
			getArticleGRDatas(id){
				getArticleTypeMsgs({
					id:id
				}).then((response) => {
					if(44 == id){
						this.ArticleTypeData_FL = response.data.article;
					}
				})
				.catch(function (error) {
					console.log(error);
				});
			},
			getGuoRenDatas(id){
				getGuoRenMsgs({
					id:id
				}).then((response) => {
					if(45 == id){
						this.ArticleTypeData_DR_2 = response.data.person.slice(0,2);
						this.ArticleTypeData_DR_o = response.data.person.slice(2,);

					}else if(46 == id){
						this.ArticleTypeData_JR = response.data.person;
						this.ArticleTypeData_JR_2 = response.data.person.slice(0,2);
						this.ArticleTypeData_JR_o = response.data.person.slice(2,);
						
					}else if(47 == id){
						this.ArticleTypeData_GR = response.data.person;
						this.ArticleTypeData_GR_2 = response.data.person.slice(0,2);
						this.ArticleTypeData_GR_o = response.data.person.slice(2,);
						
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
	.h_g_nav{
		margin-top: 3px;
		margin-bottom: 7px;
	}
	.h_g_left{
		width: 708px;
		float: left;
		border-right: 1px dotted lightgray;
		margin-top: 10px;
		height: 1110px;
	}
	
	.h_gg_center_msg_l1{
		float: left;
		margin-left: 14px;
		/* background: goldenrod; */
		width: 670px;
		height: 360px;
		margin-bottom: 20px;
	}
	.h_gg_center_msg_l2{
		float: left;
		margin-right: 14px;
		/* background: gray; */
		width: 670px;
		height: 360px;
		margin-bottom:14px;
	}
	.h_gg_center_msg_r1{
		float: left;
		/* background: saddlebrown; */
		width: 670px;
		height:360px;
		margin-bottom: 14px;
	}
	.h_gg_center_msg_r2{
		float: left;
		width: 670px;
		height:360px;
		margin-bottom: 14px;
	}
	.h_gg_center_msg_tm{
		display: inline-block;
		width: 653px;
		height: 40px;
		/* background: gray; */
		line-height: 34px;
	}
	.h_gg_center_msg_tm {
	  box-sizing: content-box;
	  padding: 9px;
	  border: none;
	  font: normal normal bold 19px/1 "Comic Sans MS", cursive, sans-serif;
	  color: black;
	  text-overflow: ellipsis;
	  background: -webkit-linear-gradient(82deg, rgba(193,186,186,0.7) 0, rgba(193,186,186,0.7) 16%, rgba(255,255,255,1) 100%);
	  background: -moz-linear-gradient(8deg, rgba(193,186,186,0.7) 0, rgba(193,186,186,0.7) 16%, rgba(255,255,255,1) 100%);
	  background: linear-gradient(8deg, rgba(193,186,186,0.7) 0, rgba(193,186,186,0.7) 16%, rgba(255,255,255,1) 100%);
	  background-position: 50% 50%;
	  background-origin: padding-box;
	  background-clip: border-box;
	  background-size: auto auto;
	  text-shadow: -1px -1px 0 rgba(255,255,255,0.2) , 1px 1px 0 rgba(0,0,0,0.25) ;
	  transition: all 200ms cubic-bezier(0.42, 0, 0.58, 1) 10ms, font-size 200ms cubic-bezier(0.42, 0, 0.58, 1) 10ms;
	  height: 22px;
	}
	
	.h_gg_center_msg_l1 .h_gg_center_msg_tm:hover{
		opacity: 0.8;
		color: lightcyan;
	}
	.h_gg_center_msg_r2 .h_gg_center_msg_tm:hover{
		opacity: 0.8;
		color: lightgoldenrodyellow;
	}
	.h_gg_center_msg_tm span{
		display: inline-block;
		float: left;
		margin-left: 10px;
	}
	.h_gg_center_msg_more{
		float: right;
		font-size: 13px;
		font-weight: 100;
		line-height: 28px;
		padding-right: 10px;
		color: black;
		transition: all 0.8 ease;
	}
	.h_gg_center_msg_more:hover{
		color: #000099 !important;
		font-size: 14px;
	}
	.h_gg_center_msg_real{
		width: 670px;
		height: 318px;
		padding: 20px;
		overflow: hidden;
		margin-top: -10px;
		border-radius: 14px;
	}
	.h_gg_center_msg_real div{
		height: 80px;
		border-bottom: 1px dotted lightgray;
		margin-bottom: 6px;
	}
	.h_gg_center_msg_real_img{
		float: left;
		width: 80px;
		height: 80px;
	}
	.h_gg_center_msg_real_msg{
		float: left;
		width: 514px;
		height: 80px;
		text-align: left;
		font-size: 14px;
		margin-left: 10px;
		padding-top: 1px;
		font-family: 宋体, 'Lucida Grande', Verdana, Arial, Sans-Serif !important;
	}
	.h_gg_center_msg_real_msg p{
		margin-top: 5px;
		line-height: 17px;
		font-family: 宋体, 'Lucida Grande', Verdana, Arial, Sans-Serif !important;
	}
	.h_gg_center_msg_real_msg a:hover{
		color: gray;
		text-decoration: none;
	}
	.people_name_all{
		list-style: none;
		display: inline-block;
		margin-top: 7px;
	}
	.people_name_all li{
		float: left;
		width: 83px;
		height: 30px;
		margin-left: 10px;
		margin-right: 10px;
	}
	.people_name_all li a{
		font-size: 14px;
		font-family: "microsoft yahei";
		color: black;
	}
	.people_name_all li a:hover{
		color: #31CAFD;
		text-decoration: none;
	}
	
	.h_g_right{
		width: 270px;
		/* background: orange; */
		margin-left: 5px;
		float: left;
		margin-top: 10px;
	}
	
	.h_g_right_title{
		 box-sizing: content-box;
		 margin: 3px;
		 padding: 11px;
		 border: none;
		 font: normal 25px/1 Verdana, Geneva, sans-serif;
		 color: black;
		 text-overflow: ellipsis;
		 background: linear-gradient(180deg, rgba(255,255,255,1) 0, rgba(241,241,241,1) 50%, rgba(225,225,225,1) 51%, rgba(246,246,246,1) 100%), rgba(239,239,239,1);
		 background-position: 50% 50%;
		 background-origin: padding-box;
		 background-clip: border-box;
		 background-size: auto auto;
		 box-shadow: 5px 5px 8px 2px rgba(0,0,0,0.4) , 0 0 1px 0 rgba(0,0,0,0.5) inset;
		 transition: all 200ms cubic-bezier(0.6, -0.28, 0.735, 0.04) 10ms;
		 margin-left: 13px;
		 margin-top: -1px;
	}
	.h_gg_top_1_center_msg{
		width: 236px;
		overflow: hidden;
	}
	.h_gg_top_1_center_msg ul{
		list-style:none;
		padding:0;
		width:230px;
		margin:7px auto 0;
		overflow: hidden;
		margin-top: 12px;
		margin-left: 10px;
	}
	.h_gg_top_1_center_msg ul li{
		height:30px;
		border-bottom:1px solid #ddd;
		background:url(../../../static/img/dot.gif) left center no-repeat;	
		background-size: 3px 3px;
		margin-left: 10px;
		width: 230px;
		float: left;
	}
	.h_gg_top_1_center_msg ul li a{
		float:left;
		height:30px;			
		font:14px/30px 'Microsoft Yahei';
		text-decoration: none;
		text-indent: 8px;
		transition: all 0.8s cubic-bezier(0.25, 0.1, 0, 1.2);
	}
	.h_gg_top_1_center_msg ul li a:hover{
		color: #31CAFD;
		font-size: 15px;
		font-weight: blod;
	}
</style>
