<template>
	<div class="hj_all">
		<div class="h_j_all">
			<router-view></router-view>
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
		name: 'Guide',
		components: {
			Bottom,
		},
		created(){
			scroll_to_top();
		}
	}
</script>

<style scoped="scoped">
	.hj_all{
		width: 100%;
	}
	.h_j_all{
		width: 1000px;
		margin: 10px auto;
	}
</style>
