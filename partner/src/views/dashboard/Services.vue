<template>
    <div class="row">
        <div class="col-8">
            <h5>Services</h5>
            <div class="me-5" v-if="services.length !== 0">
                <div
                    class="card my-2"
                    :class="{ active: service === selectedService }"
                    v-for="service in services"
                    :key="service.id"
                    @click="handleSelectService(service)"
                >
                    {{ service.name }}
                    <p>Description</p>
                    {{ service.description }}

                    <div class="card-body row">
                        <div
                            class="card col-4"
                            v-for="slot in service.slots"
                            :key="slot.id"
                        >
                            <p>slot</p>
                            {{ slot.start_time }} - {{ slot.end_time }}
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <div class="col-4">
            <h5>Create a new service</h5>
        </div>
    </div>
</template>

<script>
import { mapGetters } from 'vuex'
import axios from 'axios'
import { API } from '@/common'

export default {
    name: 'Services',
    data() {
        return {
            services: [],
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