<template>
    <div>
        <h1>Overview</h1>
        <div class="row">
            <div class="col-9"></div>
            <div class="col-3">
                <ServiceList />
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import { API } from '../../common'
import { mapGetters } from 'vuex'
import ServiceList from '@/components/dashboard/ServiceList.vue'

export default {
    components: {
        ServiceList,
    },
    computed: {
        ...mapGetters(['selectedBusiness']),
    },
}
</script>

<style>
</style>