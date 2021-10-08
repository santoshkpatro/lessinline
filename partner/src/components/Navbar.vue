<template>
    <nav class="navbar navbar-expand-lg navbar-light">
        <div class="container">
            <router-link class="navbar-brand" :to="{ name: 'Home' }"
                >LessInLine</router-link
            >
            <button
                class="navbar-toggler"
                type="button"
                data-bs-toggle="collapse"
                data-bs-target="#navbarSupportedContent"
                aria-controls="navbarSupportedContent"
                aria-expanded="false"
                aria-label="Toggle navigation"
            >
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarSupportedContent">
                <ul class="navbar-nav me-auto mb-2 mb-lg-0">
                    <li class="nav-item">
                        <router-link
                            class="nav-link active"
                            aria-current="page"
                            :to="{ name: 'About' }"
                            >About</router-link
                        >
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="#">Link</a>
                    </li>
                </ul>
                <ul class="navbar-nav">
                    <li class="nav-item mx-2" v-if="!loggedIn">
                        <router-link
                            class="btn btn-dark btn-sm"
                            :to="{ name: 'Login' }"
                        >
                            <svg
                                xmlns="http://www.w3.org/2000/svg"
                                width="20"
                                height="20"
                                fill="currentColor"
                                class="bi bi-person-fill"
                                viewBox="0 0 20 20"
                            >
                                <path
                                    d="M3 14s-1 0-1-1 1-4 6-4 6 3 6 4-1 1-1 1H3zm5-6a3 3 0 1 0 0-6 3 3 0 0 0 0 6z"
                                />
                            </svg>
                            LOGIN
                        </router-link>
                    </li>
                    <li class="nav-item mx-2" v-if="!loggedIn">
                        <button class="btn btn-dark btn-sm">
                            <svg
                                xmlns="http://www.w3.org/2000/svg"
                                width="20"
                                height="20"
                                fill="currentColor"
                                class="bi bi-person-plus-fill"
                                viewBox="0 0 20 20"
                            >
                                <path
                                    d="M1 14s-1 0-1-1 1-4 6-4 6 3 6 4-1 1-1 1H1zm5-6a3 3 0 1 0 0-6 3 3 0 0 0 0 6z"
                                />
                                <path
                                    fill-rule="evenodd"
                                    d="M13.5 5a.5.5 0 0 1 .5.5V7h1.5a.5.5 0 0 1 0 1H14v1.5a.5.5 0 0 1-1 0V8h-1.5a.5.5 0 0 1 0-1H13V5.5a.5.5 0 0 1 .5-.5z"
                                />
                            </svg>
                            CREATE ACCOUNT
                        </button>
                    </li>
                    <li class="nav-item mx-2" v-if="loggedIn">
                        <button
                            class="btn btn-dark btn-sm"
                            @click="this.$store.dispatch('logout')"
                        >
                            <svg
                                xmlns="http://www.w3.org/2000/svg"
                                width="20"
                                height="20"
                                fill="currentColor"
                                class="bi bi-person-dash-fill"
                                viewBox="0 0 20 20"
                            >
                                <path
                                    fill-rule="evenodd"
                                    d="M11 7.5a.5.5 0 0 1 .5-.5h4a.5.5 0 0 1 0 1h-4a.5.5 0 0 1-.5-.5z"
                                />
                                <path
                                    d="M1 14s-1 0-1-1 1-4 6-4 6 3 6 4-1 1-1 1H1zm5-6a3 3 0 1 0 0-6 3 3 0 0 0 0 6z"
                                />
                            </svg>
                            LOGOUT
                        </button>
                    </li>
                </ul>
            </div>
        </div>
    </nav>
</template>

<script>
import { mapGetters } from 'vuex'

export default {
    name: 'Navbar',
    computed: {
        ...mapGetters(['loggedIn']),
    },
}
</script>

<style>
</style>