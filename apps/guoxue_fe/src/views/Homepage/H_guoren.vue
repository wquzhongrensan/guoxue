<template>
	<div class="hg_all">
		<div class="h_g_all">
			<transition
			  name="custom-classes-transition"
			  enter-active-class="animated fadeInLeft">
				<router-view></router-view>
			</transition>
		</div>
	</div>
</template>

<script>
	function scroll_to_top(){
		window.scrollTo(0,0);
	}
	import Bottom from '../../components/Bottom'
	export default{
		name: 'H_guoren',
		components: {
			Bottom,
		},
		created(){
			scroll_to_top();
		}
	}
</script>

<style scoped="scoped">
	[v-cloak] {
		display: none;
	}
	.hg_all{
		width: 100%;
		/* height: 1431px; */
	}
	.h_g_all{
		width: 1000px;
		margin: 10px auto;
		border-top: 0px;
	}
	
</style>
