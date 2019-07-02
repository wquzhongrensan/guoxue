<template>
	<div class="d_all_div">
		<div class="d_all">
			<transition
			  name="custom-classes-transition"
			  enter-active-class="animated slideInDown">
				<router-view></router-view>
			</transition>
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
		name: 'Daodu',
		components: {
			Bottom,
		},
		created(){
			scroll_to_top();
		}
	}
</script>

<style scoped="scoped">
	.d_all_div{
		width: 100%;
	}
	.d_all{
		width: 1000px;
		margin: 10px auto;
		/* border: 1px solid lightgray; */
		/* height: 2000px; */
	}
</style>
