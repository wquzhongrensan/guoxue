<template>
	<div class="pm_all">
		<div class="pm">
			<div class="pm_left">
				<router-link to="/Person_Msg/PM_right1?t=1"><div @click="change_status1" :class="['pm_left_each',{'pm_left_each_choose':current_choose_1s}]">个人资料</div></router-link>
				<router-link to="/Person_Msg/PM_right2?t=2"><div @click="change_status2" :class="['pm_left_each',{'pm_left_each_choose':current_choose_2s}]">我的收藏</div></router-link>
				<router-link to="/Person_Msg/PM_right3?t=3"><div @click="change_status3" :class="['pm_left_each',{'pm_left_each_choose':current_choose_3s}]">我的关注</div></router-link>
				<router-link to="/Person_Msg/PM_right4?t=4"><div @click="change_status4" :class="['pm_left_each',{'pm_left_each_choose':current_choose_4s}]">我的粉丝</div></router-link>
				<router-link to="/Person_Msg/PM_right5?t=5"><div @click="change_status5" :class="['pm_left_each',{'pm_left_each_choose':current_choose_5s}]" style="border-top: 1px solid lightgray;">我的论坛</div></router-link>
			</div>
			<div class="pm_right">
				<transition
				  name="custom-classes-transition"
				  enter-active-class="animated fadeInLeft">
					<router-view></router-view>
				</transition>
			</div>
		</div>
		<Bottom></Bottom>
	</div>
</template>

<script>
	function scroll_to_top(){
		window.scrollTo(0,0);
	}
	
	import Bottom from '../components/Bottom'
	export default{
		name: 'Person_Msg',
		data(){
			return{
				current_choose_1: true,
				current_choose_2: false,
				current_choose_3: false,
				current_choose_4: false,
				current_choose_5: false,
			}
		},
		components: {
			Bottom
		},
		created(){
			this.get_router_query();
		},
		methods: {
			change_status1() {
				if(!this.current_choose_1){
					this.current_choose_1 = !this.current_choose_1;
					this.current_choose_2 = false;
					this.current_choose_3 = false;
					this.current_choose_4 = false;
					this.current_choose_5 = false;

				}
			},
			change_status2() {
				if(!this.current_choose_2){
					this.current_choose_2 = !this.current_choose_2;
					this.current_choose_1 = false;
					this.current_choose_3 = false;
					this.current_choose_4 = false;
					this.current_choose_5 = false;
				}
			},
			change_status3() {
				if(!this.current_choose_3){
					this.current_choose_3 = !this.current_choose_3;
					this.current_choose_2 = false;
					this.current_choose_1 = false;
					this.current_choose_4 = false;
					this.current_choose_5 = false;
				}
			},
			change_status4() {
				if(!this.current_choose_4){
					this.current_choose_4 = !this.current_choose_4;
					this.current_choose_2 = false;
					this.current_choose_3 = false;
					this.current_choose_1 = false;
					this.current_choose_5 = false;
				}
			},
			change_status5() {
				if(!this.current_choose_5){
					this.current_choose_5 = !this.current_choose_5;
					this.current_choose_2 = false;
					this.current_choose_3 = false;
					this.current_choose_4 = false;
					this.current_choose_1 = false;
				}
			},
			
			get_router_query(){
				if(this.$route.query.t == "1"){
					this.current_choose_1 = true;
					this.current_choose_2 = false;
					this.current_choose_3 = false;
					this.current_choose_4 = false;
					this.current_choose_5 = false;
				}else if(this.$route.query.t == "2"){
					this.current_choose_1 = false;
					this.current_choose_2 = true;
					this.current_choose_3 = false;
					this.current_choose_4 = false;
					this.current_choose_5 = false;
				}else if(this.$route.query.t == "3"){
					this.current_choose_1 = false;
					this.current_choose_2 = false;
					this.current_choose_3 = true;
					this.current_choose_4 = false;
					this.current_choose_5 = false;
				}else if(this.$route.query.t == "4"){
					this.current_choose_1 = false;
					this.current_choose_2 = false;
					this.current_choose_3 = false;
					this.current_choose_4 = true;
					this.current_choose_5 = false;
				}else if(this.$route.query.t == "5"){
					this.current_choose_1 = false;
					this.current_choose_2 = false;
					this.current_choose_3 = false;
					this.current_choose_4 = false;
					this.current_choose_5 = true;
				}else{
					this.current_choose_1 = true;
					this.current_choose_2 = false;
					this.current_choose_3 = false;
					this.current_choose_4 = false;
					this.current_choose_5 = false;
				}
			}
		},
		computed: {
			current_choose_1s() {
				if(this.$route.query.t == "1"){
					this.current_choose_1 = true;
					this.current_choose_2 = false;
					this.current_choose_3 = false;
					this.current_choose_4 = false;
					this.current_choose_5 = false;
				}
				return this.current_choose_1
			},
			current_choose_2s() {
				if(this.$route.query.t == "2"){
					this.current_choose_1 = false;
					this.current_choose_2 = true;
					this.current_choose_3 = false;
					this.current_choose_4 = false;
					this.current_choose_5 = false;
				}
				return this.current_choose_2
			},
			current_choose_3s() {
				if(this.$route.query.t == "3"){
					this.current_choose_1 = false;
					this.current_choose_2 = false;
					this.current_choose_3 = true;
					this.current_choose_4 = false;
					this.current_choose_5 = false;
				}
				return this.current_choose_3
			},
			current_choose_4s() {
				if(this.$route.query.t == "4"){
					this.current_choose_1 = false;
					this.current_choose_2 = false;
					this.current_choose_3 = false;
					this.current_choose_4 = true;
					this.current_choose_5 = false;
				}
				return this.current_choose_4
			},
			current_choose_5s() {
				if(this.$route.query.t == "5"){
					this.current_choose_1 = false;
					this.current_choose_2 = false;
					this.current_choose_3 = false;
					this.current_choose_4 = false;
					this.current_choose_5 = true;
				}
				return this.current_choose_5
			},
		},
	}
</script>

<style scoped="scoped">
	.pm_all{
		width: 100%;
		height: auto;
		font-family: 'Microsoft YaHei','SF Pro Display',Roboto,Noto,Arial,'PingFang SC',sans-serif;
		
	}
	.pm{
		width: 1000px;
		margin: 0 auto;
		display: inline-block;
		margin-top: 20px;
	}
	.pm_left{
		float: left;
		width: 210px;
		height: 400px;
		background: white;
	}
	.pm_left_each{
		float: left;
		width: 210px;
		height: 40px;
		line-height: 40px;
		text-align: left;
		text-indent: 20px;
		font-size: 14px;
		color: black;
		transition: all 0.8s ease;
	}
	.pm_left_each:hover{
		background: lightgray;
		opacity: 0.7;
		font-size: 15px;
		text-decoration: none;
		color: white;
		cursor: pointer;
	}
	
	.pm_left_each_choose{
		background: darkgray;
		opacity: 0.9;
		font-size: 15px;
		text-decoration: none;
		color: white;
		width: 210px;
	}
	
	.pm_right{
		background: white;
		float: right;
		width: 788px;
		height: 800px;
		overflow: hidden;
	}
</style>
