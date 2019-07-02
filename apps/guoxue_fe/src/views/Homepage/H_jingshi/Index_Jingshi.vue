<template>
	<div>
		<div class="h_j_nav">
			<el-breadcrumb separator="/">
				<el-breadcrumb-item :to="{ path: '/' }">首页</el-breadcrumb-item>
				<el-breadcrumb-item :to="{ path: '/H_jingshi' }">经济史论</el-breadcrumb-item>
			</el-breadcrumb>
		</div>
		
		<div class="h_j_top">
			<img width="1000" height="140" src="../../../static/img/jingshi/jingshi_经济史论_nav.jpg" alt="经济史论">
		</div>
		
		<div class="hj_ij_left" style="background: white;">
			<div class="hj_ij_left_each_title11">经济史论</div>
			<div class="hj_ij_left_each">
				<div class="hj_ij_left_each_title" @click="hj_ij_hidden_list1">
					<div>先秦史论</div>
				</div>
				<div class="hj_ij_left_each_msg">
					<div class="h_t_top_1_left_bottom">
						<ul :class="{hj_ij_list_ul1: !(hj_ij_list_status1 % 2)}">
							<transition
							  name="custom-classes-transition"
							  enter-active-class="animated tada"
							  leave-active-class="animated fadeOutLeft">
							<li v-if="hj_ij_list_status1 % 2" :class="{hj_ij_li_style: router_query == 'xiantong'}">
								<router-link to="/H_jingshi/detail?t=xiantong">先秦通论</router-link>
							</li>
							</transition>
							<transition
							  name="custom-classes-transition"
							  enter-active-class="animated tada"
							  leave-active-class="animated fadeOutLeft">
							<li v-if="hj_ij_list_status1 % 2" :class="{hj_ij_li_style: router_query == 'yuanjing'}">
								<router-link to="/H_jingshi/detail?t=yuanjing">原始经济</router-link>
							</li>
							</transition>
							<transition
							  name="custom-classes-transition"
							  enter-active-class="animated tada"
							  leave-active-class="animated fadeOutLeft">
							<li v-if="hj_ij_list_status1 % 2" :class="{hj_ij_li_style: router_query == 'xiaxi'}">
								<router-link to="/H_jingshi/detail?t=xiaxi">夏商西周</router-link>
							</li>
							</transition>
							<transition
							  name="custom-classes-transition"
							  enter-active-class="animated tada"
							  leave-active-class="animated fadeOutLeft">
							<li v-if="hj_ij_list_status1 % 2" :class="{hj_ij_li_style: router_query == 'chunzhan'}">
								<router-link to="/H_jingshi/detail?t=chunzhan">春秋战国</router-link>
							</li>
							</transition>
						</ul>
					</div>
				</div>
			</div>
			<div class="hj_ij_left_each">
				<div class="hj_ij_left_each_title" @click="hj_ij_hidden_list2">
					<strong>汉唐史论</strong>
				</div>
				<div class="hj_ij_left_each_msg">
					<div class="h_t_top_1_left_bottom">
						<ul  :class="{hj_ij_list_ul2: !(hj_ij_list_status2 % 2)}">
							<transition
							  name="custom-classes-transition"
							  enter-active-class="animated tada"
							  leave-active-class="animated fadeOutLeft">
							<li v-if="hj_ij_list_status2 % 2"  :class="{hj_ij_li_style: router_query == 'hantong'}">
								<router-link to="/H_jingshi/detail?t=hantong">汉唐通论</router-link>
							</li>
							</transition>
							<transition
							  name="custom-classes-transition"
							  enter-active-class="animated tada"
							  leave-active-class="animated fadeOutLeft">
							<li v-if="hj_ij_list_status2 % 2"  :class="{hj_ij_li_style: router_query == 'qinqin'}">
								<router-link to="/H_jingshi/detail?t=qinqin">秦国秦代</router-link>
							</li>
							</transition>
							<transition
							  name="custom-classes-transition"
							  enter-active-class="animated tada"
							  leave-active-class="animated fadeOutLeft">
							<li v-if="hj_ij_list_status2 % 2"  :class="{hj_ij_li_style: router_query == 'weinan'}">
								<router-link to="/H_jingshi/detail?t=weinan">魏晋南北朝</router-link>
							</li>
							</transition>
							<transition
							  name="custom-classes-transition"
							  enter-active-class="animated tada"
							  leave-active-class="animated fadeOutLeft">
							<li v-if="hj_ij_list_status2 % 2"  :class="{hj_ij_li_style: router_query == 'suiwu'}">
								<router-link to="/H_jingshi/detail?t=suiwu">隋唐五代</router-link>
							</li>
							</transition>
						</ul>
					</div>
				</div>
			</div>
			<div class="hj_ij_left_each">
				<div class="hj_ij_left_each_title" @click="hj_ij_hidden_list3">
					<strong>宋元史论</strong>
				</div>
				<div class="hj_ij_left_each_msg">
					<div class="h_t_top_1_left_bottom">
						<ul  :class="{hj_ij_list_ul3: !(hj_ij_list_status3 % 2)}">
							<transition
							  name="custom-classes-transition"
							  enter-active-class="animated tada"
							  leave-active-class="animated fadeOutLeft">
							<li v-if="hj_ij_list_status3 % 2"  :class="{hj_ij_li_style: router_query == 'songtong'}">
								<router-link to="/H_jingshi/detail?t=songtong">宋元通论</router-link>
							</li>
							</transition>
							<transition
							  name="custom-classes-transition"
							  enter-active-class="animated tada"
							  leave-active-class="animated fadeOutLeft">
							<li v-if="hj_ij_list_status3 % 2"  :class="{hj_ij_li_style: router_query == 'beinan'}">
								<router-link to="/H_jingshi/detail?t=beinan">北宋南宋</router-link>
							</li>
							</transition>
							<transition
							  name="custom-classes-transition"
							  enter-active-class="animated tada"
							  leave-active-class="animated fadeOutLeft">
							<li v-if="hj_ij_list_status3 % 2"  :class="{hj_ij_li_style: router_query == 'liaoxi'}">
								<router-link to="/H_jingshi/detail?t=liaoxi">辽金西夏</router-link>
							</li>
							</transition>
							<transition
							  name="custom-classes-transition"
							  enter-active-class="animated tada"
							  leave-active-class="animated fadeOutLeft">
							<li v-if="hj_ij_list_status3 % 2"  :class="{hj_ij_li_style: router_query == 'mengshi'}">
								<router-link to="/H_jingshi/detail?t=mengshi">蒙元史论</router-link>
							</li>
							</transition>
						</ul>
					</div>
				</div>
			</div>
			<div class="hj_ij_left_each">
				<div class="hj_ij_left_each_title" @click="hj_ij_hidden_list4">
					<strong>明清史论</strong>
				</div>
				<div class="hj_ij_left_each_msg">
					<div class="h_t_top_1_left_bottom">
						<ul  :class="{hj_ij_list_ul4: !(hj_ij_list_status4 % 2)}">
							<transition
							  name="custom-classes-transition"
							  enter-active-class="animated tada"
							  leave-active-class="animated fadeOutLeft">
							<li v-if="hj_ij_list_status4 % 2" :class="{hj_ij_li_style: router_query == 'mingtong'}">
								<router-link to="/H_jingshi/detail?t=mingtong">明清通论</router-link>
							</li>
							</transition>
							<transition
							  name="custom-classes-transition"
							  enter-active-class="animated tada"
							  leave-active-class="animated fadeOutLeft">
							<li v-if="hj_ij_list_status4 % 2" :class="{hj_ij_li_style: router_query == 'mingshi'}">
								<router-link to="/H_jingshi/detail?t=mingshi">明清史论</router-link>
							</li>
							</transition>
							<transition
							  name="custom-classes-transition"
							  enter-active-class="animated tada"
							  leave-active-class="animated fadeOutLeft">
							<li v-if="hj_ij_list_status4 % 2" :class="{hj_ij_li_style: router_query == 'qingtong'}">
								<router-link to="/H_jingshi/detail?t=qingtong">清代通论</router-link>
							</li>
							</transition>
							<transition
							  name="custom-classes-transition"
							  enter-active-class="animated tada"
							  leave-active-class="animated fadeOutLeft">
							<li v-if="hj_ij_list_status4 % 2" :class="{hj_ij_li_style: router_query == 'qingqian'}">
								<router-link to="/H_jingshi/detail?t=qingqian">清代史论</router-link>
							</li>
							</transition>
						</ul>
					</div>
				</div>
			</div>
			<div class="hj_ij_left_each">
				<div class="hj_ij_left_each_title" @click="hj_ij_hidden_list5">
					<strong>近代史论</strong>
				</div>
				<div class="hj_ij_left_each_msg">
					<div class="h_t_top_1_left_bottom">
						<ul  :class="{hj_ij_list_ul5: !(hj_ij_list_status5 % 2)}">
							<transition
							  name="custom-classes-transition"
							  enter-active-class="animated tada"
							  leave-active-class="animated fadeOutLeft">
							<li v-if="hj_ij_list_status5 % 2" :class="{hj_ij_li_style: router_query == 'jintong'}">
								<router-link to="/H_jingshi/detail?t=jintong">近代通论</router-link>
							</li>
							</transition>
							<transition
							  name="custom-classes-transition"
							  enter-active-class="animated tada"
							  leave-active-class="animated fadeOutLeft">
							<li v-if="hj_ij_list_status5 % 2" :class="{hj_ij_li_style: router_query == 'wanshi'}">
								<router-link to="/H_jingshi/detail?t=wanshi">晚清史论 </router-link>
							</li>
							</transition>
							<transition
							  name="custom-classes-transition"
							  enter-active-class="animated tada"
							  leave-active-class="animated fadeOutLeft">
							<li v-if="hj_ij_list_status5 % 2" :class="{hj_ij_li_style: router_query == 'minshi'}">
								<router-link to="/H_jingshi/detail?t=minshi">民国史论</router-link>
							</li>
							</transition>
							<transition
							  name="custom-classes-transition"
							  enter-active-class="animated tada"
							  leave-active-class="animated fadeOutLeft">
							<li v-if="hj_ij_list_status5 % 2" :class="{hj_ij_li_style: router_query == 'hongqu'}">
								<router-link to="/H_jingshi/detail?t=hongqu">红色区域</router-link>
							</li>
							</transition>
						</ul>
					</div>
				</div>
			</div>
			<div class="hj_ij_left_each">
				<div class="hj_ij_left_each_title" @click="hj_ij_hidden_list6">
					<strong>现代史论</strong>
				</div>
				<div class="hj_ij_left_each_msg">
					<div class="h_t_top_1_left_bottom">
						<ul  :class="{hj_ij_list_ul6: !(hj_ij_list_status6 % 2)}">
							<transition
							  name="custom-classes-transition"
							  enter-active-class="animated tada"
							  leave-active-class="animated fadeOutLeft">
							<li v-if="hj_ij_list_status6 % 2" :class="{hj_ij_li_style: router_query == 'xiantong1'}">
								<router-link to="/H_jingshi/detail?t=xiantong1">现代通论</router-link>
							</li>
							</transition>
							<transition
							  name="custom-classes-transition"
							  enter-active-class="animated tada"
							  leave-active-class="animated fadeOutLeft">
							<li v-if="hj_ij_list_status6 % 2" :class="{hj_ij_li_style: router_query == 'jianchu'}">
								<router-link to="/H_jingshi/detail?t=jianchu">建国初期</router-link>
							</li>
							</transition>
							<transition
							  name="custom-classes-transition"
							  enter-active-class="animated tada"
							  leave-active-class="animated fadeOutLeft">
							<li v-if="hj_ij_list_status6 % 2" :class="{hj_ij_li_style: router_query == 'wenshi'}">
								<router-link to="/H_jingshi/detail?t=wenshi">文革十年</router-link>
							</li>
							</transition>
							<transition
							  name="custom-classes-transition"
							  enter-active-class="animated tada"
							  leave-active-class="animated fadeOutLeft">
							<li v-if="hj_ij_list_status6 % 2" :class="{hj_ij_li_style: router_query == 'gaikai'}">
								<router-link to="/H_jingshi/detail?t=gaikai">改革开放</router-link>
							</li>
							</transition>
						</ul>
					</div>
				</div>
			</div>
		</div>
		<router-view></router-view>
		<!-- <div class="hj_ij_right">
			<div class="hj_ij_right_title">
				<strong>先秦史论</strong>
				<a href="">更多>></a>
			</div>
			
			<div class="hj_ij_right_msg">
				<div class="h_j_center_left_msg">
					<ul>
						<li>
							<router-link to="/h_jhiqing/HS_detail">
								我们该如何阅读资治通鉴？
							</router-link>
							<span>（发布 2016-01-04  点击 7,624）</span>
						</li>
						<li>
							<a href="javascript:;">捕捉火花——陪苏秉琦先生聊天</a>
							<span>（发布 2016-01-04  点击 7,624）</span>
						</li>
						<li>
							<a href="javascript:;">中国当代儒学“山大学派”的崛起</a>
							<span>（发布 2016-01-04  点击 7,624）</span>
						</li>
						<li>
							<a href="javascript:;">怎样学写古诗词之炼句</a>
							<span>（发布 2016-01-04  点击 7,624）</span>
						</li>
						<li>
							<a href="javascript:;">中华读书报4月推荐榜</a>
							<span>（发布 2016-01-04  点击 7,624）</span>
						</li>
						<li>
							<a href="javascript:;">我们该如何阅读资治通鉴？</a>
							<span>（发布 2016-01-04  点击 7,624）</span>
						</li>
						<li>
							<a href="javascript:;">捕捉火花——陪苏秉琦先生聊天</a>
							<span>（发布 2016-01-04  点击 7,624）</span>
						</li>
						<li>
							<a href="javascript:;">中国当代儒学“山大学派”的崛起</a>
						</li>
						<li>
							<a href="javascript:;">怎样学写古诗词之炼句</a>
						</li>
						<li>
							<a href="javascript:;">中华读书报4月推荐榜</a>
						</li>
						
						
						<li>
							<a href="javascript:;">我们该如何阅读资治通鉴？</a>
						</li>
						<li>
							<a href="javascript:;">捕捉火花——陪苏秉琦先生聊天</a>
						</li>
						<li>
							<a href="javascript:;">中国当代儒学“山大学派”的崛起</a>
						</li>
						<li>
							<a href="javascript:;">怎样学写古诗词之炼句</a>
						</li>
						<li>
							<a href="javascript:;">中华读书报4月推荐榜</a>
						</li>
					</ul>
				</div>
				
				<div class="h_s_center_right_msg_bottom_pag_div">
					<div class="h_s_center_right_msg_bottom_pag">
						<el-pagination
						  background
						  layout="prev, pager, next"
						  :total="30">
						</el-pagination>
					</div>
				</div>
			</div>
		</div>
	 -->
	</div>
