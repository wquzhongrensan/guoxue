<template>
	<div class="fl_div">
		<div style="margin-bottom: 10px;margin-left: 5px;">
			<el-breadcrumb separator="/">
				<el-breadcrumb-item :to="{ path: '/Forum' }">论坛首页</el-breadcrumb-item>
				<el-breadcrumb-item :to="{ path: '/Forum/Forum_list' }">板块详情</el-breadcrumb-item>
			</el-breadcrumb>
		</div>
		<div class="fl_div_all">
			<div class="fl_div_left">
				<div class="fl_div_left_search">
					<input placeholder="Search" />
				</div>
				<div class="fl_div_left_bottom">
					<div class="fl_div_left_bottom_title">
						板块导航
					</div>
					
					<div class="fl_div_left_bottom_title1" @click="hide_bottom_nav3">经史子集</div>
					<div class="fl_div_left_bottom_title2" v-show="hide_bottom_nav_status3"><router-link to="/Forum/Forum_list?t=zhewen">哲学文化</router-link></div>
					<div class="fl_div_left_bottom_title2" v-show="hide_bottom_nav_status3"><router-link to="/Forum/Forum_list?t=shiqing">诗词清话</router-link></div>
					<div class="fl_div_left_bottom_title2" v-show="hide_bottom_nav_status3"><router-link to="/Forum/Forum_list?t=jingshi">经济史论</router-link></div>
					<div class="fl_div_left_bottom_title2" v-show="hide_bottom_nav_status3"><router-link to="/Forum/Forum_list?t=guoren">国学人物</router-link></div>
					
					
					<div class="fl_div_left_bottom_title1" @click="hide_bottom_nav1">国学时事</div>
					
					<div class="fl_div_left_bottom_title2" v-show="hide_bottom_nav_status1"><router-link to="/Forum/Forum_list?t=jinguo">今日国学</router-link></div>
					<div class="fl_div_left_bottom_title2" v-show="hide_bottom_nav_status1"><router-link to="/Forum/Forum_list?t=shire">时事热点</router-link></div>
					<div class="fl_div_left_bottom_title2" v-show="hide_bottom_nav_status1"><router-link to="/Forum/Forum_list?t=guozi">国学资讯</router-link></div>
					<div class="fl_div_left_bottom_title2" v-show="hide_bottom_nav_status1"><router-link to="/Forum/Forum_list?t=wenzi">文化自信</router-link></div>

					<div class="fl_div_left_bottom_title1" @click="hide_bottom_nav2">国学典籍</div>
					<div class="fl_div_left_bottom_title2" v-show="hide_bottom_nav_status2"><router-link to="/Forum/Forum_list?t=jingjing">经学经事</router-link></div>
					<div class="fl_div_left_bottom_title2" v-show="hide_bottom_nav_status2"><router-link to="/Forum/Forum_list?t=shishi">史学实录</router-link></div>
					<div class="fl_div_left_bottom_title2" v-show="hide_bottom_nav_status2"><router-link to="/Forum/Forum_list?t=zidao">子学道统</router-link></div>
					<div class="fl_div_left_bottom_title2" v-show="hide_bottom_nav_status2"><router-link to="/Forum/Forum_list?t=wenzong">文学总集</router-link></div>

					
					
					<div class="fl_div_left_bottom_title1" @click="hide_bottom_nav4">礼仪民俗</div>
					<div class="fl_div_left_bottom_title2" v-show="hide_bottom_nav_status4"><router-link to="/Forum/Forum_list?t=mingdian">名人典故</router-link></div>
					<div class="fl_div_left_bottom_title2" v-show="hide_bottom_nav_status4"><router-link to="/Forum/Forum_list?t=baixing">百家姓氏</router-link></div>
					<div class="fl_div_left_bottom_title2" v-show="hide_bottom_nav_status4"><router-link to="/Forum/Forum_list?t=jiefeng">节日风俗</router-link></div>

					<div class="fl_div_left_bottom_title1">琴棋书画</div>
					<div class="fl_div_left_bottom_title1">伦理道德</div>
				</div>
			</div>
			
			<div class="fl_div_right">
				<router-view></router-view>
			</div>
		</div>
	</div>
</template>

<script>
	function scroll_to_top(){
		window.scrollTo(0,0);
	}
	export default{
		name: 'Forum_list',
		data(){
			return{
				hide_bottom_nav_status1: true,
				hide_bottom_nav_status2: true,
				hide_bottom_nav_status3: true,
				hide_bottom_nav_status4: true,
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
			}
		},
		created(){
			scroll_to_top();
		}
	}
</script>

<style scoped="scoped">
	.fl_div{
		width: 100%;
	}
	.fl_div_all{
		width: 1000px;
		
	}
	.fl_div_left{
		background: white;
		float: left;
		width: 240px;
		height: 900px;
		border: 1px solid lightgray;
		border-radius: 10px;
	}
	.fl_div_right{
		float: right;
		width: 750px;
		height: 900px;
		border-bottom: 1px solid lightgray;
		border-radius: 10px;
	}
	.fl_div_left_search input {
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
	.fl_div_left_bottom{
		margin-top: 10px;
		width: 217px;
		/* height: 1000px; */
		margin-left: 10px;
		/* border: 1px solid gray; */
		/* border-bottom: 2px solid greenyellow !important; */
	}
	.fl_div_left_bottom div{
		float: left;
		width: 215px;
		height: 30px;
		border-left: 1px solid lightgray;
		border-right: 1px solid lightgray
	}
	.fl_div_left_bottom .fl_div_left_bottom_title{
		width: 215px;
		line-height: 38px;
		height: 38px;
		text-align: center;
		font-size: 20px;
		font-weight: 600;
		box-shadow: 5px 5px 8px 2px rgba(0,0,0,0.5) inset;
		font-family:  华文行楷, 'Lucida Grande', Verdana, Arial, Sans-Serif;
	}
	.fl_div_left_bottom_title1{
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
	.fl_div_left_bottom_title1:hover{
		cursor: pointer;
		font-size: 15px;
		opacity: 0.8;
	}
	.fl_div_left_bottom_title2{
		width: 215px;
		height: 30px;
		border-bottom: 1px solid lightgray;
		line-height: 30px;
		font-size: 13px;
		/* font-family: 宋体, 'Lucida Grande', Verdana, Arial, Sans-Serif; */
		font-family: H-MingLiUC舊字形-98, "Droid Sans Fallback", "Yu Mincho", PMingLiU, FZXiYuan-M01, "Microsoft Yahei", Arial, sans-serif;
		transition: all 0.8 ease;
	}
	
	.fl_div_left_bottom_title2:hover{
		box-shadow: 4px 4px 8px 2px rgba(0,0,0,0.2) ;
		background:#FBFBFB;
	}
	
	
	
	
</style>
