<template>
    <div>
        <ul class="nav">
            <li class="nav-item">
                <router-link
                    class="nav-link"
                    aria-current="page"
                    :to="{ name: 'Overview' }"
                    >Overview</router-link
                >
            </li>
            <li class="nav-item">
                <router-link class="nav-link" :to="{ name: 'Bookings' }"
                    >Bookings</router-link
                >
            </li>
            <li class="nav-item">
                <a class="nav-link" href="#">Services</a>
            </li>
            <li class="nav-item">
                <select
                    class="form-select"
                    v-model="choosenBusiness"
                    @change="handleSelectBusiness(this.value)"
                >
                    <option
                        :value="business"
                        v-for="business in businesses"
                        :key="business.id"
                    >
                        {{ business.name }}
                    </option>
                </select>
            </li>
        </ul>
    </div>
</template>

<script>
import { mapGetters } from 'vuex'

export default {
    computed: {
        ...mapGetters(['businesses', 'selectedBusiness']),
    },
    data() {
        return {
            choosenBusiness: null,
        }
    },
    methods: {
        handleSelectBusiness(event) {
            this.$store.dispatch('selectBusiness', this.choosenBusiness)
        },
    },
}
</script>

<style scoped>
li a {
    text-decoration: none;
    color: black;
}
.router-link-active {
    border-bottom: 2px solid black;
}
</style>