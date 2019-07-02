<template>
	<div >
		<!-- <div class="d_dd_nav"> -->
			<!-- <el-breadcrumb separator="/"> -->
				<!-- <el-breadcrumb-item :to="{ path: '/' }">首页</el-breadcrumb-item> -->
				<!-- <el-breadcrumb-item :to="{ path: '/Daodu' }">经典导读</el-breadcrumb-item> -->
			<!-- </el-breadcrumb> -->
		<!-- </div> -->
		
		<div class="d_dd_top">
			<img style="margin-left: -30px;" width="960" height="140" src="../../static/img/经典导读/daodu_top_img.jpg" alt="经典导读">
		</div>
		
		<div class="id_div_left">
			<div class="id_div_left_search">
				<input placeholder="Search" />
			</div>
			<div class="id_div_left_bottom">
				<div class="id_div_left_bottom_title">
					经典导读
				</div>
				<div class="id_div_left_bottom_title1" @click="hide_bottom_nav1">经学经事</div>
				<div class="id_div_left_bottom_title2" v-show="hide_bottom_nav_status1" v-for="(item, i) in d_du_list_jingbu" :key="item.id"><router-link :to="item.link">{{item.name}}</router-link></div>
				
				<div class="id_div_left_bottom_title1" @click="hide_bottom_nav2">史学实录</div>
				<div class="id_div_left_bottom_title2" v-show="hide_bottom_nav_status2" v-for="(item, i) in d_du_list_shibu" :key="item.id"><router-link :to="item.link">{{item.name}}</router-link></div>				
				
				<div class="id_div_left_bottom_title1" @click="hide_bottom_nav3">子学道统</div>
				<div class="id_div_left_bottom_title2" v-show="hide_bottom_nav_status3" v-for="(item, i) in d_du_list_zibu" :key="item.id"><router-link :to="item.link">{{item.name}}</router-link></div>				

				<div class="id_div_left_bottom_title1" @click="hide_bottom_nav4">文学总集</div>
				<div class="id_div_left_bottom_title2" v-show="hide_bottom_nav_status4" v-for="(item, i) in d_du_list_jibu" :key="item.id"><router-link :to="item.link">{{item.name}}</router-link></div>				
			</div>
		</div>
		<transition
		  name="custom-classes-transition"
		  enter-active-class="animated slideInLeft"
		  leave-active-class="animated slideOutRight">
			<router-view></router-view>
		</transition>
	</div>
</template>

