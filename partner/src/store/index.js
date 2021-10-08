import { createStore } from 'vuex'
import axios from 'axios'

export default createStore({
    state: {
        user: null,
        businesses: [],
        selectedBusiness: null,
    },
    mutations: {
        SET_USER_DATA(state, userData) {
            localStorage.setItem('user', JSON.stringify(userData))
            axios.defaults.headers.common[
                'Authorization'
            ] = `Bearer ${userData.access_token}`
            state.user = userData
        },
        CLEAR_USER_DATA() {
            localStorage.removeItem('user')
            location.reload()
        },
        SET_BUSINESS(state, business) {
            state.selectedBusiness = business
        },
        SET_BUSINESSES(state, businesses) {
            state.businesses = businesses
        },
    },
    actions: {
        register({ commit }, credentials) {
            return axios
                .post('//localhost:3000/register', credentials)
                .then(({ data }) => {
                    commit('SET_USER_DATA', data)
                })
        },
        login({ commit }, userData) {
            commit('SET_USER_DATA', userData)
        },
        logout({ commit }) {
            commit('CLEAR_USER_DATA')
        },
        selectBusiness({ commit }, business) {
            commit('SET_BUSINESS', business)
        },
        selectBusinesses({ commit }, businesses) {
            commit('SET_BUSINESSES', businesses)
        },
    },
    modules: {},
    getters: {
        loggedIn(state) {
            return !!state.user
        },
        getUser(state) {
            return state.user
        },
        selectedBusiness(state) {
            return state.selectedBusiness
        },
        businesses(state) {
            return state.businesses
        },
    },
})
