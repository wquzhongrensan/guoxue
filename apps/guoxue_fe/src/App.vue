<template>
  <div id="app">
		<!-- <Index></Index> -->
    <router-view/>
  </div>
</template>

<script>
	
	// import Index from './views/Index'
	
	export default {
		name: 'App',
		components: {
			// Index
		}
	}
</script>

<style>
	body{
		margin: 0px;
		background: #F5F5F5;
		opacity: 0.8;
		font-family:'Microsoft Yahei';
	}
	/* #app {
		font-family: 'Avenir', Helvetica, Arial, sans-serif;
		-webkit-font-smoothing: antialiased;
		-moz-osx-font-smoothing: grayscale;
		text-align: center;
		color: #2c3e50;
		width: 100%;
		
	} */
	/* .a_header{
		background-color: greenyellow;
		opacity: 0.8;
		height: 40px;
		width: 100%;
	} */
	[v-cloak] {
		display: none;
	}
</style>
