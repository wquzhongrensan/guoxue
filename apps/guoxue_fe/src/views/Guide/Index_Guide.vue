<template>
	<div class="g_t">
		<!-- <div class="h_g_nav">
			<el-breadcrumb separator="/">
				<el-breadcrumb-item :to="{ path: '/' }">首页</el-breadcrumb-item>
				<el-breadcrumb-item :to="{ path: '/Guide' }">国学司南</el-breadcrumb-item>
			</el-breadcrumb>
		</div> -->
		<div class="g_top_1">
			<div class="g_top_1_left" style="background: white;border-radius: 15px;">
				<h3><span>国学</span></h3>
				<div v-for="(item, i) in link_list_guoxue" :key="i" class="g_r_real_route">
					<div class="h_t_top_1_right_talking g_r_real_route_1">
						<router-link :to="'/Guide/Guide_detail?t='+item.id">
							<div class="h_t_top_1_right_talking_2">
								<div class="h_t_top_1_right_talking_2_div1"><span>{{item.title}}</span></div><br />
							</div>
						</router-link>
					</div>
					<div class="h_t_top_1_right_talking g_r_real_route_2">
						<router-link :to="'/Guide/Guide_detail?t='+item.id">
							<div class="h_t_top_1_right_talking_2">
								<div class="h_t_top_1_right_talking_2_div1"><span>{{item.title}}</span></div><br />
							</div>
						</router-link>
					</div>
				</div>
			</div>
			<div class="g_top_1_center" style="background: white;border-radius: 15px;">
				<h3><span>推荐</span></h3>
				<div v-for="(item, i) in link_list_tuijian" :key="i" class="g_r_real_route">
					<div class="h_t_top_1_right_talking g_r_real_route_1">
						<router-link :to="'/Guide/Guide_detail?t='+item.id">
							<div class="h_t_top_1_right_talking_2">
								<div class="h_t_top_1_right_talking_2_div1"><span>{{item.title}}</span></div><br />
							</div>
						</router-link>
					</div>
					<div class="h_t_top_1_right_talking g_r_real_route_2">
						<router-link :to="'/Guide/Guide_detail?t='+item.id">
							<div class="h_t_top_1_right_talking_2">
								<div class="h_t_top_1_right_talking_2_div1"><span>{{item.title}}</span></div><br />
							</div>
						</router-link>
					</div>
				</div>
			</div>
			<div class="g_top_1_right" style="background: white;border-radius: 15px;">
				<h3><span>专题</span></h3>
				<div v-for="(item, i) in link_list_zhuanti" :key="i" class="g_r_real_route">
					<div class="h_t_top_1_right_talking g_r_real_route_1">
						<router-link :to="'/Guide/Guide_detail?t='+item.id">
							<div class="h_t_top_1_right_talking_2">
								<div class="h_t_top_1_right_talking_2_div1"><span>{{item.title}}</span></div><br />
							</div>
						</router-link>
					</div>
					<div class="h_t_top_1_right_talking g_r_real_route_2">
						<router-link :to="'/Guide/Guide_detail?t='+item.id">
							<div class="h_t_top_1_right_talking_2">
								<div class="h_t_top_1_right_talking_2_div1"><span>{{item.title}}</span></div><br />
							</div>
						</router-link>
					</div>
				</div>
			</div>
		</div>
		
		<div class="g_center" style="background: white;">
			<div class="g_center_0">
				<div>常用网址</div>
			</div>
			<div class="g_center_1">
				<div v-for="(item, i) in link_list" :key="i">
					<a :href="item.link" target="_blank">{{item.title}}</a>
				</div>
			</div>
			
		</div>
	</div>
	
</template>

<script>
	import {
		get_guide_data,
		get_guide_detail
	} from '@/api/api';
	export default{
		name: 'Index_Guide',
		data(){
			return {
				link_list_guoxue:''
			}
		},
		methods: {
			get_guide_datas() {
				get_guide_data({
				}).then((response) => {
					this.link_list_guoxue = response.data[0]["sub_guide"];
					this.link_list_tuijian = response.data[2]["sub_guide"];
					this.link_list_zhuanti = response.data[3]["sub_guide"];
				})
				.catch(function (error) {
					console.log(error);
				});
				
				get_guide_detail({
					id: 14
				}).then((response) => {
					this.link_list = response.data;
				})
				.catch(function (error) {
					console.log(error);
				});
			},
			
		},
		created(){
			this.get_guide_datas();
		}
	}
</script>

