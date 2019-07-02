<template>
	<div class="bottom">
		<div class="bottom_real"><span>够啦 够啦</span></div>
	</div>
</template>

<script>
	export default{
		name:' Bottom',
		data(){
			return {
				
			}
		}
	}
</script>

<style>
	.bottom{
		width: 100%;
		height: 30px;
		display: inline-block;
		margin-top: 100px;
	}
	.bottom_real {
		padding: 11px;
		border: none;
		font: normal 25px/1 Verdana, Geneva, sans-serif;
		color: white;
		text-overflow: ellipsis;
		background: darkgray;
	}
</style>
