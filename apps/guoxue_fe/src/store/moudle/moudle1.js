const state = {
    testMsg: '原始文本',
    childText:"子组件原始文本"
}

const mutations = {
    changeTestMsg(state, str){
        state.testMsg = str;
    },
    changeChildText(state, str){
        state.childText = str;
    }

}

export default{
	state: state,
	mutations: mutations
}