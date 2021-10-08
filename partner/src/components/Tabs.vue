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
                    aria-label="Default select example"
                    v-model="selected"
                    @change="handleBusiness"
                >
                    <option
                        v-for="business in businesses"
                        :key="business.id"
                        :value="business"
                    >
                        {{ business.name }}
                    </option>
                </select>
            </li>
        </ul>
    </div>
</template>

<script>
import axios from 'axios'
import { API } from '../common'

export default {
    data() {
        return {
            selected: null,
            businesses: [],
        }
    },
    mounted() {
        axios
            .get(`${API}/business`)
            .then(({ data }) => {
                this.selected = data[0]
                this.businesses = data
            })
            .catch((e) => console.log(data))
    },
    methods: {
        handleBusiness(event) {
            this.$store.dispatch('selectBusiness', this.selected)
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