// import axios  from 'axios'
import axios from '@/axios/http';
// Vue.prototype.$axios = axios;
// axios.defaults.headers.patch['Content-Type'] = 'application/x-www-fromurlencodeed'
let base = '';
export const host = 'http://192.168.255.132:8007'

// 用户注册
export const register = params => {
	return axios.post(`${host}/users/`, params)
}

// 用户登录
export const login = params => {
	return axios.post(`${host}/sessions/`, params)
}

// 用户第三方登录   这个接口是没有用的。  已经直接使用router的push方法添加路径了
export const login_TP = params => {
	return axios.get(`${host}/login/weibo`, params)
}

// 获取用户的id    
export const get_users_id = params => {
	return axios.get(`${host}/users_id/?username=` + params.username)
}

// 获取书籍分类信息
export const getBookTypes = params => {
	if("id" in params){
		return axios.get(`${host}/book_types/` + params.id+'/');
	}else{
		return axios.get(`${host}/book_types/`, params)
	}
}
// 获取书籍详情
export const getBookMsgs = params => {
	if("id" in params){
		return axios.get(`${host}/book_msgs/` + params.id+'/');
	}else{
		return axios.get(`${host}/book_msgs/`, params)
	}
}

// 获取指南信息
export const get_guide_data = params => {
	return axios.get(`${host}/guide_type_msgs/`)
}
// 获取指南详细信息
export const get_guide_detail = params => {
	return axios.get(`${host}/guide_detail_msgs?guide_type=`+params.id)

}

// 获取首页的文章详情
export const getArticleDMsgs = params => {
	if("id" in params){
		return axios.get(`${host}/article_d_msgs/` + params.id+'/');
	}else{
		return axios.get(`${host}/article_d_msgs/`, params)
	}
}

// 获取首页的国学入门的数据
export const getArticleRMMsgs = params => {
	if("id" in params){
		return axios.get(`${host}/article_rm_msgs/` + params.id+'/');
	}else{
		return axios.get(`${host}/article_rm_msgs/`, params)
	}
}
// 获取首页的今日国学的数据
export const getArticleJRMsgs = params => {
	if("id" in params){
		return axios.get(`${host}/article_jr_msgs/` + params.id+'/');
	}else{
		return axios.get(`${host}/article_jr_msgs/`, params)
	}
}
// 获取首页经典导读的数据
export const getDaoduMsgs_1 = params => {
	return axios.get(`${host}/book_homepages/`, params)
}
export const getDaoduMsgs_2 = params => {
	return axios.get(`${host}/book_sort_homepages/`, params)
}
// 获取各分类信息
export const getArticleTypeMsgs = params => {
	if("id" in params){
		return axios.get(`${host}/article_zw_msgs/` + params.id+'/');
	}else{
		return axios.get(`${host}/article_zw_msgs/`, params)
	}
}

// 获取国学人物的分类信息 article_gr_msgs
export const getGuoRenMsgs = params => {
	if("id" in params){
		return axios.get(`${host}/article_gr_msgs/` + params.id+'/');
	}else{
		return axios.get(`${host}/article_gr_msgs/`, params)
	}
}

// 获取国学人物的详细信息 article_gr_msgs
export const getGuoRenDetailMsgs = params => {
	if("id" in params){
		return axios.get(`${host}/article_grd_msgs/` + params.id+'/');
	}else{
		return axios.get(`${host}/article_grd_msgs/`, params)
	}
}

// 获取需要认证之后的信息
export const get_book_jwt_test = params => {
	return axios.get(`${host}/book_jwt_test/`, params)
}

// 获取个人信息
export const person_info = params => {
	return axios.get(`${host}/person_info/?username=`+ params.username)
}
// 修改个人信息
export const person_infos = params => {
	if("put" == params.method){
		return axios.patch(`${host}/person_infos/` + params.id+'/', params);
	}else if("post" == params.method){
		return axios.post(`${host}/person_infos/`, params)
	}
}

// 获取论坛分类信息
export const forum_type_msgs = params => {
	if("id" in params){
		return axios.get(`${host}/forum_type_msgs/` + params.id+'/');
	}else{
		return axios.get(`${host}/forum_type_msgs/`, params)
	}
}

// 用户发帖
export const publish_forum_topics = params => {
	return axios.post(`${host}/forum_topics/`, params)
}
// 获取某个帖子详情信息 /id
export const get_forum_msgs = params => {
	if("id" in params){
		return axios.get(`${host}/forum_msgs/` + params.id+'/');
	}else{
		return axios.get(`${host}/forum_msgs/`, params)
	} 
}

// 用户回帖
export const reply_forums = params => {
	return axios.post(`${host}/forum_reply_msgs/`, params)
}

// 获取排名信息
export const forum_honor_msgs = params => {
	return axios.get(`${host}/forum_honor_msgs/`, params)
}

// 获取多个帖子详情信息
export const forum_detail_msgs = params => {
	if('delete_id' in params){
		return axios.delete(`${host}/forum_detail_msgs/` + params.delete_id + '/');
	}else if('author' in params){
		return axios.get(`${host}/forum_detail_msgs/?page_size=` + params.page_size + '&ordering=' + params.ordering + '&p=' + params.p + '&author=' + params.author);
	}if(('p' in params) & ('ordering' in params)){
		return axios.get(`${host}/forum_detail_msgs/?page_size=` + params.page_size + '&forum_type_id=' + params.forum_type_id + '&p='+params.p + '&ordering=' + params.ordering);
	}else if('p' in params){
		return axios.get(`${host}/forum_detail_msgs/?page_size=` + params.page_size + '&forum_type_id=' + params.forum_type_id + '&p='+params.p);
	}else if('forum_type_id' in params){
		return axios.get(`${host}/forum_detail_msgs/?page_size=` + params.page_size + '&forum_type_id=' + params.forum_type_id);
	}else{
		return axios.get(`${host}/forum_detail_msgs/?page_size=` + params.page_size + '&ordering=' + params.ordering);
	}
}

// 用户关注功能
export const userfollow_msgs = params => {
	if("user_ids" in params){
		return axios.get(`${host}/userfollow_msgs/?user=` + params.user_ids)
	}else if('follow_ids' in params){
		return axios.get(`${host}/userfollow_msgs/?follow=` + params.follow_ids)
	}else if('delete_user_id' in params){
		return axios.delete(`${host}/userfollow_msgs/` + params.delete_user_id + '/');
	}
	return axios.post(`${host}/userfollow_msgs/`, params);
}
// 用户收藏功能
export const userfav_msgs = params => {
	if('userss' in params){
		return axios.get(`${host}/userfav_msgs?user=` + params.userss);
	}else if('fav_id' in params){
		return axios.delete(`${host}/userfav_msgs/` + params.fav_id + '/');
	}
	return axios.post(`${host}/userfav_msgs/`, params)
}

// 获取用户回复的帖子
export const get_reply_forums = params => {
	return axios.get(`${host}/forum_detail_reply_msgs?author=`+params.author+'&page_size='+params.page_size+'&p='+params.p)
}
// 获取部分帖子
export const get_part_forum_forums = params => {
	return axios.get(`${host}/forum_part_detail_msgs?page_size=`+params.page_size)
}


