import { createStore } from 'vuex'
import modules from './modules'

const state = {}
const getters = {}
const mutations = {}
const actions = {}

export default createStore({
    state,
    getters,
    mutations,
    actions,
    modules
})