<template>
    <div class="container">
        <Tabs />
        <router-view v-if="businesses.length !== 0"></router-view>
    </div>
</template>

<script>
import Tabs from '@/components/Tabs.vue'
import axios from 'axios'
import { API } from '../common'

export default {
    name: 'Dashboard',
    components: {
        Tabs,
    },
    data() {
        return {
            businesses: [],
        }
    },
    mounted() {
        axios.get(`${API}/business/`).then(({ data }) => {
            this.$store.dispatch('selectBusinesses', data)
            this.$store.dispatch('selectBusiness', data[0])
            this.businesses = data
        })
    },
}
</script>

<style>
</style>