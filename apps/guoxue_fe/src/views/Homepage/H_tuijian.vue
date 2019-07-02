<template>
	<div class="h_t_all" v-cloak>
		<div class="h_t_top">
			<div class="h_t_top_left">
				<el-row class="tac">
					<el-col :span="12">
						<el-menu
							class="el-menu-vertical-demo"
							@open="handleOpen"
							@close="handleClose">
							<el-menu-item index="1">
								<i class="el-icon-view"></i>
								<span slot="title"/>国学入门</span>
							</el-menu-item>
							<el-menu-item index="2">
								<i class="el-icon-tickets"></i>
								<span slot="title">哲学文化</span>
							</el-menu-item>
							<el-menu-item index="3">
								<i class="el-icon-document"></i>
								<span slot="title">诗词清话</span>
							</el-menu-item>
							<el-menu-item index="4">
								<i class="el-icon-edit"></i>
								<span slot="title">经济史论</span>
							</el-menu-item>
							<el-menu-item index="5">
								<i class="el-icon-picture"></i>
								<span slot="title">国学人物</span>
							</el-menu-item>
						</el-menu>
					 </el-col>
				</el-row>
			</div>
			<div class="h_t_top_center" style="overflow: hidden;">
				<Slide_Car></Slide_Car>
			</div>
			<div class="h_t_top_right">
				<div class="h_t_top_right_top" style="background: white;">
					
					<h3 class="jinwen_route">
						<div class="jinwen_route_1">每日金文</div>
						<div class="jinwen_route_2">每日金文</div>
					</h3>
					<hr class="jinwen_hr" />
					<ul>
						<li v-for="item in jinwens" :key="item.index" @mouseenter="stop" @mouseleave="scroll_jinwen">
							<a href="javascript:;"  v-text="item"></a>
						</li>
					</ul>
				
				</div>
				<div class="h_t_top_right_bottom" style="background: white;">
					<h3>
						<span>国学分类</span>
					</h3>
					<ul class="clearfix">
						<li>
							<router-link to="/Daodu" ><img src="../../static/img/homepage/icon_jing.jpg" alt="经"></router-link>
						</li>
						<li>
							<router-link to="/Daodu"><img src="../../static/img/homepage/icon_shi.jpg" alt="史"></router-link>
						</li>
						<li>
							<router-link to="/Daodu"><img src="../../static/img/homepage/icon_zi.jpg" alt="子"></router-link>
						</li>
						<li>
							<router-link to="/Daodu"><img src="../../static/img/homepage/icon_ji.jpg" alt="集"></router-link>
						</li>
						<li>
							<router-link to="/Daodu"><img src="../../static/img/homepage/icon_qin.jpg" alt="琴"></router-link>
						</li>
						<li>
							<router-link to="/Daodu"><img src="../../static/img/homepage/icon_qi.jpg" alt="棋"></router-link>
						</li>
						<li>
							<router-link to="/Daodu"><img src="../../static/img/homepage/icon_shu.jpg" alt="书"></router-link>
						</li>
						<li>
							<router-link to="/Daodu"><img src="../../static/img/homepage/icon_hua.jpg" alt="画"></router-link>
						</li>
					</ul>
				
				</div>
			</div>
		</div>
	
		<div class="h_t_top_1">
			<div class="h_t_top_1_left" style="background: white;">
				<h3><span>国学入门</span></h3>
				<div class="h_t_top_1_left_top">
					<router-link to="/H_detail/134">
						国学即中国传统文化，有广义和狭义之分，狭义的国学仅指经、史、子、集等学问，而广义的国学则可以包括中国传统文化的各个方面，包括哲学、历史、政治、经济、法律、科教、文学、艺术等。而国学的源头和根本还是在经、史、子、集里面，主要是指《五经》和《道德经》等中华原......
					</router-link>
				</div>
				<div class="h_t_top_1_left_bottom">
					<ul>
						<li v-for="(item, i) in ArticleRMMsgs" :key="i">
							<router-link :to="'/H_detail/'+item.id">{{item.title}}</router-link>
						</li>
					</ul>
				</div>
			</div>
			<div class="h_t_top_1_center" style="background: white;">
				<h3><span>今日国学</span></h3>
				<div class="h_t_top_1_center_msg">
					<ul>
						<li v-for="(item, i) in ArticleJRMsgs">
							<router-link :to="'/H_detail/'+item.id">{{item.title}}</router-link>
						</li>
					</ul>
				</div>
			</div>
			<div class="h_t_top_1_right" style="background: white;">
				<h3><span>正在讨论...</span></h3>
				<div class="h_t_top_1_right_talking" v-for="(item ,i) in talking_msgs" :key="i">
					<div class="h_t_top_1_right_talking_1">
						<img src="../../static/img/论坛.svg" style="margin-top: 3px;margin-right: 6px;" width="40" height="40" alt="帖子详情"/>
					</div>
					<div class="h_t_top_1_right_talking_2">
						<div class="h_t_top_1_right_talking_2_div1"><span><router-link :to="'/Forum/Forum_detail?id='+item.id">{{maxSlice1(item.title, 13)}}</router-link></span></div><br />
						<div class="h_t_top_1_right_talking_2_div2">
							<span >{{item.author.username}}</span>&nbsp;&nbsp;
							<span>{{item.add_time.replace("T", "").split(".")[0]}}</span>
						</div>
					</div>
				</div>
			</div>
		</div>
		
		<div class="h_top_adv1" style="background: white;">
			<div>
				这是一个充满<span>正</span>能量的广告位
			</div>
	
		</div>
		
		<div class="h_t_center">
			<div class="h_t_center_msg_l2">
				<div class="h_t_center_msg_tm">
					<div class="h_t_center_msg_title"><span>诗词清话</span></div>
					<div class="h_t_center_msg_more"><router-link to="/H_shiqing">更多>></router-link></div>
				</div>
				<div class="h_t_center_msg_real" style="background: white;">
					<div>
						<div class="h_t_center_msg_real_img">
							<router-link to="/H_shiqing/HS_detail/2/"><img width="70" height="89" src="../../static/img/homepage/tuijian_唐诗.jpg" alt="tuijian_唐诗"></router-link>
						</div>
						<div class="h_t_center_msg_real_msg">
							<router-link to="/H_shiqing/HS_detail/2/">
								<p>
									<strong style="font-size: 16px;">唐诗</strong>   泛指创作于唐朝诗人的诗。唐诗是中华民族珍贵的文化遗产之一，是中华文化宝库中的一颗明珠，同时也对世界上许多民族和国家的文化发展产生了很大影响，对于后人研究唐代的政治、民情、风俗、文化等都有重要的参考意义和价值。
								</p>
							</router-link>
						</div>
					</div>
					<div>
						<div class="h_t_center_msg_real_img">
							<router-link to="/H_shiqing/HS_detail/12/"><img width="70" height="89" src="../../static/img/homepage/tuijian_绝句.jpg" alt="tuijian_绝句"></router-link>
						</div>
						<div class="h_t_center_msg_real_msg">
							<router-link to="/H_shiqing/HS_detail/12/">
								<p>
									<strong style="font-size: 16px;">绝句</strong>   又称截句、断句、短句、绝诗，属于近体诗的一种形式。各家对其解释并不一致，有人以为“截取律之半”以便入乐传唱。绝句由四句组成，分为律绝和古绝，其中律绝有严格的格律要求。常见的绝句有五言绝句和七言绝句，六言绝句较为少见
								</p>
							</router-link>
						</div>
					</div>
					<div>
						<div class="h_t_center_msg_real_img">
							<router-link to="/H_shiqing/HS_detail/26/"><img width="70" height="89" src="../../static/img/homepage/tuijian_楹联.jpg" alt="tuijian_楹联"></router-link>
						</div>
						<div class="h_t_center_msg_real_msg">
							<router-link to="/H_shiqing/HS_detail/26/">
								<p>
									<strong style="font-size: 16px;">楹联</strong>   中国的传统文化之一，又称楹联或对子，是写在纸、布上或刻在竹子、木头、柱子上的对偶语句。对联对仗工整，平仄协调，是一字一音的中华语言独特的艺术形式。对联是中国传统文化瑰宝。
								</p>
							</router-link>
						</div>
					</div>
				</div>
			</div>
			<div class="h_t_center_msg_r1">
				<div class="h_t_center_msg_tm">
					<div class="h_t_center_msg_title"><span>国学人物</span></div>
					<div class="h_t_center_msg_more"><router-link to="/H_guoren">更多>></router-link></div>
				</div>
				<div class="h_t_center_msg_real" style="background: white;">
					<div>
						<div class="h_t_center_msg_real_img">
							<router-link to="/H_guoren/HG_person/3"><img width="70" height="89" src="../../static/img/homepage/guoxue_person_桑弘羊.jpg" alt="桑弘羊"></router-link>
						</div>
						<div class="h_t_center_msg_real_msg">
							<router-link to="/H_guoren/HG_person/3">
								<p>
									<strong style="font-size: 16px;">桑弘羊</strong>  （前155年—前80年）西汉时期著名的理财家和政治家。事汉武帝、汉昭帝两朝，历任侍中、大农丞、治粟都尉、大司农、御史大夫等职，因功赐爵左庶长。主持或参与制定的一系列政策与制度为汉武帝的文治武功奠定了雄厚的物质基础。
								</p>
							</router-link>
						</div>
					</div>
					<div>
						<div class="h_t_center_msg_real_img">
							<router-link to="/H_guoren/HG_person/4"><img width="70" height="89" src="../../static/img/homepage/guoxue_person_钱穆.jpg" alt="钱穆"></router-link>
						</div>
						<div class="h_t_center_msg_real_msg">
							<router-link to="/H_guoren/HG_person/4">
								<p>
									<strong style="font-size: 16px;">钱穆</strong>  （1895－1990）中国现代历史学家，国学大师，教育家，中央研究院院士，故宫博物院特聘研究员。在北大任历史讲席已越10年，学识淹博，议论宏通，极得学生欢迎。其著作亦均缜密谨严，蜚声学圃，实为今日国史界之第一人。 
								</p>
							</router-link>
						</div>
					</div>
					<div>
						<div class="h_t_center_msg_real_img">
							<router-link to="/H_guoren/HG_person/2"><img width="70" height="89" src="../../static/img/homepage/曾仕强.jpg" alt="曾仕强"></router-link>
						</div>
						<div class="h_t_center_msg_real_msg">
							<router-link to="/H_guoren/HG_person/2">
								<p>
									<strong style="font-size: 16px;">曾仕强</strong> （1934-2018）现任胡雪岩研究会副会长、台湾师范大学教授，中国统一促进会理事长等。曾仕强先生生于1934年，祖籍福建漳州。在教学、研究、写作、演讲、翻译各方面皆有卓越的成就。
								</p>
							</router-link>						
						</div>
					</div>
				</div>
			</div>
			<div class="h_t_center_msg_l1">
				<div class="h_t_center_msg_tm">
					<div class="h_t_center_msg_title"><span>哲学文化</span></div>
					<div class="h_t_center_msg_more"><router-link to="/H_zhewen">更多>></router-link></div>
				</div>
				<div class="h_t_center_msg_2" style="background: white !important; ">
					<div class="con">
						<router-link to="/H_zhewen/HZ_detail/81" class="con_1">
							<div class="h_t_center_msg_2_im">
								<div class="h_t_center_msg_2_img">
									<img width="215" height="105" src="../../static/img/homepage/tuijian_周易.jpg" alt="tuijian_周易">
								</div>
								<div class="h_t_center_msg_2_msg"><span>《周易》对中国哲学史研究之重要意义</span></div>
							</div>
						</router-link>
						<router-link to="/H_zhewen/HZ_detail/81" class="con_2">
							<div class="h_t_center_msg_2_im">
								<div class="h_t_center_msg_2_img">
									<img width="215" height="105" src="../../static/img/homepage/tuijian_周易.jpg" alt="tuijian_周易">
								</div>
								<div class="h_t_center_msg_2_msg"><span>《周易》对中国哲学史研究之重要意义</span></div>
							</div>
						</router-link>
					</div>
					
					
					<div class="con">
						<router-link to="/H_zhewen/HZ_detail/74" class="con_1">
							<div class="h_t_center_msg_2_im">
								<div class="h_t_center_msg_2_img">
									<img width="215" height="105" src="../../static/img/homepage/tuijian_王阳明.jpg" alt="tuijian_王阳明">
								</div>
								<div class="h_t_center_msg_2_msg"><span>王阳明良知论的三个面向</span></div>
							</div>
						</router-link>
						<router-link to="/H_zhewen/HZ_detail/74" class="con_2">
							<div class="h_t_center_msg_2_im">
								<div class="h_t_center_msg_2_img">
									<img width="215" height="105" src="../../static/img/homepage/tuijian_王阳明.jpg" alt="tuijian_王阳明">
								</div>
								<div class="h_t_center_msg_2_msg"><span>王阳明良知论的三个面向</span></div>
							</div>
						</router-link>
					</div>
					<div class="con">
						<router-link to="/H_zhewen/HZ_detail/138" class="con_1">
							<div class="h_t_center_msg_2_im">
								<div class="h_t_center_msg_2_img">
									<img width="215" height="105" src="../../static/img/homepage/tuijian_儒家.jpg" alt="tuijian_儒家">
								</div>
								<div class="h_t_center_msg_2_msg"><span>传统儒家的自由观</span></div>
							</div>
						</router-link>
						<router-link to="/H_zhewen/HZ_detail/138" class="con_2">
							<div class="h_t_center_msg_2_im">
								<div class="h_t_center_msg_2_img">
									<img width="215" height="105" src="../../static/img/homepage/tuijian_儒家.jpg" alt="tuijian_儒家">
								</div>
								<div class="h_t_center_msg_2_msg"><span>传统儒家的自由观</span></div>
							</div>
						</router-link>
					</div>
					<div class="con">
						<router-link to="/H_zhewen/HZ_detail/139" class="con_1">
							<div class="h_t_center_msg_2_im">
								<div class="h_t_center_msg_2_img">
									<img width="215" height="105" src="../../static/img/homepage/tuijian_茶道.jpg" alt="tuijian_茶道">
								</div>
								<div class="h_t_center_msg_2_msg"><span>中国传统茶道同生态学存在共鸣</span></div>
							</div>
						</router-link>
						<router-link to="/H_zhewen/HZ_detail/139" class="con_2">
							<div class="h_t_center_msg_2_im">
								<div class="h_t_center_msg_2_img">
									<img width="215" height="105" src="../../static/img/homepage/tuijian_茶道.jpg" alt="tuijian_茶道">
								</div>
								<div class="h_t_center_msg_2_msg"><span>中国传统茶道同生态学存在共鸣</span></div>
							</div>
						</router-link>
					</div>
				</div>
			</div>
			<div class="h_t_center_msg_r2">
				<div class="h_t_center_msg_tm">
					<div class="h_t_center_msg_title"><span>经济史论</span></div>
					<div class="h_t_center_msg_more"><router-link to="/H_jingshi">更多>></router-link></div>
				</div>
				<div class="h_t_center_msg_2" style="background: white !important; ">
				 	<div class="con">
				 		<router-link to="/H_jingshi/HJ_detail/58/" class="con_1">
				 			<div class="h_t_center_msg_2_im">
				 				<div class="h_t_center_msg_2_img">
				 					<img width="215" height="105" src="../../static/img/homepage/tuijian_旧石器时代.jpg" alt="tuijian_旧石器时代">
				 				</div>
				 				<div class="h_t_center_msg_2_msg"><span>旧石器时代向新石器时代过渡时期文化初探</span></div>
				 			</div>
				 		</router-link>
				 		<router-link to="/H_zhewen/HZ_detail/58/" class="con_2">
				 			<div class="h_t_center_msg_2_im">
				 				<div class="h_t_center_msg_2_img">
				 					<img width="215" height="105" src="../../static/img/homepage/tuijian_旧石器时代.jpg" alt="tuijian_旧石器时代">
				 				</div>
				 				<div class="h_t_center_msg_2_msg"><span>旧石器时代向新石器时代过渡时期文化初探</span></div>
				 			</div>
				 		</router-link>
				 	</div>
				 	
				 	
				 	<div class="con">
				 		<router-link to="/H_zhewen/HZ_detail/67/" class="con_1">
				 			<div class="h_t_center_msg_2_im">
				 				<div class="h_t_center_msg_2_img">
				 					<img width="215" height="105" src="../../static/img/homepage/tuijian_春秋会盟.jpg" alt="tuijian_春秋会盟">
				 				</div>
				 				<div class="h_t_center_msg_2_msg"><span>试论春秋会盟的历史作用</span></div>
				 			</div>
				 		</router-link>
				 		<router-link to="/H_zhewen/HZ_detail/67/" class="con_2">
				 			<div class="h_t_center_msg_2_im">
				 				<div class="h_t_center_msg_2_img">
				 					<img width="215" height="105" src="../../static/img/homepage/tuijian_春秋会盟.jpg" alt="tuijian_春秋会盟">
				 				</div>
				 				<div class="h_t_center_msg_2_msg"><span>试论春秋会盟的历史作用</span></div>
				 			</div>
				 		</router-link>
				 	</div>
				 	<div class="con">
				 		<router-link to="/H_zhewen/HZ_detail/63/" class="con_1">
				 			<div class="h_t_center_msg_2_im">
				 				<div class="h_t_center_msg_2_img">
				 					<img width="215" height="105" src="../../static/img/homepage/tuijian_长城.jpg" alt="tuijian_长城">
				 				</div>
				 				<div class="h_t_center_msg_2_msg"><span>燕山—长城南北地区史前文化的适应变迁</span></div>
				 			</div>
				 		</router-link>
				 		<router-link to="/H_zhewen/HZ_detail/63/" class="con_2">
				 			<div class="h_t_center_msg_2_im">
				 				<div class="h_t_center_msg_2_img">
				 					<img width="215" height="105" src="../../static/img/homepage/tuijian_长城.jpg" alt="tuijian_长城">
				 				</div>
				 				<div class="h_t_center_msg_2_msg"><span>燕山—长城南北地区史前文化的适应变迁</span></div>
				 			</div>
				 		</router-link>
				 	</div>
				 	<div class="con">
				 		<router-link to="/H_zhewen/HZ_detail/62/" class="con_1">
				 			<div class="h_t_center_msg_2_im">
				 				<div class="h_t_center_msg_2_img">
				 					<img width="215" height="105" src="../../static/img/homepage/tuijian_大禹治水.jpg" alt="tuijian_大禹治水">
				 				</div>
				 				<div class="h_t_center_msg_2_msg"><span>洪水传说与大禹治水略论</span></div>
				 			</div>
				 		</router-link>
				 		<router-link to="/H_zhewen/HZ_detail/62/" class="con_2">
				 			<div class="h_t_center_msg_2_im">
				 				<div class="h_t_center_msg_2_img">
				 					<img width="215" height="105" src="../../static/img/homepage/tuijian_大禹治水.jpg" alt="tuijian_大禹治水">
				 				</div>
				 				<div class="h_t_center_msg_2_msg"><span>洪水传说与大禹治水略论</span></div>
				 			</div>
				 		</router-link>
				 	</div>
				 </div>
			</div>
		</div>
		<div class="h_top_adv2" style="background: white;">
			<div>
				这又是一个充满<span>正</span>能量的广告位
			</div>
		</div>
		<div class="h_t_bottom_1">
			<div class="h_t_bottom_1_left"  style="background: white;">
				<div class="h_t_bottom_1_left_top">
					<div class="h_t_bottom_1_left_title">
						<h3>
							<span>经典导读</span>
						</h3>
					</div>
					<div class="h_t_bottom_1_left_link"><router-link to="/Daodu">更多>></router-link></div>
				</div>
				<div class="h_t_bottom_1_left_bottom">
					<div class="h_t_bottom_1_left_bottom_div_f" v-for="(item, i) in DaoduData1" :key="i">
						<div class="h_t_bottom_1_left_bottom_div">
							<div class="h_t_bottom_1_left_bottom_img">
								<router-link :to="'/Daodu/D_detail/?id='+item.id">
									<img width="155" height="190" :src="item.img_link" :alt="item.name">
								</router-link>
							</div>
							<div class="h_t_bottom_1_left_bottom_msg">
								<router-link :to="'/Daodu/D_detail/?id='+item.id">
									{{maxSlice(item.desc)}}
								</router-link>
							</div>
						</div>
					</div>
				</div>
			</div>
			
			<div class="h_t_bottom_1_right"  style="background: white;">
				<div class="h_t_bottom_1_right_title">热读榜</div>
				<div class="h_t_bottom_1_right_msg" style="margin-top: 13px;">
					<div class="h_t_bottom_1_right_msg_div11" v-for="(item, i) in DaoduData2" :key="i">
						<div class="h_t_bottom_1_right_msg_l">{{item.id}}</div>
						<div class="h_t_bottom_1_right_msg_r"><router-link :to="'/Daodu/D_detail/?id='+item.id">{{item.name}}</router-link></div>
					</div>
				</div>
			</div>
		</div>
		<Bottom v-cloak></Bottom>
	</div>
