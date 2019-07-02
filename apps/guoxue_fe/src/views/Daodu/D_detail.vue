<template>
	<div v-cloak>
		<div class="d_nav">
			<el-breadcrumb separator="/">
				<el-breadcrumb-item :to="{ path: '/' }">首页</el-breadcrumb-item>
				<el-breadcrumb-item :to="{ path: '/Daodu' }">经典导读</el-breadcrumb-item>
				<el-breadcrumb-item :to="{ path: '/Daodu/D_detail' }">经典详情</el-breadcrumb-item>
			</el-breadcrumb>
		</div>
		<div class="d_d_bottom_all" v-if="item">
			<div class="d_d_bottom">
				<div class="d_d_bottom_top" style="background: white;">
					<div class="d_d_bottom_top_left">
						<div>
							<img :src="item.img_link" width="120" height="170" alt="易经的故事">
						</div>
					</div>
					<div class="d_d_bottom_top_right">
						<p>《{{item.name}}》</p>
						<div>作者：<a :href="'https://baike.baidu.com/item/'+item.author.name">{{item.author.name}}</a></div>
						<div>出版社: {{item.publishing_house}}</div>
						<div>出版年: {{item.publishing_date}}</div>
						<div>页数: {{item.page_count}}</div>
						<div>定价: {{item.price}}元</div>
						<div>ISBN: {{item.IBSN}}</div>
					</div>
				</div>
				<div class="d_d_bottom_center_line"></div>
				<div class="d_d_bottom_bottom" style="background: white;">
					<div class="d_d_bottom_bottom_title">
						<strong>内容简介</strong>
					</div>
					<div class="d_d_bottom_bottom_msg">
						<p>{{item.desc}}</p>
					</div>
					<div class="d_d_bottom_bottom_title">
						<strong>目录</strong>
					</div>
					<div class="d_d_bottom_bottom_msg">
						<div class="indent" id="dir_5359679_full" style="">
							图书目录<br>
							<div v-html="item.catalog"></div>
							<!-- 第一集阴阳之道<br>
							第二集八卦定乾坤<br>
							第三集《易经》与命运<br>
							第四集破解占卦<br>
							第五集乾坤易之门<br>
							第六集乾卦六龙<br>
							第七集六龙御天<br>
							第八集孔子《文言传》<br>
							第九集阳极成阴<br>
							第十集地道柔刚<br>
							第十一集乾坤之道<br>
							第十二集始生之难<br>
							第十三集蒙以养正<br>
							第十四集需要等待<br>
							第十五集待机之道<br>
							第十六集争强好胜<br>
							第十七集化除讼累<br>
							第十八集师忧比乐<br>
							第十九集师出正道<br>
							第二十集亲比和谐<br>
							第二十一集情投意合<br>
							...... -->
						</div>
					</div>
				</div>
				<div class="d_d_bottom_center_line2"></div>
			</div>
			<div class="d_d_bottom1">
				<div class="d_d_bottom1_redu_title">作者简介</div>
				<div class="d_d_bottom1_redu_msg" style="background: white;">
					<div class="d_d_bottom1_redu_msg_author_img">
						<img style="border-radius: 50%;" width="80" height="80" :src="item.author.avatar_link" alt="作者头像">
					</div>
					<div class="d_d_bottom1_redu_msg_11">
						<div>{{item.author.introduces}}</div>
					</div>
				</div>
			</div>
			<div class="d_d_bottom1">
				<div class="d_d_bottom1_redu_title">热读榜</div>
				<div class="d_d_bottom1_redu_msg" style="background: white;">
					<ul>
						<li class="d_d_bottom1_redu_msg_li1">
							<a href="javascript:;">
								<span class="span_msg1">1</span>
								<div class="d_d_bottom1_redu_msg_img">
									<img style="margin-top: 2px" width="78" height="100" src="../../static/img/经典导读/daodu_list_易经.jpg" alt="易经的智慧">
								</div>
								<div class="d_d_bottom1_redu_msg_img_desc">
									<div class="d_d_bottom1_redu_msg_img_desc_1">易经的智慧</div>
									<div class="d_d_bottom1_redu_msg_img_desc_2">曾仕强</div>
								</div>
							</a>
						</li>
						<li>
							<a href="javascript:;"><span class="span_msg1">2</span><span class="span_msg">捕捉火花</span> </a>
						</li>
						<li>
							<a href="javascript:;"><span class="span_msg1">3</span><span class="span_msg">中国当代儒学“山大</span></a>
						</li>
						<li>
							<a href="javascript:;"><span class="span_msg1">4</span><span class="span_msg">怎样学写古诗词之</span></a>
						</li>
						<li>
							<a href="javascript:;"><span class="span_msg1">5</span><span class="span_msg">中华读书报4月</span></a>
						</li>
						<li>
							<a href="javascript:;"><span class="span_msg1">6</span><span class="span_msg">什么是“文献”</span></a>
						</li>
					</ul>
				</div>
			</div>
		</div>
		<div v-else style="
			width: 1000px;
			height: 40px;
			line-height: 40px;
			background: white;
			border-radius: 10px;
			margin-top: 10px;
			font-size: 15px;
		">还没有添加相关的数据，请您耐心等待，谢谢您的配合</div>
	</div>
