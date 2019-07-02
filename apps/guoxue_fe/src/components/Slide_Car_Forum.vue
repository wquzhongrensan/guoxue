<template>
  <el-carousel indicator-position="outside">
    <el-carousel-item v-for="item in silde_data" :key="item.id">
		<img width="370" height="300" :src="item.src" :alt="item.name">
    </el-carousel-item>
  </el-carousel>
</template>

<script>
	export default{
		name: 'Slide_Car_Forum',
		data(){
			return {
				silde_data:[
					{id: 2, name: "slide_4", src: require("../static/img/国学论坛/car_2.jpg")},
					{id: 3, name: "slide_2", src: require("../static/img/国学论坛/car_3.jpg")},
					{id: 4, name: "slide_3", src: require("../static/img/国学论坛/car_4.jpg")},
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
		line-height: 290px;
		margin: 0;
	}
	.el-carousel__item:nth-child(2n) {
		background-color: #99a9bf;
	}
	  
	.el-carousel__item:nth-child(2n+1) {
		background-color: #d3dce6;
	}
</style>