<script>
	
	export default{
		name: 'Index_Daodu',
		data(){
			return {
				d_d_list_status1: 1,
				d_d_list_status2: 2,
				d_d_list_status3: 2,
				d_d_list_status4: 2,
				
				hide_bottom_nav_status1: true,
				hide_bottom_nav_status2: false,
				hide_bottom_nav_status3: false,
				hide_bottom_nav_status4: false,
				
				hide_dd_title1_status: true,
				hide_dd_title2_status: true,
				
				d_du_list_jingbu: [
					{
						id: 1,
						name: '小学',
						link:'/Daodu/detail?t=xiaoxue'
					},
					{
						id: 2,
						name: '易类',
						link:'/Daodu/detail?t=yilei'
					},
					{
						id: 3,
						name: '诗类',
						link:'/Daodu/detail?t=shilei'
					},
					{
						id: 4,
						name: '书类',
						link:'/Daodu/detail?t=shulei'
					},
					{
						id: 5,
						name: '礼类',
						link:'/Daodu/detail?t=lilei'
					},
					{
						id: 6,
						name: '春秋',
						link:'/Daodu/detail?t=chunqiu'
					},
					{
						id: 7,
						name: '孝经',
						link:'/Daodu/detail?t=xiaojing'
					},
					{
						id: 8,
						name: '石经',
						link:'/Daodu/detail?t=shijing'
					},
					{
						id: 9,
						name: '五经',
						link:'/Daodu/detail?t=wujing'
					},
					{
						id: 10,
						name: '四书',
						link:'/Daodu/detail?t=sishu'
					},
					{
						id: 11,
						name: '乐类',
						link:'/Daodu/detail?t=yuelei'
					},
					{
						id: 12,
						name: '十三经',
						link:'/Daodu/detail?t=shisanjing'
					},
				],
				d_du_list_shibu: [
					{
						id: 1,
						name: '正史',
						link:'/Daodu/detail?t=zhengshi'
					},
					{
						id: 2,
						name: '编年',
						link:'/Daodu/detail?t=biannian'
					},
					{
						id: 3,
						name: '杂史',
						link:'/Daodu/detail?t=zashi'
					},
					{
						id: 4,
						name: '别史',
						link:'/Daodu/detail?t=bieshi'
					},
					{
						id: 5,
						name: '传记',
						link:'/Daodu/detail?t=zhuanji'
					},
					{
						id: 6,
						name: '载记',
						link:'/Daodu/detail?t=zaiji'
					},
					{
						id: 7,
						name: '地理',
						link:'/Daodu/detail?t=dili'
					},
					{
						id: 8,
						name: '职官',
						link:'/Daodu/detail?t=zhiguan'
					},
					{
						id: 9,
						name: '政书',
						link:'/Daodu/detail?t=zhengshu'
					},
				],
				d_du_list_zibu: [
					{
						id: 1,
						name: '儒家',
						link:'/Daodu/detail?t=rujia'
					},
					{
						id: 2,
						name: '道家',
						link:'/Daodu/detail?t=daojai'
					},
					{
						id: 3,
						name: '法家',
						link:'/Daodu/detail?t=fajia'
					},
					{
						id: 4,
						name: '医家',
						link:'/Daodu/detail?t=yijia'
					},
					{
						id: 5,
						name: '兵家',
						link:'/Daodu/detail?t=bingjia'
					},
					{
						id: 6,
						name: '农家',
						link:'/Daodu/detail?t=nongjia'
					}
				],
				d_du_list_jibu: [
					{
						id: 1,
						name: '楚辞',
						link:'/Daodu/detail?t=chuci'
					},
					{
						id: 2,
						name: '别集',
						link:'/Daodu/detail?t=bieji'
					},
					{
						id: 3,
						name: '总集',
						link:'/Daodu/detail?t=zongji'
					},
					{
						id: 4,
						name: '词曲',
						link:'/Daodu/detail?t=ciqu'
					},
					{
						id: 5,
						name: '元曲',
						link:'/Daodu/detail?t=yuanqu'
					}
				]
				
				
			}
		},
		computed: {
			router_query() {
				return this.$route.query.t;
			}
		},
		methods: {
			hide_bottom_nav1() {
				this.hide_bottom_nav_status1 = !this.hide_bottom_nav_status1;
			},
			hide_bottom_nav2() {
				this.hide_bottom_nav_status2 = !this.hide_bottom_nav_status2;
			},
			hide_bottom_nav3() {
				this.hide_bottom_nav_status3 = !this.hide_bottom_nav_status3;
			},
			hide_bottom_nav4() {
				this.hide_bottom_nav_status4 = !this.hide_bottom_nav_status4;
			},
			
			d_d_hidden_list1() {
				this.d_d_list_status1 = this.d_d_list_status1 + 1;
				if(this.d_d_list_status2 % 2){
					this.d_d_list_status2 = this.d_d_list_status2 - 1;
				}
				if(this.d_d_list_status3 % 2){
					this.d_d_list_status3 = this.d_d_list_status3 - 1;
				}
				if(this.d_d_list_status4 % 2){
					this.d_d_list_status4 = this.d_d_list_status4 - 1;
				}
				if(this.d_d_list_status5 % 2){
					this.d_d_list_status5 = this.d_d_list_status5 - 1;
				}
				if(this.d_d_list_status6 % 2){
					this.d_d_list_status6 = this.d_d_list_status6 - 1;
				}
			},
			d_d_hidden_list2() {
				this.d_d_list_status2 = this.d_d_list_status2 + 1;
				if(this.d_d_list_status1 % 2){
					this.d_d_list_status1 = this.d_d_list_status1 - 1;
				}
				if(this.d_d_list_status3 % 2){
					this.d_d_list_status3 = this.d_d_list_status3 - 1;
				}
				if(this.d_d_list_status4 % 2){
					this.d_d_list_status4 = this.d_d_list_status4 - 1;
				}
				if(this.d_d_list_status5 % 2){
					this.d_d_list_status5 = this.d_d_list_status5 - 1;
				}
				if(this.d_d_list_status6 % 2){
					this.d_d_list_status6 = this.d_d_list_status6 - 1;
				}
			},
			d_d_hidden_list3() {
				this.d_d_list_status3 = this.d_d_list_status3 + 1;
				if(this.d_d_list_status2 % 2){
					this.d_d_list_status2 = this.d_d_list_status2 - 1;
				}
				if(this.d_d_list_status1 % 2){
					this.d_d_list_status1 = this.d_d_list_status1 - 1;
				}
				if(this.d_d_list_status4 % 2){
					this.d_d_list_status4 = this.d_d_list_status4 - 1;
				}
				if(this.d_d_list_status5 % 2){
					this.d_d_list_status5 = this.d_d_list_status5 - 1;
				}
				if(this.d_d_list_status6 % 2){
					this.d_d_list_status6 = this.d_d_list_status6 - 1;
				}
			},
			d_d_hidden_list4() {
				this.d_d_list_status4 = this.d_d_list_status4 + 1;
				if(this.d_d_list_status2 % 2){
					this.d_d_list_status2 = this.d_d_list_status2 - 1;
				}
				if(this.d_d_list_status3 % 2){
					this.d_d_list_status3 = this.d_d_list_status3 - 1;
				}
				if(this.d_d_list_status1 % 2){
					this.d_d_list_status1 = this.d_d_list_status1 - 1;
				}
				if(this.d_d_list_status5 % 2){
					this.d_d_list_status5 = this.d_d_list_status5 - 1;
				}
				if(this.d_d_list_status6 % 2){
					this.d_d_list_status6 = this.d_d_list_status6 - 1;
				}
			},
			hide_dd_title1(){
				this.hide_dd_title1_status = !this.hide_dd_title1_status;
			},
			hide_dd_title2(){
				this.hide_dd_title2_status = !this.hide_dd_title2_status;
			},
		},
	}
