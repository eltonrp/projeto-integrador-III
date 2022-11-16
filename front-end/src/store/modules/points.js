import axios from "axios"

axios.defaults.baseURL = "https://coletadb.herokuapp.com"

// Initial state
const state = {

    points: []

}

// Getters
const getters = {

    getAll: state => state.points

}

// Setters
const mutations = {

    setPoints: (state, points) => state.points = points

}

// Methods
const actions = {

    getPoints: async ({commit}) => {
            
        const response = await axios.get('/')
        commit('setPoints', response.data.datahome)

    },

    insertNewPoint: async ({commit}, point) => {

        await axios.post('/post', point)

    },

    deletePoint: async ({commit}, id) => {

        await axios.delete(`/delete/${id}`, id)

    }

}

// Config
export default {
    namespaced: true,
    state,
    mutations,
    actions,
    getters
}