<template>
    <h2>Bookings</h2>
</template>

<script>
import { mapGetters } from 'vuex'
import axios from 'axios'
import { API } from '../../common'

export default {
    data() {
        return {
            services: null,
        }
    },
    computed: {
        ...mapGetters(['selectedBusiness']),
    },
    mounted() {
        axios
            .get(`${API}/business/services`, {
                params: {
                    business_id: this.selectedBusiness.id,
                },
            })
            .then(({ data }) => (this.services = data))
            .catch((e) => console.log(e))
    },
}
</script>

<style>
</style>