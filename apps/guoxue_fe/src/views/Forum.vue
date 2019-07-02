<template>
	<div class="F_all_div">
		<Sub_nav_forum></Sub_nav_forum>
		<div class="F_all">
			<router-view></router-view>
		</div>
		<Bottom></Bottom>
	</div>
</template>

<script>
	function scroll_to_top(){
		window.scrollTo(0,0);
	}
	import Sub_nav_forum from '@/components/Sub_nav_forum.vue'
	import Bottom from '../components/Bottom'
	export default{
		name: 'Forum',
		components: {
			Sub_nav_forum,
			Bottom,
		},
		created(){
			scroll_to_top();
		}
	}
</script>

<style scoped="scoped">
	.F_all_div{
		width: 100%;
	}
	.F_all{
		width: 1000px;
		margin: 10px auto;
		/* border: 1px solid gray; */
		/* border-radius: 30px; */
		height: 1300px;
	}
</style>