</template>

<script>
	import {
		getArticleRMMsgs,
		getArticleJRMsgs,
		getDaoduMsgs_1,
		getDaoduMsgs_2,
		forum_detail_msgs,
	} from '@/api/api';
	
	function scroll_to_top(){
		window.scrollTo(0,0);
	}

	import Slide_Car from '../../components/Slide_Car'
	import Bottom from '../../components/Bottom'

	export default{
		name: 'H_tuijian',
		data(){
			return {
				jinwen:['一阴一阳之谓道', '一生二二生三三生万物', '道不可说'],
				intervalId:null ,//data上面定义一个定时器
				adv_msg: '这是一个充满正能量的广告位',
				intervalId_adv:null,
				// 控制经典导读那里的字符串的长度
				maxLength: 37
				,
				
				// 国学入门的数据
				ArticleRMMsgs:'',
				// 今日国学的数据
				ArticleJRMsgs:'',
				// 经典导读的数据
				DaoduData1: '',
				DaoduData2: '',
				// 正在讨论
				talking_msgs: ''
			}
		},
		components: {
			Slide_Car,
			Bottom,
		},
		computed: {
			jinwens(){
				return this.jinwen;
			},
			adv_msgs(){
				return this.adv_msg.split('');
			},
		},
		methods: {
			handleOpen(key, keyPath) {
				console.log(key, keyPath);
			},
			handleClose(key, keyPath) {
				console.log(key, keyPath);
			},
			scroll_jinwen(){
				// 定时器
				if(this.intervalId != null) return;
				this.intervalId = setInterval(()=>{
					var start = this.jinwen[0];//获取数组的第一个值
					this.jinwen.splice(0,1);
					this.jinwen.slice(1,this.jinwen.length);//获取第一个值后面所有数据
					this.jinwen.push(start);
				},1500)
			},
			stop(){
				clearInterval(this.intervalId);
				this.intervalId = null;
			},
			sroll_adv_msg(){
				// 定时器
				if(this.intervalId_adv != null) return;
				this.intervalId_adv = setInterval(()=>{
					var start = this.adv_msg.substring(0,1);
					var end = this.adv_msg.substring(1);
					this.adv_msg = end + start ;
				},1500)
			},
			stop_adv_msg(){
				clearInterval(this.intervalId_adv);
				this.intervalId_adv = null;
			},
			// 获取国学入门的数据
			getArticleRMDatas(){
				getArticleRMMsgs({
				}).then((response) => {
					this.ArticleRMMsgs = response.data;
				})
				.catch(function (error) {
					console.log(error);
				});
			},
			// 获取今日国学的数据
			getArticleJRDatas(){
				getArticleJRMsgs({
				}).then((response) => {
					this.ArticleJRMsgs = response.data;
				})
				.catch(function (error) {
					console.log(error);
				});
			},
			// 获取正在讨论的信息
			get_forum_detail_msgs(){
				forum_detail_msgs({
					page_size: 3,
					ordering: '-id',
				}).then((response) => {
					this.talking_msgs = response.data.results;
				})
				.catch(function (error) {
					console.log(error);
				});
			},
			// 获取经典导读的数据
			getDaoduDatas_1(){
				getDaoduMsgs_1({
				}).then((response) => {
					this.DaoduData1 = response.data;
				})
				.catch(function (error) {
					console.log(error);
				});
			},
			// 控制景点多读字符串的长度
			maxSlice(content){
				return content.length > this.maxLength ? content.slice(0, this.maxLength) + '...' : content;
			},
			maxSlice1(content, length){
				return content.length > length ? content.slice(0, length) + '...' : content;
			},
			// 获取经典导读的数据
			getDaoduDatas_2(){
				getDaoduMsgs_2({
				}).then((response) => {
					this.DaoduData2 = response.data;
				})
				.catch(function (error) {
					console.log(error);
				});
			},
		},
		created(){
			this.scroll_jinwen();
			this.sroll_adv_msg();
			scroll_to_top();
			// 向后台发起获取数据的请求
			this.getArticleRMDatas();
			this.getArticleJRDatas();
			this.getDaoduDatas_1();
			this.getDaoduDatas_2();
			this.get_forum_detail_msgs();
		}
	}