</template>

<script>
// 	import Vue from 'vue'
// 	Vue.directive('zhou',function(el,binding){
// 		el.style="color:"+binding.value;
// 	})	
	
	export default{
		name: 'Index_Jingshi',
		data(){
			return {
				hj_ij_list_status1: 1,
				hj_ij_list_status2: 2,
				hj_ij_list_status3: 2,
				hj_ij_list_status4: 2,
				hj_ij_list_status5: 2,
				hj_ij_list_status6: 2,
			}
		},
		computed: {
			router_query() {
				return this.$route.query.t;
			}
		},
		methods: {
			hj_ij_hidden_list1() {
				this.hj_ij_list_status1 = this.hj_ij_list_status1 + 1;
				if(this.hj_ij_list_status2 % 2){
					this.hj_ij_list_status2 = this.hj_ij_list_status2 - 1;
				}
				if(this.hj_ij_list_status3 % 2){
					this.hj_ij_list_status3 = this.hj_ij_list_status3 - 1;
				}
				if(this.hj_ij_list_status4 % 2){
					this.hj_ij_list_status4 = this.hj_ij_list_status4 - 1;
				}
				if(this.hj_ij_list_status5 % 2){
					this.hj_ij_list_status5 = this.hj_ij_list_status5 - 1;
				}
				if(this.hj_ij_list_status6 % 2){
					this.hj_ij_list_status6 = this.hj_ij_list_status6 - 1;
				}
			},
			hj_ij_hidden_list2() {
				this.hj_ij_list_status2 = this.hj_ij_list_status2 + 1;
				if(this.hj_ij_list_status1 % 2){
					this.hj_ij_list_status1 = this.hj_ij_list_status1 - 1;
				}
				if(this.hj_ij_list_status3 % 2){
					this.hj_ij_list_status3 = this.hj_ij_list_status3 - 1;
				}
				if(this.hj_ij_list_status4 % 2){
					this.hj_ij_list_status4 = this.hj_ij_list_status4 - 1;
				}
				if(this.hj_ij_list_status5 % 2){
					this.hj_ij_list_status5 = this.hj_ij_list_status5 - 1;
				}
				if(this.hj_ij_list_status6 % 2){
					this.hj_ij_list_status6 = this.hj_ij_list_status6 - 1;
				}
			},
			hj_ij_hidden_list3() {
				this.hj_ij_list_status3 = this.hj_ij_list_status3 + 1;
				if(this.hj_ij_list_status2 % 2){
					this.hj_ij_list_status2 = this.hj_ij_list_status2 - 1;
				}
				if(this.hj_ij_list_status1 % 2){
					this.hj_ij_list_status1 = this.hj_ij_list_status1 - 1;
				}
				if(this.hj_ij_list_status4 % 2){
					this.hj_ij_list_status4 = this.hj_ij_list_status4 - 1;
				}
				if(this.hj_ij_list_status5 % 2){
					this.hj_ij_list_status5 = this.hj_ij_list_status5 - 1;
				}
				if(this.hj_ij_list_status6 % 2){
					this.hj_ij_list_status6 = this.hj_ij_list_status6 - 1;
				}
			},
			hj_ij_hidden_list4() {
				this.hj_ij_list_status4 = this.hj_ij_list_status4 + 1;
				if(this.hj_ij_list_status2 % 2){
					this.hj_ij_list_status2 = this.hj_ij_list_status2 - 1;
				}
				if(this.hj_ij_list_status3 % 2){
					this.hj_ij_list_status3 = this.hj_ij_list_status3 - 1;
				}
				if(this.hj_ij_list_status1 % 2){
					this.hj_ij_list_status1 = this.hj_ij_list_status1 - 1;
				}
				if(this.hj_ij_list_status5 % 2){
					this.hj_ij_list_status5 = this.hj_ij_list_status5 - 1;
				}
				if(this.hj_ij_list_status6 % 2){
					this.hj_ij_list_status6 = this.hj_ij_list_status6 - 1;
				}
			},
			hj_ij_hidden_list5() {
				this.hj_ij_list_status5 = this.hj_ij_list_status5 + 1;
				if(this.hj_ij_list_status2 % 2){
					this.hj_ij_list_status2 = this.hj_ij_list_status2 - 1;
				}
				if(this.hj_ij_list_status3 % 2){
					this.hj_ij_list_status3 = this.hj_ij_list_status3 - 1;
				}
				if(this.hj_ij_list_status4 % 2){
					this.hj_ij_list_status4 = this.hj_ij_list_status4 - 1;
				}
				if(this.hj_ij_list_status1 % 2){
					this.hj_ij_list_status1 = this.hj_ij_list_status1 - 1;
				}
				if(this.hj_ij_list_status6 % 2){
					this.hj_ij_list_status6 = this.hj_ij_list_status6 - 1;
				}
			},
			hj_ij_hidden_list6() {
				this.hj_ij_list_status6 = this.hj_ij_list_status6 + 1;
				if(this.hj_ij_list_status2 % 2){
					this.hj_ij_list_status2 = this.hj_ij_list_status2 - 1;
				}
				if(this.hj_ij_list_status3 % 2){
					this.hj_ij_list_status3 = this.hj_ij_list_status3 - 1;
				}
				if(this.hj_ij_list_status4 % 2){
					this.hj_ij_list_status4 = this.hj_ij_list_status4 - 1;
				}
				if(this.hj_ij_list_status5 % 2){
					this.hj_ij_list_status5 = this.hj_ij_list_status5 - 1;
				}
				if(this.hj_ij_list_status1 % 2){
					this.hj_ij_list_status1 = this.hj_ij_list_status1 - 1;
				}
			},
		
		},
	}
