<template>
	<div class="forum_top_nav_all">
		<div id="head">
			<div id="head_forum_menu">
				<div id="head_forum_menu_body">
					<div id="head_forum_mbR">
						<div >
							<img class="f_img_style" src="../static/img/jiantou.svg" alt="引导">
						</div>
						<ul class="forum_menu_list">
							<li class="f_search_text">
								<div style="width: 170px; height: 20px;	"></div>
							</li>
							<li class="f_li_back1">
								<router-link to="/Forum" :class="{choose_s_s_1: choose_s_1s}">论坛首页</router-link>
								<img v-show="choose_s_1s" src="../static/img/jiantou_up.svg" width="15" height="15" style="position: absolute;left: 38px; top: 23px;" alt="">
							</li>
							<li class="f_li_back1">
								<router-link to="/Forum/Forum_list" :class="{choose_s_s_1: choose_s_2s}">板块详情</router-link>
								<img v-show="choose_s_2s" src="../static/img/jiantou_up.svg" width="15" height="15" style="position: absolute;left: 38px; top: 23px;" alt="">
							</li> 
							<li class="f_li_back1">
								<router-link to="/Forum/Forum_sort" :class="{choose_s_s_1: choose_s_3s}">荣誉榜</router-link>
								<img v-show="choose_s_3s" src="../static/img/jiantou_up.svg" width="15" height="15" style="position: absolute;left: 38px; top: 23px;" alt="">
							</li> 
							<li class="f_li_back4">
								<router-link to="/Forum/Forum_publish" :class="{choose_s_s_2: choose_s_4s}">我要发帖</router-link>
								<img v-show="choose_s_4s" src="../static/img/jiantou_up.svg" width="15" height="15" style="position: absolute;left: 38px; top: 23px;" alt="">
							</li>
						</ul>
					</div>
				</div>
			</div>
		</div>
	</div>
</template>
<script>
	export default{
		name: 'Sub_nav_forum',
		data() {
			return {
				choose_s_1: true,
				choose_s_2: false,
				choose_s_3: false,
				choose_s_4: false,
			}
		},
		created(){
			this.get_route_query();
		},
		methods: {
			get_route_query(){
				this.route_data = this.$route.fullPath.split("/")[2];
				if(this.route_data == "Forum_list"){
					this.choose_s_1 = false;
					this.choose_s_2 = true;
					this.choose_s_3 = false;
					this.choose_s_4 = false;
				}else if(this.route_data == "Forum_sort"){
					this.choose_s_1 = false;
					this.choose_s_2 = false;
					this.choose_s_3 = true;
					this.choose_s_4 = false;
				}else if(this.route_data == "Forum_publish"){
					this.choose_s_1 = false;
					this.choose_s_2 = false;
					this.choose_s_3 = false;
					this.choose_s_4 = false;
				}else{
					this.choose_s_1 = true;
					this.choose_s_2 = false;
					this.choose_s_3 = false;
					this.choose_s_4 = false;
				}
			}
		},
		computed: {
			choose_s_1s(){
				if(this.$route.fullPath == "/Forum"){
					this.choose_s_1 = true;
					this.choose_s_2 = false;
					this.choose_s_3 = false;
					this.choose_s_4 = false;
				}
				return this.choose_s_1
			},
			choose_s_2s(){
				if(this.$route.fullPath.split("/")[2] == "Forum_list"){
					this.choose_s_1 = false;
					this.choose_s_2 = true;
					this.choose_s_3 = false;
					this.choose_s_4 = false;
				}
				return this.choose_s_2
			},
			choose_s_3s(){
				if(this.$route.fullPath.split("/")[2] == "Forum_sort"){
					this.choose_s_1 = false;
					this.choose_s_2 = false;
					this.choose_s_3 = true;
					this.choose_s_4 = false;
				}
				return this.choose_s_3
			},
			choose_s_4s(){
				if(this.$route.fullPath.split("/")[2] == "Forum_publish"){
					this.choose_s_1 = false;
					this.choose_s_2 = false;
					this.choose_s_3 = false;
					this.choose_s_4 = true;
				}
				return this.choose_s_4
			},
			
		},
			
	}
</script>

<style scoped="scoped">

	.forum_top_nav_all{
		background-color: lightslategray;
		opacity: 0.8;
		height: 34px;
	}

	.f_little_jiantou {
		display: block;
		position: absolute;
		left: 50%;
		top: 28px;
		width: 12px;
		height: 7px;
		margin-left: -6px;
		overflow: hidden;
		background-position: -226px 0;
		background-color: yellow;
	}
	.f_img_style{
		width:25px;
		position: absolute;
		top:-15px;
		left:264px;
	}
	.f_li_back a{
		display: block;
		height: 22px;
		line-height: 22px;
		width: 39px;
		border-radius: 5px;
		margin-top: 7px;
		font-size: 13px;
		color: white;
	}
	.f_li_back a:hover{
		background: #4D7E9B !important;
		text-decoration: none !important;
		opacity: 0.9 !important;
	}
	.choose_s_s_1{
		text-decoration: none !important;
		border-bottom: 2px solid #054B79;
		border-radius: 0px !important;
		margin-top: 0px !important;
		height: 34px !important;
		line-height: 34px !important;
	}
	.choose_s_s_2{
		text-decoration: none !important;
		border-bottom: 2px solid #054B79;
		border-radius: 0px !important;
		margin-top: 0px !important;
		height: 34px !important;
		line-height: 34px !important;
		background: none !important;
	}
	.f_li_back1,.f_li_back4{
		position: relative;
	}
	.f_li_back1 a{
		display: block;
		height: 22px;
		line-height: 22px;
		width: 73px;
		border-radius: 5px;
		margin-top: 7px;
		font-size: 13px;
		color: white;
	}
	.f_li_back1 a:hover{
		background: #86AABF !important;
		text-decoration: none !important;
		border-bottom: 2px solid #054B79;
		border-radius: 0px !important;
		margin-top: 0px !important;
		height: 34px !important;
		line-height: 34px !important;
	}
	.f_li_back4 a{
		display: block;
		height: 34px;
		line-height: 34px;
		width: 73px;
		border-radius: 5px;
		font-size: 13px;
		color: white;
		background: #054B79;
	}
	.f_li_back4 a:hover{
		background: #86AABF !important;
		text-decoration: none !important;
		border-bottom: 2px solid #054B79;
		border-radius: 0px !important;
		margin-top: 0px !important;
		height: 34px !important;
		line-height: 34px !important;
	}
	.f_search_2{
		line-height: 35px;
	}
	.f_search {
		color: #fff;
		background-color: gray;
		height: 31px;
		margin-top: 15px;
		line-height: 31px;
		margin-left: -7px;
		width: 45px;
		border-radius: 4px;
	}
	.f_search:hover{
		background-color: gray;
		opacity: 0.8;
	}
	#head {
		color: #fff;
	    height: 35px;
	    width: 100%;
	    background-position: center;
		text-align: center;
		font-size: 13px;
		line-height: 35px;
		
	}
	.fl {
	    float: left;
	}
	#head_forum_menu {
	    height: 35px;
	    width: 100%;
	    background-color: rgba(255, 255, 255, 0.4);
	}
	#head_forum_menu_body {
	    height: 35px;
	    width: 1200px;
	    margin: 0 auto;
	    position: relative;
	}
	#head_forum_mbR {
		position: relative;
		margin-left: 20px;
	}
	#head_forum_mbR>ul>li {
	    line-height: 35px;
	    text-align: center;
	    float: left;
	    margin: auto 5px;
	    padding: 0 8px;
		margin-left: -3px;
	}
	
</style>
