<template>
	<div class="a_header">
		<div id="head">
			<div id="head-menu">
				<div id="head-menu-body">
					<div id="head-mbR">
						<div >
							<img class="s_img_style" src="../static/img/jiantou.svg" alt="引导">
						</div>
						<ul class="menu-list">
							<li class="s_search_text">
								<div style="width: 170px; height: 20px;	"></div>
							</li>
							<li class="s_li_back">
								<router-link to="/" :class="{choose_s_s_1: choose_s_1s}">推荐</router-link>
							</li> 
							<li class="s_li_back1">
								<router-link to="/H_zhewen" :class="{choose_s_s_1: choose_s_2s}">哲学文化</router-link>
							</li> 
							<li class="s_li_back1">
								<router-link to="/H_shiqing" :class="{choose_s_s_1: choose_s_3s}">诗词清话</router-link>
							</li> 
							<li class="s_li_back1">
								<router-link to="/H_jingshi" :class="{choose_s_s_1: choose_s_4s}">经济史论</router-link>
							</li> 
							<li class="s_li_back1">
								<router-link to="/H_guoren" :class="{choose_s_s_1: choose_s_5s}">国学人物</router-link>
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
		name: 'Sub_nav_homepage',
		data() {
			return {
				route_data: '',
				choose_s_1: true,
				choose_s_2: false,
				choose_s_3: false,
				choose_s_4: false,
				choose_s_5: false,
			}
		},
		created(){
			this.get_route_query();
		},
		methods: {
			get_route_query(){
				this.route_data = this.$route.fullPath.split("/")[1];
				if(this.route_data == ""){
					this.choose_s_1 = true;
					this.choose_s_2 = false;
					this.choose_s_3 = false;
					this.choose_s_4 = false;
					this.choose_s_5 = false;
				}else if(this.route_data == "H_zhewen"){
					this.choose_s_1 = false;
					this.choose_s_2 = true;
					this.choose_s_3 = false;
					this.choose_s_4 = false;
					this.choose_s_5 = false;
				}else if(this.route_data == "H_shiqing"){
					this.choose_s_1 = false;
					this.choose_s_2 = false;
					this.choose_s_3 = true;
					this.choose_s_4 = false;
					this.choose_s_5 = false;
				}else if(this.route_data == "H_jingshi"){
					this.choose_s_1 = false;
					this.choose_s_2 = false;
					this.choose_s_3 = false;
					this.choose_s_4 = false;
					this.choose_s_5 = true;
				}else if(this.route_data == "H_guoren"){
					this.choose_s_1 = false;
					this.choose_s_2 = false;
					this.choose_s_3 = false;
					this.choose_s_4 = false;
					this.choose_s_5 = true;
				}
			}
					
		},
		computed: {
			choose_s_1s(){
				if(this.$route.fullPath.split("/")[1] == ""){
					this.choose_s_1 = true;
					this.choose_s_2 = false;
					this.choose_s_3 = false;
					this.choose_s_4 = false;
					this.choose_s_5 = false;
				}
				return this.choose_s_1
			},
			choose_s_2s(){
				if(this.$route.fullPath.split("/")[1] == "H_zhewen"){
					this.choose_s_1 = false;
					this.choose_s_2 = true;
					this.choose_s_3 = false;
					this.choose_s_4 = false;
					this.choose_s_5 = false;
				}
				return this.choose_s_2
			},
			choose_s_3s(){
				if(this.$route.fullPath.split("/")[1] == "H_shiqing"){
					this.choose_s_1 = false;
					this.choose_s_2 = false;
					this.choose_s_3 = true;
					this.choose_s_4 = false;
					this.choose_s_5 = false;
				}
				return this.choose_s_3
			},
			choose_s_4s(){
				if(this.$route.fullPath.split("/")[1] == "H_jingshi"){
					this.choose_s_1 = false;
					this.choose_s_2 = false;
					this.choose_s_3 = false;
					this.choose_s_4 = true;
					this.choose_s_5 = false;
				}
				return this.choose_s_4
			},
			choose_s_5s(){
				if(this.$route.fullPath.split("/")[1] == "H_guoren"){
					this.choose_s_1 = false;
					this.choose_s_2 = false;
					this.choose_s_3 = false;
					this.choose_s_4 = false;
					this.choose_s_5 = true;
				}
				return this.choose_s_5
			}
		},
			
	}
</script>

<style scoped="scoped">
	.a_header{
		background-color: lightslategray;
		opacity: 0.8;
		height: 35px;
		
	}

	.s_little_jiantou {
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
	.s_img_style{
		width:25px;
		position: absolute;
		top:-15px;
		left:205px;
	}
	.s_li_back a{
		display: block;
		height: 22px;
		line-height: 22px;
		width: 39px;
		border-radius: 5px;
		margin-top: 7px;
		font-size: 13px;
		color: white;
	}
	.s_li_back a:hover{
		background: #4D7E9B !important;
		text-decoration: none !important;
		opacity: 0.9 !important;
	}
	.choose_s_s_1{
		background: #4D7E9B !important;
		text-decoration: none !important;
	}
	.s_li_back1 a{
		display: block;
		height: 22px;
		line-height: 22px;
		width: 73px;
		border-radius: 5px;
		margin-top: 7px;
		font-size: 13px;
		color: white;
	}
	.s_li_back1 a:hover{
		background: #4D7E9B !important;
		text-decoration: none !important;
		opacity: 0.9 !important;
	}
	.s_search_2{
		line-height: 35px;
	}
	.s_search {
		color: #fff;
		background-color: gray;
		height: 31px;
		margin-top: 15px;
		line-height: 31px;
		margin-left: -7px;
		width: 45px;
		border-radius: 4px;
	}
	.s_search:hover{
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
	#head-menu {
	    height: 35px;
	    width: 100%;
	    background-color: rgba(255, 255, 255, 0.4);
	}
	#head-menu-body {
	    height: 35px;
	    width: 1200px;
	    margin: 0 auto;
	    position: relative;
	}
	#head-mbR {
		position: relative;
		margin-left: 20px;
	}
	#head-mbR>ul>li {
	    line-height: 35px;
	    text-align: center;
	    float: left;
	    margin: auto 5px;
	    padding: 0 8px;
		margin-left: -1px;
	}
	
</style>
