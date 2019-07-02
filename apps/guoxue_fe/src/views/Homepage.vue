<template>
	<div>
		<Sub_nav_homepage></Sub_nav_homepage>
		<transition
		  name="custom-classes-transition"
		  enter-active-class="animated fadeInLeft">
			<router-view></router-view>
		</transition>
	</div>
</template>

<script>
	import Sub_nav_homepage from '@/components/Sub_nav_homepage'
	
	export default{
		name: 'Homepage',
		components: {
			Sub_nav_homepage,
		}
	}
</script>

<style scoped="scoped">
</style>
