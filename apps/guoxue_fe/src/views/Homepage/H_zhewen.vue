<template>
	<div class="hz_all">
		<div class="h_z_all">
			<transition
			  name="custom-classes-transition"
			  enter-active-class="animated slideInLeft">
				<router-view></router-view>
			</transition>
		</div>
		<Bottom v-cloak></Bottom>
	</div>
</template>

<script>
	function scroll_to_top(){
		window.scrollTo(0,0);
	}
	import Bottom from '../../components/Bottom'
	export default{
		name: 'H_zhewen',
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
	.hz_all{
		width: 100%;
	}
	.h_z_all{
		width: 1000px;
		margin: 10px auto;
		border-top: 0px;
	}
</style>
