<template>
	<div class="hs_all">
		<div class="h_s_all">
			<transition
			  name="custom-classes-transition"
			  enter-active-class="animated slideInRight">
				<router-view></router-view>
			</transition>
		</div>
		<!-- <Bottom></Bottom> -->
	</div>
</template>

<script>
	function scroll_to_top(){
		window.scrollTo(0,0);
	}
	
	import Bottom from '../../components/Bottom'
	export default{
		name: 'H_shiqing',
		components: {
			Bottom,
		},
		created(){
			scroll_to_top();
		}
	}
</script>

<style scoped="scoped">
	.hs_all{
		width: 100%;
	}
	.h_s_all{
		width: 1000px;
		margin: 10px auto;
		border-top: 0px;
	}
</style>
