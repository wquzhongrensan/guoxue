<template>
	<h1>{{testMsg}}</h1>
</template>

<script>
	export default{
		name: 'test',
		data() {
			return {
				// testMsg: ''
			}
		},
		computed: {
			testMsg(){
				alert(this.$store.state.moudle1.testMsg);
				
				return this.$store.state.moudle1.testMsg;
			}
		}
	}
</script>

<style>
</style>