</script>

<style scoped="scoped">
	.d_d_left_each{
		margin-top: 20px;
		margin-bottom: 20px;
		margin-left: -20px;
	}
	.dd_search_style{
		width: 1000px;
		height: 59px;
		line-height: 40px;
		margin-top: -6px;
	}
	/* .dd_search_style */
	.d_d_list_ul1 {
		height: 0px !important;
		transition-duration: 1s;
	}
	.d_d_list_ul2 {
		height: 0px !important;
		transition-duration: 1s;
	}
	.d_d_list_ul3 {
		height: 0px !important;
		transition-duration: 1s;
	}
	.d_d_list_ul4 {
		height: 0px !important;
		transition-duration: 1s;
	}
	
	.d_dd_nav{
		float: left;
		margin-top: 3px;
		margin-bottom: 7px;
		line-height: 30px;
	}
	.d_dd_top{
		margin-bottom: 16px;
		margin-left: -10px;
	}
	.d_d_left{
		width: 220px;
		float: left;
		margin-left:10px;
		background-color: #F9F9F9;
		padding-top: 5px;
		background: white;
	}
	.d_d_title1, .d_d_title2{
		margin-bottom: 5px;
		width: 220px;
		float: left;
		height: 40px;
		line-height: 37px;
		font-size: 23px;
		font-family: 华文行楷, 'Lucida Grande', Verdana, Arial, Sans-Serif;
	}
	
	.d_d_title1:hover{
		opacity: 0.7;
		cursor: pointer;
	}
	.d_d_title1{
		display: block;
		box-sizing: content-box;
		float: none;
		z-index: auto;
		width: 198px;
		height: 30px;
		position: static;
		cursor: default;
		opacity: 1;
		margin: 0;
		padding: 11px;
		overflow: visible;
		border: none;
		border-radius: 0;
		font-family: 华文行楷, 'Lucida Grande', Verdana, Arial, Sans-Serif;
		color: black;
		text-overflow: ellipsis;
		background: none;
		box-shadow: 4px 4px 8px 2px rgba(0,0,0,0.2) inset, 1px 1px 4px 0 rgba(0,0,0,0.2) inset;
		text-shadow: 4px 0 9px rgba(86,170,255,0.9) ;
		transition: none;
		transform: none;
		transform-origin: 50% 50% 0;
		line-height: 30px;
		font-size: 24px;
		border-radius: 30px;
	}
	.d_d_title2{
		display: block;
		box-sizing: content-box;
		float: none;
		z-index: auto;
		width: 198px;
		height: 29px;
		position: static;
		cursor: default;
		opacity: 1;
		margin: 0;
		padding: 11px;
		overflow: visible;
		font-family: 华文行楷, 'Lucida Grande', Verdana, Arial, Sans-Serif;
		font-size: 24px;
		color: black;
		text-overflow: ellipsis;
		background: linear-gradient(90deg, rgba(255,255,255,1) 0, rgba(243,243,243,1) 50%, rgba(237,237,237,1) 51%, rgba(255,255,255,1) 100%), linear-gradient(180deg, rgba(219,142,142,0) 0, rgba(255,255,255,0.2) 50%, rgba(255,255,255,0.8) 51%, rgba(255,255,255,0.8) 100%);
		background-position: 50% 50%;
		background-origin: padding-box;
		background-clip: border-box;
		background-size: auto auto;
		box-shadow: 0 0 1px 0 rgba(0,0,0,0.5) , 2px 2px 2px 0 rgba(0,0,0,0.3) ;
		text-shadow: none;
		transition: none;
		transform: none;
		transform-origin: 50% 50% 0;
		line-height: 30px;
		margin-bottom: 4px;
		border-radius: 30px;
	}
	.d_d_title2:hover{
		opacity: 0.7;
		cursor: pointer;
	}
	.dd_title_status{
		margin-left: 10px !important;
	}
	.d_d_left_each{
		float: left;
		width: 175px;
		margin: 0 auto;
		padding-bottom: 9px;
		border-bottom: 1px dotted lightgray;
		margin-top: 20px;
	}
	.d_d_left_eacd_ditle{
		float: left;
		text-align: left;
		margin-left: 10px;
		margin-top: 10px;
		width: 170px;
		font-size: 17px;
		font-weight: 550 !important;
	}
	.d_d_left_eacd_ditle:hover{
		cursor: pointer;
		opacity: 0.6;
		color: #0000FF;
	}
	.d_d_left_each_msg{
		float: left;
		text-align: left;
		margin-left: 15px;
		margin-top: 1px;
	}
	.d_d_top_1_left_bottom{
		width: 277px;
		margin-left: -7px;
		overflow: hidden;
	}
	.d_d_top_1_left_bottom ul{
		list-style:none;
		padding-bottom:10px;
		width:290px;
		margin:7px auto 0;
		overflow: hidden;
		margin-top: 10px;
	}
	.d_d_top_1_left_bottom ul li{
		height:30px;
		background:url(../../static/img/dot.gif) left center no-repeat;	
		background-size: 3px 3px;
		margin-left: 10px;
		width: 153px;
		float: left;
	}
	.d_d_top_1_left_bottom ul li:hover{
		box-shadow: 4px 4px 8px 2px rgba(0,0,0,0.2) ;
		background:#FBFBFB;
	}
	.d_d_top_1_left_bottom ul .d_d_li_style{
		box-shadow: 4px 4px 8px 2px rgba(0,0,0,0.2) ;
	}
	.d_d_top_1_left_bottom ul .d_d_li_style a{
		font-size: 16px !important;
		line-height: 28px;
		color: dodgerblue 	;
		background:#FBFBFB;
	}
	.d_d_top_1_left_bottom ul .d_d_li_style a{
		color: dodgerblue !important;
	}
	.d_d_top_1_left_bottom ul li a{
		float:left;
		height:30px;			
		font:14px/30px 'Microsoft Yahei';
		text-decoration:none;
		color:#000;
		text-indent:8px;
		transition: all 0.8s cubic-bezier(0.25, 0.1, 0, 1.2);
	}
	.d_d_top_1_left_bottom ul li a:hover{
		color:dodgerblue;
		font-size: 15px;
		font-weight: blod;
	}
	.d_search_style {
		float: left;
		height: 28px;
		width: 600px;
	    display: inline-block;
	    box-sizing: content-box;
	    padding: 5px 15px;
	    border: 1px solid #b7b7b7;
	    border-radius: 3px;
	    font: normal 16px/normal "Times New Roman", Times, serif;
	    color: rgba(0,142,198,1);
	    text-overflow: clip;
	    background: rgba(252,252,252,1);
	    box-shadow: 2px 2px 2px 0 rgba(0,0,0,0.2) inset;
	    text-shadow: 1px 1px 0 rgba(255,255,255,0.66) ;
	    transition: all 200ms cubic-bezier(0.42, 0, 0.58, 1);
	    transform: rotateX(-0.5729577951308232deg) rotateY(19.48056503444799deg)   ;
	}
	.d_d_search_2{
		line-height: 37px;
		width: 782px;
		float: right;
		margin-right: 83px;
		margin-top: 30px;
		margin-bottom: 20px;
	}
	.d_search {
		float: left;
		width: 84px;
		color: #fff;
		background: gray;
		height: 39px;
		line-height: 41px;
		margin-left: -19px;
		border-radius: 4px;
		font-size: 17px;
		margin-top: -1px;
	}
	.d_search:hover{
		background-color: gray;
		opacity: 0.8;
	}
	.d_d_bottom_2_right_msg_div{
		float: left;
		width: 177px;
		margin-top:3px;
		margin-left:12px;
		border-bottom: 1px dotted lightgray;
		height: 36px;
	}
	.d_d_bottom_2_right_msg_l{
		float: left;
		width: 25px;
		height: 25px;
		margin-top:5px;
		background: darkgray;
		color: white;
		line-height: 25px;
		font-size: 15px;
		font-weight: blod;
	}
	.d_d_bottom_2_right_msg_r{
		float: left;
		margin-left: 20px;
		margin-top:5px;
		font-size:16px;
		line-height: 25px;
		transform: all 1000ms ease;
	}
	.d_d_bottom_2_right_msg_r a:hover{
		color: darkred;
		text-decoration: none;
		font-size:17px;
	}
	.id_div_left{
		background: white;
		float: left;
		width: 240px;
	    margin-left: 15px;
		padding-bottom: 11px;
		border: 1px solid lightgray;
		border-radius: 10px;
	}
	.id_div_right{
		float: right;
		width: 750px;
		height: 900px;
		border-bottom: 1px solid lightgray;
		border-radius: 10px;
	}
	.id_div_left_search input {
		margin-top: 16px;
	    display: inline-block;
	    box-sizing: content-box;
	    padding: 5px 15px;
	    border: 1px solid #b7b7b7;
	    border-radius: 3px;
	    font: normal 16px/normal "Times New Roman", Times, serif;
	    color: rgba(0,142,198,1);
	    text-overflow: clip;
	    background: rgba(252,252,252,1);
	    box-shadow: 2px 2px 2px 0 rgba(0,0,0,0.2) inset;
	    text-shadow: 1px 1px 0 rgba(255,255,255,0.66) ;
	    transition: all 200ms cubic-bezier(0.42, 0, 0.58, 1);
	    transform: rotateX(-0.5729577951308232deg) rotateY(19.48056503444799deg)   ;
	}
	.id_div_left_bottom{
		margin-top: 10px;
		width: 217px;
		/* height: 1000px; */
		margin-left: 10px;
		/* border: 1px solid gray; */
		/* border-bottom: 2px solid greenyellow !important; */
	}
	.id_div_left_bottom div{
		float: left;
		width: 215px;
		height: 30px;
		border-left: 1px solid lightgray;
		border-right: 1px solid lightgray
	}
	.id_div_left_bottom .id_div_left_bottom_title{
		width: 215px;
		line-height: 38px;
		height: 38px;
		text-align: center;
		font-size: 20px;
		font-weight: 600;
		box-shadow: 5px 5px 8px 2px rgba(0,0,0,0.5) inset;
		font-family:  华文行楷, 'Lucida Grande', Verdana, Arial, Sans-Serif;
	}
	.id_div_left_bottom_title1{
		width: 215px;
		height: 30px;
		background: #E3E3E3;
		opacity: 0.9;
		/* color: white; */
		border-bottom: 1px solid lightgray;
		line-height: 30px;
		font-size: 14px;
		font-family: H-MingLiUC舊字形-98, "Droid Sans Fallback", "Yu Mincho", PMingLiU, FZXiYuan-M01, "Microsoft Yahei", Arial, sans-serif;
		/* font-family: 宋体, 'Lucida Grande', Verdana, Arial, Sans-Serif; */
		box-shadow: 1px 1px 4px 0 rgba(0,0,0,0.2) inset;
		transition: all 0.8s ease;
	}
	.id_div_left_bottom_title1:hover{
		cursor: pointer;
		font-size: 15px;
		opacity: 0.8;
	}
	.id_div_left_bottom_title2{
		width: 215px;
		height: 30px;
		border-bottom: 1px solid lightgray;
		line-height: 30px;
		font-size: 13px;
		/* font-family: 宋体, 'Lucida Grande', Verdana, Arial, Sans-Serif; */
		font-family: H-MingLiUC舊字形-98, "Droid Sans Fallback", "Yu Mincho", PMingLiU, FZXiYuan-M01, "Microsoft Yahei", Arial, sans-serif;
		transition: all 0.8 ease;
	}
	
	.id_div_left_bottom_title2:hover{
		box-shadow: 4px 4px 8px 2px rgba(0,0,0,0.2) ;
		background:#FBFBFB;
	}
	
	
	
	
	
	
	
	
</style>