</template>

<script>
	import {getBookMsgs} from '@/api/api';
	function scroll_to_top(){
		window.scrollTo(0,0);
	}
	export default{
		name: 'D_detail',
		created(){
			scroll_to_top();
		},
		data() {
			return {
				author: '曾仕强',
				item: '',
				query_id: '',
			}
		},
		methods: {
			getBookMsgDatas(id) {
				getBookMsgs({
					id: id,
				}).then((response) => {
					this.item = response.data;
				  })
				  .catch(function (error) {
					console.log(error);
				  });
			}
		},
		created(){
			this.query_id = this.$route.query.id;
			this.getBookMsgDatas(this.query_id);
		}
	}
</script>

<style scoped="scoped">
	[v-cloak] {
		display: none;
	}
	.d_nav{
		margin-top: 4px;
		margin-left: 4px;
		margin-bottom: 7px;
	}
	.d_d_bottom_all{
		border-top:1px solid lightgray;
		width: 1000px;
		margin: 3px auto;
	}
	.d_d_bottom{
		/* border-right:1px solid lightgray; */
		width: 750px;
		float: left;
		margin-bottom: 500px;
	}
	.d_d_bottom_top{
		width: 679px;
		height: 200px;
		margin: 0px auto;
		margin-top: 15px;
		margin-bottom: 10px;
		margin-left: 36px;
	}
	.d_d_bottom_top_left{
		float: left;
		width: 130px;
		height: 180px;
		margin-left: 20px;
		margin-top: 11px;
		border: 1px dotted lightgray;
	}
	.d_d_bottom_top_left:hover{
		border: 1px solid lightgray;
	}
	.d_d_bottom_top_left div{
		margin: 4px auto;
	}
	.d_d_bottom_top_right{
		float: left;
		width: 450px;
		height: 200px;
		margin-left: 10px;
		overflow: hidden;
		margin-top: 3px;
	}
	.d_d_bottom_top_right p{
		float: left;
		margin-top: 15px;
		font-size: 19px;
		font-weight: 580;
		color: darkred;
		width: 730px;
		text-align: left;
		margin-bottom: 15px;
	}
	.d_d_bottom_top_right div{
		float: left;
		width: 730px;
		font-size: 13px;
		text-align: left;
		margin-top: 6px;
		font-family:  宋体, 'Lucida Grande', Verdana, Arial, Sans-Serif;
		color: black;
		margin-left: 13px;
		letter-spacing:1px;
	}
	.d_d_bottom_top_righ_grade span{
		font-weight: 600;
	}
	.d_d_bottom_top_right a:hover{
		color: #0000FF;
		text-decoration: none;
	}
	.d_d_bottom .d_d_bottom_center_line, .d_d_bottom_center_line2{
		box-sizing: content-box;
		padding: -16px;
		border: none;
		font: normal 13px/1 Verdana, Geneva, sans-serif;
		color: black;
		text-overflow: ellipsis;
		box-shadow: 0 0 2px 1px rgba(0,0,0,0.5) inset;
		transition: all 200ms cubic-bezier(0.6, -0.28, 0.735, 0.04) 10ms;
		height: 10px;
		width: 700px;
		margin-left: 24px;
	}
	.d_d_bottom_bottom{
		display: inline-block;
		width: 680px;
		margin-top: 10px;
	}
	.d_d_bottom_bottom .d_d_bottom_bottom_title{
		display: inline-block;
		width: 650px;
		height: 30px;
		text-align: left;
		line-height: 30px;
		margin-top: 8px;
	}
	.d_d_bottom_bottom_title strong{
		font-size: 17px;
		font-weight: 700;
		font-family: 'microsoft yahei';
		color: black;
	}
	.d_d_bottom_bottom_msg{
		width: 630px;
		margin: 6px auto;
		text-align: justify;
	}
	.d_d_bottom_bottom_msg p{
		font-size: 14px;
		line-height: 25px;
		font-family: 宋体, 'Lucida Grande', Verdana, Arial, Sans-Serif;
		color: black;
		/* 设置文本段落左右同时对其 */
		text-align: justify !important
	}
	p{
		display: block;
		margin-block-start: 1em;
		margin-block-end: 1em;
		margin-inline-start: 0px;
		margin-inline-end: 0px;
	}
	.d_d_bottom_center_line2{
		margin-top:5px;
		margin-bottom: 5px;
	}
	.d_d_bottom_bottom_other{
		width: 680px;
		height: 50px;
		margin-top: 20px;
	}
	.d_d_bottom_bottom_other div{
		float: right;
		margin-right: 25px;
	}
	.d_d_bottom1{
		float: left;
		width: 240px;
		/* margin-left: 10px; */
		border: 1px solid lightgray;
		margin-top: 6px;
		margin-bottom: 10px;
	}
	.d_d_bottom1_redu_msg{
		width: 240px;
	}
	.d_d_bottom1_redu_msg ul{
		list-style:none;
		padding:0;
		width:240px;
		/* margin:7px auto 0; */
		overflow: hidden;
	}
	.d_d_bottom1_redu_msg ul li{
		height:30px;
		border-bottom:1px solid #ddd;
		background-size: 3px 3px;
		width: 238px;
		float: left;
	}
	.d_d_bottom1_redu_msg ul li .span_msg1{
		border: 1px solid gray;
		background: gray;
		border-radius: 30px;
		color: white;
		width: 20px;
		height: 20px;
		line-height: 18px;
		text-align: center;
		float: left;
		margin-top: 4px;
		margin-left: 4px;
	}
	.span_msg{
		float: left;
		margin-left: 4px;
		width: 210px;
		text-indent: 4px;
		text-align: left;
		border: 0px solid gray;
	}
	.d_d_bottom1_redu_msg_li1{
		height: 106px !important;
		line-height: 106px !important;
	}
	.d_d_bottom1_redu_msg_li1 span{
		float: left;
		margin-top: 39px !important;
		margin-right: 3px;
		/* height: 100px; */
		/* line-height: 100px; */
		/* width: 35px; */
	}
	.d_d_bottom1_redu_msg ul li a{
		/* float:left; */
		height:30px;		
		font:14px/30px 'Microsoft Yahei';
		text-decoration: none;
		/* text-indent: 8px; */
		/* transition: all 0.8s cubic-bezier(0.25, 0.1, 0, 1.2); */
	}
	.d_d_bottom1_redu_msg ul li:hover{
		/* color: orchid; */
		/* font-size: 15px; */
		/* font-weight: blod; */
		background: lightgray;
		opacity: 0.8;
	}
	.d_d_bottom1_redu_title{
		display: block;
		box-sizing: content-box;
		float: none;
		z-index: auto;
		width: auto;
		height: auto;
		position: static;
		cursor: default;
		opacity: 1;
		margin: 2px;
		padding: 7px;
		overflow: visible;
		border: none;
		border-radius: 0;
		font: normal 16px/1 "Times New Roman", Times, serif;
		color: black;
		text-overflow: ellipsis;
		background: linear-gradient(90deg, rgba(255,255,255,1) 0, rgba(200,200,200,1) 100%);
		background-position: 50% 50%;
		background-origin: padding-box;
		background-clip: border-box;
		background-size: auto auto;
		box-shadow: 1px 1px 4px 0 rgba(0,0,0,0.2) ;
		
		height: 30px;
		width: 220px;
		line-height: 30px;
		font-size: 23px;
		font-family:  华文行楷, 'Lucida Grande', Verdana, Arial, Sans-Serif;
	}
	.d_d_bottom1_redu_msg_img{
		width: 80px;
		height: 100px;
		float: left;
		margin-left: 3px;
	}
	.d_d_bottom1_redu_msg_img_desc{
		float: left;
		width: 110px;
		margin-top: 16px;
	}
	.d_d_bottom1_redu_msg_img_desc_1{
		font-size: 15px;
		font-weight: 600;
	}
	.d_d_bottom1_redu_msg_author_img{
		padding-top: 13px;
		padding-bottom: 13px;
		width: 80px;
		height: 106px;
		display: inline-block;
	}
	.d_d_bottom1_redu_msg_11{
		width: 220px;
		margin-left: 10px;
		text-align: justify;
		/* text-indent: 23px; */
		padding-bottom: 10px;
		font: 16px/1.68 H-MingLiUC舊字形-98, "Droid Sans Fallback", "Yu Mincho", PMingLiU, FZXiYuan-M01, "Microsoft Yahei", Arial, sans-serif;
		font-size: 12px;
	}
</style>
