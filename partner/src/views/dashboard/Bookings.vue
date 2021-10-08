<template>
    <div>
        <div class="row mt-5">
            <div class="col-9">
                <div>
                    <div
                        class="card"
                        v-for="booking in bookings"
                        :key="booking.ID"
                    >
                        <div class="card-body">
                            <div class="row">
                                <div class="col-4 border-2 border-end">
                                    Status -
                                    <span class="badge bg-dark">{{
                                        booking.status
                                    }}</span>
                                    <p>Date - booking Date</p>
                                </div>
                                <div class="col-8">
                                    <p>User Details</p>
                                    Name: {{ booking.user.first_name }}
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="col-3">
                <ServiceList @selectedService="handleSelectService" />
            </div>
        </div>
    </div>
</template>

<script>
import ServiceList from '@/components/dashboard/ServiceList'
import axios from 'axios'
import { API } from '@/common'

export default {
    components: {
        ServiceList,
    },
    data() {
        return {
            service: null,
            bookings: null,
        }
    },
    methods: {
        handleSelectService(service) {
            this.service = service
            this.fetchBookings()
        },
        fetchBookings() {
            if (this.service !== null) {
                axios
                    .get(`${API}/business/bookings/`, {
                        params: {
                            service_id: this.service.id,
                        },
                    })
                    .then(({ data }) => (this.bookings = data))
                    .catch((e) => console.log(e))
            } else {
                this.bookings = []
            }
        },
    },
    mounted() {
        this.fetchBookings()
    },
}
</script>

<style>
</style>