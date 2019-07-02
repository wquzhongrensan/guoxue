<template>
  <el-carousel style="overflow: hidden;" indicator-position="outside">
    <el-carousel-item v-for="item in silde_data" :key="item.id">
		<img :src="item.src" :alt="item.name">
    </el-carousel-item>
  </el-carousel>
</template>

<script>
	export default{
		name: 'Slide_Car',
		data(){
			return {
				silde_data:[
					{id: 1, name: "slide_易经", src: require("../static/img/homepage/易经.jpg")},
					{id: 2, name: "slide_道德经", src: require("../static/img/homepage/道德经.jpg")},
					{id: 3, name: "slide_论语", src: require("../static/img/homepage/论语.jpg")},
				]
			}
		},
	}
</script>

<style scoped="scoped">
	[v-cloak] {
		display: none;
	}
	.el-carousel__item h3 {
		color: #475669;
		font-size: 18px;
		opacity: 0.75;
		line-height: 300px;
		margin: 0;
	}
	.el-carousel__item:nth-child(2n) {
		background-color: #99a9bf;
	}
	  
	.el-carousel__item:nth-child(2n+1) {
		background-color: #d3dce6;
	}
</style>