</script>

<style scoped="scoped">
	[v-cloak] {
		display: none;
	}
	.clearfix:before,.clearfix:after{
		content:"";
		display:table;
	}
	
	.clearfix:after{
		clear:both;
	}
	
	.clearfix{
		zoom:1;
	}
	.h_t_all{
		/* color: red; */
		margin: 0 auto
	}
	/* h_t_top */
	.h_t_top{
		display: inline-block;
		width: 1000px;
		margin-top: 10px;
	}
	.h_t_top_left{
		float: left;
		width: 230px;
		height: 300px;
		background: yellow;
	}
	.h_t_top_center{
		width: 500px;
		height: 300px;
		background: green;
		float: left;
		margin-left:10px;
	}
	.h_t_top_right{
		float: left;
		width: 250px;
		height: 300px;
		margin-left: 10px;
	}
	.el-menu{
		width: 230px;	
	}
	.el-menu-item{
		height: 60px;
	}
	.h_t_top_right_top{
		height: 120px;
		/* border:1px solid #ddd; */
		overflow:hidden;
	}
	
	.h_t_top_right_top h3{
		width:99px;
		height:30px;
		margin-left: 10px;
	}
	
	.h_t_top_right_top h3 div{
		float:left;
		height:28px;
		font:16px/30px 'Microsoft Yahei';
		color:white;
		padding:0 15px;
		margin: 6px 0px;
		background: #D95459;
	}
	/* jinwen_router */
	.jinwen_route{
		margin-top: 3px;
		position:relative;			
		transform-style:preserve-3d;
		transform:perspective(800px) rotateY(0deg);
	}
	.jinwen_route_1,.jinwen_route_2{
		position:absolute;
		left:0;
		top:0;
		backface-visibility:hidden;
		transform:perspective(800px) rotateX(0deg);
		transition:all 500ms ease;
	}
	.jinwen_route_2{
		transform:translateZ(2px) rotateX(180deg);
	}
	
	.jinwen_route:hover .jinwen_route_1{
		transform:perspective(800px) rotateX(180deg);
	}
	
	.jinwen_route:hover .jinwen_route_2{
		transform:perspective(800px) rotateX(0deg);
	}
	.jinwen_hr{
		width: 93px;
		margin-left: 10px;
		margin-top:8px;
		margin-bottom: 4px;
		
	}
	
	.h_t_top_right_top ul{
		list-style:none;
		padding:0;
		width:250px;
		height:80px;
		margin:-4px auto 0;
	}
	.h_t_top_right_top ul li{
		height:38px;
		background:url(../../static/img/dot.gif) left center no-repeat;	
		margin-left: 10px;
		width: 230px;
	}
	.h_t_top_right_top ul li a{
		float:left;
		height:38px;			
		font:14px/38px 'Microsoft Yahei';
		text-decoration:none;
		text-indent:24px;
		background: url(../../static/img/jiantou_right1.png) 1px center no-repeat;
		transition: all 0.8s ease;
	}
	.h_t_top_right_top ul li a:hover{
		color:gold;
		font-size: 16px;
		font-weight: blod;
	}
	.h_t_top_right_bottom{
		margin-top: 15px;
		height: 165px;
		/* border:1px solid #ddd; */
		overflow:hidden;
	}
	
	.h_t_top_right_bottom h3{
		width:230px;
		height:32px;
		border-bottom:1px solid #ddd;
		margin:0px auto;
	}
	
	.h_t_top_right_bottom h3 span{
		float:left;
		height:30px;
		border-bottom:2px solid red;
		font:16px/30px 'Microsoft Yahei';
		color:#000;
		padding:0 1px;
		position:relative;
		margin: 2px 0px;
	}
	.h_t_top_right_bottom ul{
		width:250px;
		margin:14px 0 16px 5px;
	}
	
	.h_t_top_right_bottom ul li{
		width:54px;
		height:54px;
		float:left;
		margin:0 8.5px 6px 0;
		transition: all 0.8ms ease-in;
	}
	.h_t_top_right_bottom ul li a img{
		width: 52px;
	}
	.h_t_top_right_bottom ul li a img:hover{
		width:53px;
	}
	
	/* h_t_top_1 */
	.h_t_top_1{
		display: inline-block;
		width: 1000px;
		margin-top: 25px;
		height: 270px;
	}
	
	.h_t_top_1_left{
		float: left;
		width: 320px;
		height: 270px;
		border-top: 3px solid brown;
		
	}
	.h_t_top_1_left h3{
		display: block;
		border-left:5px solid brown;
		text-align: left;
		font-color: block;
		margin-left: 9px;
		margin-top: 11px;
		margin-bottom: 10px; 	
		height: 18px;
	}
	.h_t_top_1_left h3 span{
		display: inline-block;
		margin-left: 10px;
		font-size: 19px;
		font-weight: 1000;
	}
	.h_t_top_1_left_top{
		margin-top: 8px;
		border-top: 1px solid darkgray;
		border-bottom: 1px solid darkgray;
		padding-top: 5px;
		padding-bottom: 5px;
		display: inline-block;
		width: 270px;
		height: 117px;
		text-align: justify;
		text-indent: 28px;
		font-size: 14px;
		text-decoration: none;
		line-height: 15px;
	}
	.h_t_top_1_left_top a:hover{
		color: brown;
	}
	/* .h_t_top_1_left_top a:visited{
		color: black;
		text-decoration: none !important;
	} */
	/* .h_t_top_1_left_top a:active{
		color: black;
		text-decoration: none !important;
	} */
	.h_t_top_1_center_msg{
		width: 320px;
	}
	.h_t_top_1_center_msg ul{
		list-style:none;
		padding:0;
		width:303px;
		margin:7px auto 0;
		overflow: hidden;
		margin-top: 12px;
		margin-left: 4px;
	}
	.h_t_top_1_center_msg ul li{
		height:30px;
		border-bottom:1px solid #ddd;
		background:url(../../static/img/dot.gif) left center no-repeat;	
		background-size: 3px 3px;
		margin-left: 10px;
		width: 300px;
		float: left;
	}
	.h_t_top_1_center_msg ul li a{
		float:left;
		height:30px;			
		font:14px/30px 'Microsoft Yahei';
		text-decoration:none;
		text-indent:8px;
		transition: all 0.8s cubic-bezier(0.25, 0.1, 0, 1.2);
		/* color:orchid; */
	}
	.h_t_top_1_center_msg ul li a:hover{
		color:orchid;
		font-size: 15px;
		font-weight: blod;
	}
	
	.h_t_top_1_center{
		float: left;
		width: 320px;
		height: 270px;
		margin-left:20px;
		border-top: 3px solid blueviolet;
		
	}
	.h_t_top_1_center h3{
		display: block;
		border-left:5px solid blueviolet;
		text-align: left;
		font-color: block;
		margin-left: 9px;
		margin-top: 11px;
		margin-bottom: 10px; 	
		height: 18px;
	}
	.h_t_top_1_center h3 span{
		display: inline-block;
		margin-left: 10px;
		font-size: 19px;
		font-weight: 1000;
	}
	.h_t_top_1_left_bottom{
		width: 320px;
	}
	.h_t_top_1_left_bottom ul{
		list-style:none;
		padding:0;
		width:290px;
		height:112px;
		margin:7px auto 0;
		overflow: hidden;
		margin-top: 15px;
	}
	.h_t_top_1_left_bottom ul li{
		height:30px;
		border-bottom:1px solid #ddd;
		background:url(../../static/img/dot.gif) left center no-repeat;	
		background-size: 3px 3px;
		margin-left: 10px;
		width: 129px;
		float: left;
	}
	.h_t_top_1_left_bottom ul li a{
		float:left;
		height:30px;			
		font:14px/30px 'Microsoft Yahei';
		text-decoration:none;
		color:#000;
		text-indent:8px;
		transition: all 0.8s cubic-bezier(0.25, 0.1, 0, 1.2);
		/* color:limegreen; */
	}
	.h_t_top_1_left_bottom ul li a:hover{
		color:brown;
		font-size: 15px;
		font-weight: blod;
	}
	
	.h_t_top_1_right{
		float: left;
		width: 320px;
		height: 270px;
		margin-left: 20px;
		border-top: 3px solid orangered;
		
	}
	.h_t_top_1_right h3{
		display: block;
		border-left:5px solid orangered;
		text-align: left;
		font-color: block;
		margin-left: 9px;
		margin-top: 11px;
		margin-bottom: 10px; 	
		height: 18px;
	}
	.h_t_top_1_right h3 span{
		display: inline-block;
		margin-left: 10px;
		
		font-size: 19px;
		font-weight: 1000;
	}
	.h_t_top_1_right_talking{
		display: inline-block;
		width: 290px;
		margin-x: auto;
		margin-bottom: 10px;
		line-height: 65px;
		height: 65px;
		border: 1px dotted lightgray;
	}
	.h_t_top_1_right_talking div{
		display: inline-block;
		height: 57px;
	}
	.h_t_top_1_right_talking_1{
		float: left;
		margin-top: 7px;
		margin-left: 10px;
	}
	.h_t_top_1_right_talking_2{
		float: left;
		margin-left: 8px;	
		line-height: 30px;
	}
	.h_t_top_1_right_talking_2 div{
		float: left;
		height: 10px;
	}
	.h_t_top_1_right_talking_2_div1{
		font-size: 15px;
		font-weight: 400;
		margin-top:5px;
	}
	
	.h_t_top_1_right_talking a{
		font-size: 15px;
		transition: all 0.8s ease;
	}
	
	.h_t_top_1_right_talking a:hover{
		text-decoration: none;
		font-size: 16px;
		color: #FD6831;
	}
	
	/* h_top_adv1 */
	.h_top_adv1{
		width: 1000px;
		height: 50px;
		display: inline-block;
		margin: 20px auto;
		text-align: center;
		line-height: 50px;
		border-top: 1px dotted lightgray;
		border-bottom: 1px dotted lightgray;
	}
	.h_top_adv1 div{
		display: inline-block;
		font-size: 25px;
		color: dimgray;
		font-family: "microsoft sans serif";
		font-weight: 800;
	}
	.h_top_adv1 div span{
		display: inline-block;
		width: 35px;
		color: white;
		height:35px;
		border-radius: 21px;
		background: red;
		line-height: 34px;
		margin-left:3px;
		margin-right: 3px;
	}
	/* h_t_center */
	.h_t_center{
		display: inline-block;
		width: 1000px;
		height: 732px;
	}
	.h_t_center_msg_l1{
		float: left;
		margin-right: 14px;
		/* background: goldenrod; */
		width: 493px;
		height: 360px;
		margin-bottom:14px;
	}
	.h_t_center_msg_l2{
		float: left;
		margin-right: 14px;
		/* background: gray; */
		width: 493px;
		height: 360px;
		margin-bottom:14px;
	}
	.h_t_center_msg_r1{
		float: left;
		/* background: saddlebrown; */
		width: 493px;
		height:360px;
		margin-bottom: 14px;
	}
	.h_t_center_msg_r2{
		float: left;
		/* background: firebrick; */
		width: 493px;
		height:360px;
		margin-bottom: 14px;
	}
	.h_t_center_msg_tm{
		display: inline-block;
		width: 475px;
		height: 40px;
		/* background: gray; */
		line-height: 34px;
	}
	.h_t_center_msg_tm {
	  -webkit-box-sizing: content-box;
	  -moz-box-sizing: content-box;
	  box-sizing: content-box;
	  padding: 9px;
	  border: none;
	  font: normal normal bold 19px/1 "Comic Sans MS", cursive, sans-serif;
	  color: black;
	  -o-text-overflow: ellipsis;
	  text-overflow: ellipsis;
	  background: -webkit-linear-gradient(82deg, rgba(193,186,186,0.7) 0, rgba(193,186,186,0.7) 16%, rgba(255,255,255,1) 100%);
	  background: -moz-linear-gradient(8deg, rgba(193,186,186,0.7) 0, rgba(193,186,186,0.7) 16%, rgba(255,255,255,1) 100%);
	  background: linear-gradient(8deg, rgba(193,186,186,0.7) 0, rgba(193,186,186,0.7) 16%, rgba(255,255,255,1) 100%);
	  background-position: 50% 50%;
	  -webkit-background-origin: padding-box;
	  background-origin: padding-box;
	  -webkit-background-clip: border-box;
	  background-clip: border-box;
	  -webkit-background-size: auto auto;
	  background-size: auto auto;
	  text-shadow: -1px -1px 0 rgba(255,255,255,0.2) , 1px 1px 0 rgba(0,0,0,0.25) ;
	  -webkit-transition: all 200ms cubic-bezier(0.42, 0, 0.58, 1) 10ms, font-size 200ms cubic-bezier(0.42, 0, 0.58, 1) 10ms;
	  -moz-transition: all 200ms cubic-bezier(0.42, 0, 0.58, 1) 10ms, font-size 200ms cubic-bezier(0.42, 0, 0.58, 1) 10ms;
	  -o-transition: all 200ms cubic-bezier(0.42, 0, 0.58, 1) 10ms, font-size 200ms cubic-bezier(0.42, 0, 0.58, 1) 10ms;
	  transition: all 200ms cubic-bezier(0.42, 0, 0.58, 1) 10ms, font-size 200ms cubic-bezier(0.42, 0, 0.58, 1) 10ms;
      height: 22px;
	  /* color: darkgreen; */
	}
	
	.h_t_center_msg_l1 .h_t_center_msg_tm:hover{
		opacity: 0.8;
		color: lightcyan;
	}
	.h_t_center_msg_l2 .h_t_center_msg_tm:hover{
		opacity: 0.8;
		color: cornsilk;
	}
	.h_t_center_msg_r1 .h_t_center_msg_tm:hover{
		opacity: 0.8;
		color: lightseagreen;
	}
	.h_t_center_msg_r2 .h_t_center_msg_tm:hover{
		opacity: 0.8;
		color: lightgoldenrodyellow;
	}
	.h_t_center_msg_tm span{
		display: inline-block;
		float: left;
		margin-left: 10px;
	}
	.h_t_center_msg_more{
		float: right;
		font-size: 13px;
		font-weight: 100;
		line-height: 28px;
		padding-right: 10px;
		color: black;
		transition: all 0.8 ease;
	}
	.h_t_center_msg_more:hover{
		color: #000099 !important;
		font-size: 14px;
	}
	.h_t_center_msg_real{
		width: 493px;
		margin-top: 2px;
		height: 318px;
		padding: 10px;
		padding-left: 20px;
		overflow: hidden;
	}
	.h_t_center_msg_real div{
		height: 100px;
		border-bottom: 1px solid lightgray;
		margin-bottom: 6px;
		font-family: 宋体, 'Lucida Grande', Verdana, Arial, Sans-Serif;
		font-size: 12px !important;
		line-height: 18px;
		text-align: justify;
	}
	.h_t_center_msg_real_img{
		float: left;
		width: 84px;
		height: 92px;
		transition: all 0.3s cubic-bezier(0.06, 0.45, 1, 1);
	}
	.h_t_center_msg_real_img img{
		transition: all 0.3s cubic-bezier(0.06, 0.45, 1, 1);
	}
	.h_t_center_msg_real_img img:hover{
		width: 71px;
		height: 90px;
	}
	.h_t_center_msg_real_msg{
		float: left;
		width: 350px;
		height: 80px;
		text-align: justify;
		font-size: 14px;
		margin-left: 10px;
		padding-top: 5px;
		
	}
	.h_t_center_msg_real_msg a:hover{
		color: #A09B9B;
		opacity: 0.6;
		text-decoration: none;
	}
	
	/* asdf */
	.h_s_center_left_msg{
		width: 493px;
		height: 310px;
		display: inline-block;
		margin:3px auto;
		
		overflow: hidden;
	}
	.h_s_center_left_msg ul{
		list-style:none;
		padding:0;
		width:461px;
		margin:7px auto 0;
		overflow: hidden;
		margin-top: 2px;
		margin-left: 10px;
	}
	.h_s_center_left_msg ul li{
		height:30px;
		/* border-bottom:1px solid #ddd; */
		background:url(../../static/img/dot.gif) left center no-repeat;	
		background-size: 3px 3px;
		margin-left: 10px;
		margin-right: 6px;
		width: 484px;
		float: left;
	}
	.h_s_center_left_msg ul li a{
		float:left;
		height:30px;			
		font:14px/30px 'Microsoft Yahei';
		text-decoration: none;
		text-indent: 8px;
		/* transition: all 0.8s cubic-bezier(0.25, 0.1, 0, 1.2); */
		transition: all 200ms cubic-bezier(0.42, 0, 0.58, 1) 10ms, font-size 200ms cubic-bezier(0.42, 0, 0.58, 1) 10ms;
		font-size: 15px;
	}
	.h_s_center_left_msg ul li a:hover{
		color:indianred;
		font-size: 17px;
		font-weight: blod;
	}
	/* asdf */
	.h_t_center_msg_2{
		width: 493px;
		height: 312px;
		display: inline-block;
		margin:3px auto;
	}
	.h_t_center_msg_2 div:hover{
		opacity: 0.9;
		background: white;
	}
	.h_t_center_msg_2 div{
		float: left;
		width: 236px;
		height: 147px;
		margin-right:3px; 
		margin-left:4px;
		margin-top: 2px;
		margin-bottom: 4px;
		border-radius: 10px;
		
	}
	.h_t_center_msg_2 .h_t_center_msg_2_im{
		display: inline-block;
		width: 236px;
		height: 147px;
		border: 1px dotted lightgray
	}
	
	.h_t_center_msg_2 .h_t_center_msg_2_img{
		float: left;
		margin-left: -1px;
		height: 110px;
	}
	.h_t_center_msg_2 .h_t_center_msg_2_msg{
		float: left;
		margin-left: -3px;
		height: 10px;
		width: 236px;
		font-size: 15px;
		text-align: center;
		padding-left:5px ;
		font-family: 宋体, 'Lucida Grande', Verdana, Arial, Sans-Serif;
		font-size: 12px !important;
	}
	
	
	.con{
		position:relative;			
		transform-style:preserve-3d;
		transform:perspective(800px) rotateY(0deg);
	}
	.con_1,.con_2{
		position:absolute;
		left:0;
		top:0;
		backface-visibility:hidden;
		transform:perspective(800px) rotateY(0deg);
		transition:all 0.7s ease;
	}

	.con_1{
		transform:translateZ(2px) rotateY(180deg);
	}

	.con:hover .con_2{
		transform:perspective(800px) rotateY(180deg);
	}
	.con:hover .con_1{
		transform:perspective(800px) rotateY(0deg);
	}
	
	
	/* h_top_adv2 */
	.h_top_adv2{
		width: 1000px;
		height: 50px;
		display: inline-block;
		margin: 20px auto;
		text-align: center;
		line-height: 50px;
		border-top: 1px dotted lightgray;
		border-bottom: 1px dotted lightgray;
	}
	.h_top_adv2 div{
		display: inline-block;
		font-size: 25px;
		color: dimgray;
		font-family: "microsoft sans serif";
		font-weight: 800;
	}
	.h_top_adv2 div span{
		display: inline-block;
		width: 35px;
		color: white;
		height:35px;
		border-radius: 21px;
		background: red;
		line-height: 34px;
		margin-left:3px;
		margin-right: 3px;
	}
	
	/* h_t_bottom_1 */
	.h_t_bottom_1{
		width: 1000px;
		margin: 3px auto;
		height: 320px;
		/* background: #0000FF; */
		margin-bottom: 10px;
	}
	.h_t_bottom_1_left{
		float: left;
		height: 320px;
		width: 720px;
		/* background: #007788; */
		
	}
	.h_t_bottom_1_left_top{
		width: 716px;
		height: 40px;
		/* background: #00CC99; */
		line-height: 40px;
	}
	.h_t_bottom_1_left_title{
		float: left;
	}
	.h_t_bottom_1_left_title h3{
		display: block;
		border-bottom:5px solid cornflowerblue;
		padding-bottom: 23px;
		text-align: left;
		font-color: block;
		margin-left: 20px;
		margin-top: 17px;
		margin-bottom: 10px; 	
		height: 18px;
	}
	.h_t_bottom_1_left_title h3 span{
		display: inline-block;
		font-size: 19px;
		font-weight: 1000;
	}
	
	.h_t_bottom_1_left_link{
		float: right;
		font-size: 13px;
		margin-right: 18px;
		margin-top: 13px;
	}
	.h_t_bottom_1_left_link a:hover{
		color: orange
	}
	.h_t_bottom_1_left_bottom{
		display: inline-block;
		width: 710px;
		height:250px;
		margin:3px auto;
	}
	.h_t_bottom_1_left_bottom_div_f{
		float: left;
		height: 248px;
		width: 161px;
		margin-left: 14px;
	}
	.h_t_bottom_1_left_bottom .h_t_bottom_1_left_bottom_div{
		float: left;
		height: 243px;
		width: 159px;
	}
	.h_t_bottom_1_left_bottom .h_t_bottom_1_left_bottom_div:hover{
		border: 1px solid lightgray;
	}
	.h_t_bottom_1_left_bottom_img{
		width: 158px;
		height: 190px;
		margin-top:2px;
		text-align: center;
	}
	.h_t_bottom_1_left_bottom_msg{
		width: 156px;
		height: 50px;
		margin-top: 10px;
		text-align: left;
	}
	.h_t_bottom_1_left_bottom_msg a:hover{
		text-decoration: none;
		color: #81A8EF;
	}
	
	
	.h_t_bottom_1_right{
		float: left;
		height: 320px;
		width: 260px;
		margin-left: 20px;
		
		overflow: hidden;
	}
	
	.h_t_bottom_1_right_title{
		margin-left:10px;
		margin-top:8px;
		width: 80px;
		height: 40px;
		border-bottom: 5px solid lightgray;
		line-height: 40px;
		font-weight: 1000;
		font-size: 22px;
		color: darkred;
	}
	.h_t_bottom_1_right_msg_div11{
		width: 240px;
		margin-top:3px;
		margin-left:12px;
		border-bottom: 1px dotted lightgray;
		height: 36px;
	}
	.h_t_bottom_1_right_msg_l{
		float: left;
		width: 25px;
		height: 25px;
		margin-top:5px;
		background: darkgray;
		color: white;
		line-height: 25px;
		font-size: 15px;
		font-weight: blod;
	}
	.h_t_bottom_1_right_msg_r{
		float: left;
		margin-left: 20px;
		margin-top:5px;
		font-size:16px;
		line-height: 25px;
		transition: all 0.8s ease;
	}
	.h_t_bottom_1_right_msg_r a:hover{
		color: darkred;
		text-decoration: none;
		font-size: 17px;
	}
	/* h_t_bottom_2 */
	.h_t_bottom_2{
		width: 1000px;
		margin: 3px auto;
		height: 320px;
		/* background: #0000FF; */
		margin-bottom: 10px;
		margin-top:30px;
	}
	.h_t_bottom_2_left{
		float: left;
		height: 330px;
		width: 720px;
		
	}
	.h_t_bottom_2_left_top{
		width: 716px;
		height: 40px;
		/* background: #00CC99; */
		line-height: 40px;
	}
	.h_t_bottom_2_left_title{
		float: left;
	}
	.h_t_bottom_2_left_title h3{
		display: block;
		border-bottom:5px solid deepskyblue;
		padding-bottom: 23px;
		text-align: left;
		margin-left: 20px;
		margin-top: 17px;
		margin-bottom: 10px; 	
		height: 18px;
	}
	.h_t_bottom_2_left_title h3 span{
		display: inline-block;
		font-size: 19px;
		font-weight: 1000;
	}
	
	.h_t_bottom_2_left_link{
		float: right;
		font-size: 13px;
		margin-right: 18px;
		margin-top: 13px;
	}
	.h_t_bottom_2_left_link a:hover{
		color: orange
	}
	.h_t_bottom_2_left_bottom{
		display: inline-block;
		width: 710px;
		height:250px;
		margin:3px auto;
	}
	.h_t_bottom_2_left_bottom .h_t_bottom_2_left_bottom_div{
		float: left;
		height: 80px;
		width: 678px;
		margin-left: 15px;
	}
	.h_t_bottom_2_left_bottom .h_t_bottom_2_left_bottom_div a{
		float: left;
		height: 80px;
		width: 678px;
	}
	.h_t_bottom_2_left_bottom_1{
		width: 158px;
		height: 80px;
		margin-top:2px;
		text-align: center;
		float: left;
		line-height: 136px;
		margin-left: -30px;
	}
	.h_t_bottom_2_left_bottom_1 img{
		width: 70px;
		height: 70px;
	}
	.h_t_bottom_2_left_bottom_2{
		width: 500px;
		height: 80px;
		margin-top: -20px;
		text-align: left;
		margin-left: -30px;
	}
	.h_t_bottom_2_left_bottom_2_div1{
		height: 10px;
		float: left;
		font-size: 16px;
		font-weight: 700;
		margin-left: -20px;
		margin-top: -10px;
	}
	.h_t_bottom_2_left_bottom_2_div2{
		height: 10px;
		float: left;
		font-size: 14px;
		font-weight: blod;
		margin-top: -35px;
		margin-left: -20px;
	}
	.h_t_bottom_2_right{
		float: left;
		height: 330px;
		width: 260px;
		margin-left: 20px;
		overflow: hidden;
	}
	.h_t_bottom_2_right_title{
		margin-left:10px;
		margin-top:8px;
		width: 80px;
		height: 40px;
		border-bottom: 5px solid lightgray;
		line-height: 40px;
		font-weight: 1000;
		font-size: 22px;
		color: darkred;
	}
	.h_t_bottom_2_right_msg_div11{
		width: 240px;
		margin-top:3px;
		margin-left:12px;
		border-bottom: 1px dotted lightgray;
		height: 36px;
	}
	.h_t_bottom_2_right_msg_l{
		float: left;
		width: 25px;
		height: 25px;
		margin-top:5px;
		background: darkgray;
		color: white;
		line-height: 25px;
		font-size: 15px;
		font-weight: blod;
	}
	.h_t_bottom_2_right_msg_r{
		float: left;
		margin-left: 20px;
		margin-top:5px;
		font-size:16px;
		line-height: 25px;
		transform: all 1000ms ease;
	}
	.h_t_bottom_2_right_msg_r a:hover{
		color: darkred;
		text-decoration: none;
		font-size:17px;
	}
	.h_t_bottom_2_left_bottom_div{
		display: inline-block;
		width: 290px;
		margin-x: auto;
		margin-bottom: 10px;
		line-height: 65px;
		height: 65px;
		border: 1px solid lightgray;
	}
	.h_t_bottom_2_left_bottom_div div{
		display: inline-block;
		height: 57px;
	}
	.h_t_bottom_2_left_bottom_div_1{
		float: left;
		margin-top: 7px;
		margin-left: 10px;
	}
	.h_t_bottom_2_left_bottom_div_2{
		float: left;
		margin-left: 8px;	
		line-height: 30px;
	}
	.h_t_bottom_2_left_bottom_div_2 div{
		float: left;
		height: 10px;
	}
	.h_t_bottom_2_left_bottom_div_2_div1{
		font-size: 15px;
		font-weight: 400;
		margin-top:5px;
	}
	.h_t_bottom_2_left_bottom_div a{
		display: inline-block;
		width: 290px;
	}
	/* .h_t_bottom_2_left_bottom_div a:hover{
		background: lightgray;
		opacity: 0.7;
	} */
	.h_t_bottom_2_left_bottom_2_div1 a:hover{
		color: #31CAFD;
		text-decoration: none;
	}
	
	.h_s_center_left_msg_left{
		float: left;
		width: 220px;
		height: 318px;
		display: inline-block;
		margin:2px auto;
		border: 1px solid lightgray;
		border-radius: 10px;
		/* border-left: 1px solid lightgray;
		border-right: 1px solid lightgray; */
		overflow: hidden;
		margin-right: 9px;
	}
	.h_s_center_left_msg_left ul{
		list-style:none;
		padding:0;
		width:235px;
		margin:2px auto 0;
		overflow: hidden;
		margin-top: 2px;
		margin-right: 1px;
	}
	.h_s_center_left_msg_left ul li{
		height:30px;
		/* border-bottom:1px solid #ddd; */
		background:url(../../static/img/dot.gif) left center no-repeat;	
		background-size: 3px 3px;
		margin-left: 10px;
		margin-right: 6px;
		width: 235px;
		float: left;
	}
	.h_s_center_left_msg_left ul li a{
		float:left;
		height:30px;			
		font:14px/30px 'Microsoft Yahei';
		text-decoration: none;
		text-indent: 8px;
		/* transition: all 0.8s cubic-bezier(0.25, 0.1, 0, 1.2); */
		transition: all 200ms cubic-bezier(0.42, 0, 0.58, 1) 10ms, font-size 200ms cubic-bezier(0.42, 0, 0.58, 1) 10ms;
		font-size: 15px;
	}
	.h_s_center_left_msg_left ul li a:hover{
		color:indianred;
		font-size: 17px;
		font-weight: blod;
	}
	.h_s_center_left_msg_right{
		float: left;
		width: 253px;
		height: 600px;
		display: inline-block;
		margin:3px auto;
		
		overflow: hidden;
	}
	.h_s_center_left_msg_right ul{
		list-style:none;
		padding:0;
		width:250px;
		margin:7px auto 0;
		overflow: hidden;
		margin-top: 2px;
		margin-left: 10px;
	}
	.h_s_center_left_msg_right ul li{
		height:30px;
		/* border-bottom:1px solid #ddd; */
		background:url(../../static/img/dot.gif) left center no-repeat;	
		background-size: 3px 3px;
		margin-left: 10px;
		margin-right: 6px;
		width: 250px;
		float: left;
	}
	.h_s_center_left_msg_right ul li a{
		float:left;
		height:30px;			
		font:14px/30px 'Microsoft Yahei';
		text-decoration: none;
		text-indent: 8px;
		/* transition: all 0.8s cubic-bezier(0.25, 0.1, 0, 1.2); */
		transition: all 200ms cubic-bezier(0.42, 0, 0.58, 1) 10ms, font-size 200ms cubic-bezier(0.42, 0, 0.58, 1) 10ms;
		font-size: 15px;
	}
	.h_s_center_left_msg_right ul li a:hover{
		color:indianred;
		font-size: 17px;
		font-weight: blod;
	}
	.h_s_center_left_msg_left_top{
		width: 218px;
		height: 30px !important;
		border: 1px solid dimgray !important;
		border-radius: 10px;
		border-bottom: 3px solid dimgray;
		text-align: center;
		line-height: 30px;
	}
	.h_s_center_left_msg_left{
		height: 300px !important;
		font-size: 18px;
		color: darkred;
	}
</style>
