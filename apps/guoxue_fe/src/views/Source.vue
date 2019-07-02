<template>
	<div class="S_all_div">
		<div class="S_all">
			<div style="font-size: 30px;line-height: 300px;color: gray;">
				hello i am Source Page
				<br />正在开发中...
			</div>
			<!-- <router-view></router-view> -->
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
		name: 'Source',
		components: {
			Bottom,
		},
		created(){
			scroll_to_top();
		}
	}
</script>

<style scoped="scoped">
	.S_all_div{
		width: 100%;
	}
	.S_all{
		width: 1000px;
		margin: 10px auto;
		border: 1px solid gray;
		border-radius: 30px;
		height: 800px;
	}
</style>