<style>
	.h_g_nav{
		margin-bottom: 12px;
	}
	.g_t{
		display: inline-block;
		width: 1000px;
		margin-top: 25px;
		height: 1000px;
		/* border: 1px solid lightgray; */
		overflow: hidden;
	}
	/* g_top_1 */
	.g_top_1{
		display: inline-block;
		width: 1000px;
		height: 270px;
	}
	
	.g_top_1_left{
		/* background: white; */
		float: left;
		overflow: hidden;
		width: 320px;
		height: 270px;
		border-top: 3px solid brown;
		border-left: 1px dotted darkgray;
		border-right: 1px dotted darkgray;
		border-bottom: 1px dotted darkgray;
	}
	.g_top_1_left h3{
		display: block;
		border-left:5px solid brown;
		text-align: left;
		font-color: block;
		margin-left: 9px;
		margin-top: 11px;
		margin-bottom: 15px; 	
		height: 18px;
	}
	.g_top_1_left h3 span{
		display: inline-block;
		margin-left: 10px;
		font-size: 19px;
		font-weight: 1000;
		transition: all 0.8s ease;
	}
	.g_top_1_left span:hover{
		transform: skew(10deg,0);
	}
	.g_top_1_center{
		float: left;
		width: 320px;
		height: 270px;
		margin-left:20px;
		border-top: 3px solid blueviolet;
		border-left: 1px dotted darkgray;
		border-right: 1px dotted darkgray;
		border-bottom: 1px dotted darkgray;
	}
	.g_top_1_center h3{
		display: block;
		border-left:5px solid blueviolet;
		text-align: left;
		font-color: block;
		margin-left: 9px;
		margin-top: 11px;
		margin-bottom: 10px; 	
		height: 18px;
	}
	.g_top_1_center h3 span{
		display: inline-block;
		margin-left: 10px;
		font-size: 19px;
		font-weight: 1000;
		transition: all 0.8s ease;
	}
	.g_top_1_center span:hover{
		transform: skew(10deg,0);
	}
	
	.g_top_1_right{
		float: left;
		width: 320px;
		height: 270px;
		margin-left: 20px;
		border-top: 3px solid orangered;
		border-left: 1px dotted darkgray;
		border-right: 1px dotted darkgray;
		border-bottom: 1px dotted darkgray;
	}
	.g_top_1_right h3{
		display: block;
		border-left:5px solid orangered;
		text-align: left;
		font-color: block;
		margin-left: 9px;
		margin-top: 11px;
		margin-bottom: 10px; 	
		height: 18px;
	}
	.g_top_1_right h3 span{
		display: inline-block;
		margin-left: 10px;
		
		font-size: 19px;
		font-weight: 1000;
		transition: all 0.8s ease;
	}
	.g_top_1_right span:hover{
		transform: skew(10deg,0);
	}
	
	.g_center{
		width: 1000px;
		height: 352px;
		margin-top: 20px;
		overflow: hidden;
	}
	.g_center_0{
		width: 100px;
		margin-left:395px;
		border-bottom: 5px solid #000099;
		text-align: center;
		height: 30px;
		border-top:960px ;
		border-right:30px ;
		border-top:30px ;
		border-radius: 20px;
		font-weight: 600;
		margin-top: 20px;
	}
	.g_center_0 div{
		font-size: 19px;
		transition: all 0.6s ease;
	}
	.g_center_0 div:hover{
		font-size: 21px;
		color:#000099;
	}
	.g_center_1{
		display: inline-block;
		width: 960px;
		marign: 2px auto;
		border: 1px solid blueviolet;
	}
	.g_center_1 div{
		float: left;
		width: 130px;
		height: 55px;
		border: 1px dotted gray;
		margin: 14.5px;
		line-height: 55px;
		text-align: center;
		font-size: 18px;
		color: dimgray;
		transition: all 200ms cubic-bezier(0.42, 0, 0.58, 1) 10ms, font-size 200ms cubic-bezier(0.42, 0, 0.58, 1) 10ms;
	}
	.g_center_1 div:hover{
		border: 1px solid gray;
		opacity: 0.8;
		background: lightgrey;
		color: white !important;
		text-decoration: none;
		transform: rotateX(-30deg);
		transform: skew(30deg,0);
	}
	
	.g_r_real_route{
		margin-top: 3px;
		float: left;
		width: 55px;
		height: 40px;
		margin: 3.8px;
		margin-bottom: 6px;
		position:relative;			
		transform-style:preserve-3d;
		transform:perspective(800px) rotateY(0deg);
	}
	.g_r_real_route_1,.g_r_real_route_2{
		position:absolute;
		left:0;
		top:0;
		backface-visibility:hidden;
		transform:perspective(800px) rotateX(0deg);
		transition:all 500ms ease;
	}
	.g_r_real_route_2{
		transform:translateZ(2px) rotateX(180deg);
	}
	
	.g_r_real_route:hover .g_r_real_route_1{
		background: lightgray;
		opacity: 0.7;
		transform:perspective(800px) rotateX(180deg);
	}
	
	.g_r_real_route:hover .g_r_real_route_2{
		background: lightgray;
		opacity: 0.7;
		transform:perspective(800px) rotateX(0deg);
	}
	.h_t_top_1_right_talking{
		width: 55px;
		height: 40px;
		
		margin: 3px;
		border: 1px dotted gray;
	}
	.h_t_top_1_right_talking_2{
		line-height: 40px;
		font-size: 13px;
		font-family:  宋体, 'Lucida Grande', Verdana, Arial, Sans-Serif;
	}
</style>
