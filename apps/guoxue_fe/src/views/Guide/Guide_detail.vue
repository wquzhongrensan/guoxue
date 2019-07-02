<template>
	<div class="g_t">
		<div class="h_g_nav">
			<el-breadcrumb separator="/">
				<el-breadcrumb-item :to="{ path: '/' }">首页</el-breadcrumb-item>
				<el-breadcrumb-item :to="{ path: '/Guide' }">国学司南</el-breadcrumb-item>
				<el-breadcrumb-item :to="{ path: '/Guide/Guide_deatil' }">详情</el-breadcrumb-item>
			</el-breadcrumb>
		</div>
		<div class="g_center" style="background: white;">
			<div class="g_center_0">
				<div>{{title_name}}</div>
			</div>
			<div class="g_center_2">
				<div v-for="(item, i) in link_list" :key="i">
					<a :href="item.link" target="_blank">{{item.title}}</a>
				</div>
			</div>
			
		</div>
	</div>
	
</template>

<script>
	import {
		get_guide_detail
	} from '@/api/api'
	export default{
		name: 'Guide_detail',
		data(){
			return {
				
				title_name: '',
				link_list: [
					{
						name: '国学网',
						link: 'http://www.guoxue.com/'
					},
					{
						name: '新浪',
						link: 'http://www.sina.com.cn/'
					},
					{
						name: '天涯社区',
						link: 'http://www.tianya.cn/'
					},
					{
						name: '光明网',
						link: 'http://www.gmw.cn/'
					},
					{
						name: '凤凰网',
						link: 'http://www.ifeng.com/'
					},
					{
						name: '新华网',
						link: 'http://www.xinhuanet.com/'
					},
					{
						name: '今日头条',
						link: 'http://https://www.toutiao.com/'
					},
					{
						name: '中华散文网',
						link: 'http://www.cnprose.com'
					},
					{
						name: '搜 韵',
						link: 'http://sou-yun.com/'
					},
					{
						name: '国家图书馆',
						link: 'http://www.nlc.gov.cn/'
					},
					{
						name: '豆 瓣',
						link: 'http://www.douban.com/'
					},
					{
						name: '中国社会科学网',
						link: 'http://www.cssn.cn/'
					},
					{
						name: '中华书局',
						link: 'http://www.zhbc.com.cn/index.asp'
					},
					{
						name: '中华五千年',
						link: 'http://www.zh5000.com/'
					},
				],
			}
		},
		methods: {
			get_data(){
				get_guide_detail({
					id: this.$route.query.t
				}).then((response) => {
					this.link_list = response.data;
					this.title_name = response.data[0].guide_type.title;
				})
				.catch(function (error) {
					console.log(error);
				});
			}
		},
		created(){
			this.get_data();
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
	.g_center{
		width: 1000px;
		height: 400px;
		/* border: 1px solid gray; */
		margin-top: 20px;
		overflow: hidden;
	}
	.g_center_0{
		/* display: inline-block; */
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
	.g_center_2{
		display: inline-block;
		width: 960px;
		marign: 2px auto;
		border-top: 2px solid blueviolet;
		border-left: 1px solid lightgray;
		border-right: 1px solid lightgray;
	}
	.g_center_2 div{
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
	.g_center_2 div:hover{
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
