<template>
    <div class="container">
        <div
            class="flex flex-column"
            style="
                max-width: 400px;
                margin: 200px auto;
                min-height: 60vh;
                text-align: center;
                justify-content: center;
                padding: 16px;
            "
        >
            <h2>Login</h2>
            <form @submit.prevent="handleLogin">
                <div class="form-floating mb-3">
                    <input
                        type="email"
                        class="form-control"
                        id="floatingInput"
                        placeholder="name@example.com"
                        v-model="credentials.email"
                    />
                    <label for="floatingInput">Email address</label>
                </div>
                <div class="form-floating">
                    <input
                        type="password"
                        class="form-control"
                        id="floatingPassword"
                        placeholder="Password"
                        v-model="credentials.password"
                    />
                    <label for="floatingPassword">Password</label>
                </div>
                <div class="d-grid mt-4">
                    <button class="btn btn-dark" type="submit">Login</button>
                </div>
            </form>
        </div>
    </div>
</template>

<script>
import { API } from '../../common'
import axios from 'axios'

export default {
    name: 'Login',
    data() {
        return {
            credentials: {
                email: null,
                password: null,
            },
            error: null,
        }
    },
    methods: {
        handleLogin() {
            axios
                .post(`${API}/auth/login/`, this.credentials)
                .then(({ data }) => {
                    this.$store.dispatch('login', data)
                    if (this.$route.query.redirect) {
                        this.$router.push(this.$route.query.redirect)
                    } else {
                        this.$router.push({ name: 'Home' })
                    }
                })
                .catch((e) => console.log(e))
        },
    },
}
</script>

<style>
</style>