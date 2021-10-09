<template>
    <div>
        <h5>Services</h5>
        <ul class="list-group" v-if="services.length !== 0">
            <li
                class="list-group-item"
                :class="{ active: service === selectedService }"
                v-for="service in services"
                :key="service.id"
                @click="handleSelectService(service)"
            >
                {{ service.name }}
            </li>
            <li class="list-group-item">
                <svg
                    xmlns="http://www.w3.org/2000/svg"
                    width="25"
                    height="25"
                    fill="currentColor"
                    class="bi bi-plus"
                    viewBox="0 0 20 17"
                >
                    <path
                        d="M8 4a.5.5 0 0 1 .5.5v3h3a.5.5 0 0 1 0 1h-3v3a.5.5 0 0 1-1 0v-3h-3a.5.5 0 0 1 0-1h3v-3A.5.5 0 0 1 8 4z"
                    />
                </svg>
                Create a service
            </li>
        </ul>
        <ul class="list-group" v-else>
            <li class="list-group-item">
                <svg
                    xmlns="http://www.w3.org/2000/svg"
                    width="25"
                    height="25"
                    fill="currentColor"
                    class="bi bi-plus"
                    viewBox="0 0 20 17"
                >
                    <path
                        d="M8 4a.5.5 0 0 1 .5.5v3h3a.5.5 0 0 1 0 1h-3v3a.5.5 0 0 1-1 0v-3h-3a.5.5 0 0 1 0-1h3v-3A.5.5 0 0 1 8 4z"
                    />
                </svg>
                Create a service
            </li>
        </ul>
    </div>
</template>

<script>
import axios from 'axios'
import { mapGetters } from 'vuex'
import { API } from '../../common'

export default {
    computed: {
        ...mapGetters(['selectedBusiness']),
    },
    emits: ['selectedService'],
    data() {
        return {
            services: [],
            selectedService: null,
        }
    },
    methods: {
        fetchServices() {
            if (this.selectedBusiness !== null) {
                axios
                    .get(`${API}/business/services/`, {
                        params: {
                            business_id: this.selectedBusiness.id,
                        },
                    })
                    .then(({ data }) => {
                        if (data.length !== 0) {
                            this.services = data
                            this.selectedService = data[0]
                            this.$emit('selectedService', data[0])
                        } else {
                            this.services = []
                        }
                    })
                    .catch((e) => console.log(e))
            }
        },
        handleSelectService(service) {
            this.selectedService = service
            this.$emit('selectedService', service)
        },
    },
    mounted() {
        this.fetchServices()
    },
    watch: {
        selectedBusiness: function (newBusiness, oldBusiness) {
            this.fetchServices()
        },
    },
}
</script>

<style>
</style>