</script>

<style scoped="scoped">
	.hj_ij_list_ul1 {
		height: 0px !important;
		transition-duration: 1s;
	}
	.hj_ij_list_ul2 {
		height: 0px !important;
		transition-duration: 1s;
	}
	.hj_ij_list_ul3 {
		height: 0px !important;
		transition-duration: 1s;
	}
	.hj_ij_list_ul4 {
		height: 0px !important;
		transition-duration: 1s;
	}
	.hj_ij_list_ul5 {
		height: 0px !important;
		transition-duration: 1s;
	}
	.hj_ij_list_ul6 {
		height: 0px !important;
		transition-duration: 1s;
	}
	.h_j_nav{
		margin-top: 3px;
		margin-bottom: 7px;
	}
	.h_j_top{
		margin-bottom: 16px;
	}
	.hj_ij_left{
		
		/* height: 1800px; */
		width: 220px;
		float: left;
		margin-left:36px;
		/* border: 1px solid lightgray; */
		background-color: #F9F9F9;
		border-radius: 14px;
	}
	.hj_ij_left_each_title11{
		float: left;
		width: 221px;
		height: 40px;
		text-shadow: 1px 1px 2px rgba(0,0,0,0.5);
		font-family: 华文行楷, 'Lucida Grande', Verdana, Arial, Sans-Serif;
		line-height: 40px;
		margin: 0 auto;
		margin-bottom: 3px;
		font-size: 22px;
		-webkit-box-shadow: 4px 4px 8px 2px rgba(0,0,0,0.2) inset;
		box-shadow: 4px 4px 8px 2px rgba(0,0,0,0.2) inset;
	}
	.hj_ij_left_each{
		float: left;
		width: 175px;
		margin: 0 auto;
		padding-bottom: 9px;
		margin-left: 20px;
		border-bottom: 1px dotted lightgray;
	}
	.hj_ij_left_each_title{
		float: left;
		text-align: left;
		margin-left: 10px;
		margin-top: 10px;
		width: 170px;
		font-size: 17px;
		font-weight: 550 !important;
	}
	.hj_ij_left_each_title:hover{
		cursor: pointer;
		opacity: 0.6;
		
	}
	.hj_ij_left_each_msg{
		float: left;
		text-align: left;
		margin-left: 15px;
		margin-top: 1px;
		/* width: 170px; */
	}
	.h_t_top_1_left_bottom{
		width: 277px;
		margin-left: -7px;
	}
	.h_t_top_1_left_bottom ul{
		list-style:none;
		padding:0;
		width:290px;
		height:125px;
		margin:7px auto 0;
		overflow: hidden;
		margin-top: 10px;
	}
	.h_t_top_1_left_bottom ul li{
		height:30px;
		background:url(../../../static/img/dot.gif) left center no-repeat;	
		background-size: 3px 3px;
		margin-left: 10px;
		width: 153px;
		float: left;
	}
	.h_t_top_1_left_bottom ul .hj_ij_li_style{
		/* border: 1px solid #FBFBFB; */
		box-shadow: 4px 4px 8px 2px rgba(0,0,0,0.2) ;
	}
	.h_t_top_1_left_bottom ul .hj_ij_li_style a{
		font-size: 16px !important;
		line-height: 28px;
		color: dodgerblue 	;
		background:#FBFBFB;
	}
	.h_t_top_1_left_bottom ul .hj_ij_li_style a{
		color: dodgerblue !important;
	}
	.h_t_top_1_left_bottom ul li a{
		float:left;
		height:30px;			
		font:14px/30px 'Microsoft Yahei';
		text-decoration:none;
		color:#000;
		text-indent:8px;
		transition: all 0.8s cubic-bezier(0.25, 0.1, 0, 1.2);
		/* color:limegreen; */
	}
	.h_t_top_1_left_bottom ul li a:hover{
		color:dodgerblue;
		font-size: 15px;
		font-weight: blod;
	}
	
	
	/* .hj_ij_right{
		width: 710px;
		float: left;
		margin-left: 20px;
	}
	.hj_ij_right_title{
		float: left;
		width: 670px;
		text-align: left;
		margin-left: 20px;
		border-bottom: 2px solid dodgerblue;
		padding-bottom: 7px;
	}
	.hj_ij_right_title strong{
		font-size:21px;
		font-weight: normal;
		float: left;
		font-family: "Microsoft Yahei", Arial, Helvetica, sans-serif;
	}
	.hj_ij_right_title a{
		float: right;
		margin-right: 6px;
		margin-top:10px;
	} */
	/* .hj_ij_right_msg{
		width: 670px;
		margin: 20px auto;
		float: left;
		margin-top: 10px;
		margin-left: 20px;
		overflow: hidden;
		border-right: 1px dotted lightgray;
		border-left: 1px dotted lightgray;
	}
	.hj_ij_right_msg_each{
		width: 640px;
		height: 100px;
		border-radius: 8px;
		border-right: 1px solid lightgray;
		border-left: 1px solid lightgray;
		margin: 17px;
		float: left
	}
	.h_j_center_left_msg{
		width: 640px;
		overflow: hidden;
	}
	.h_j_center_left_msg ul{
		list-style:none;
		padding:0;
		width:640px;
		margin:7px auto 0;
		overflow: hidden;
		margin-top: 12px;
		margin-left: 10px;
	}
	.h_j_center_left_msg ul li{
		height:30px;
		border-bottom:1px solid #ddd;
		background:url(../../../static/img/dot.gif) left center no-repeat;	
		background-size: 3px 3px;
		margin-left: 15px;
		width: 640px;
		float: left;
	}
	.h_j_center_left_msg ul li a{
		float:left;
		height:30px;			
		font:14px/30px 'Microsoft Yahei';
		text-decoration: none;
		text-indent: 8px;
		transition: all 0.8s cubic-bezier(0.25, 0.1, 0, 1.2);
	}
	.h_j_center_left_msg ul li a:hover{
		color:dodgerblue;
		font-size: 15px;
		font-weight: blod;
	}
	.h_j_center_left_msg ul li span{
		float: left;
		margin-top: 10px;
	}
	.h_s_center_right_msg_bottom_pag_div{
		width: 640px;
		margin-top: 15px;
		height: 30px;
		float: left;
		margin-left: 220px;
	}
	.h_s_center_right_msg_bottom_pag{
		margin: 0 auto;
	} */
</style>
