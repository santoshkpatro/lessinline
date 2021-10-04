import http from 'k6/http'
import { check, group, sleep, fail } from 'k6'

export let options = {
    vus: 1, // 1 user looping for 1 minute
    duration: '1m',

    thresholds: {
        http_req_duration: ['p(99)<1500'], // 99% of requests must complete below 1.5s
    },
}

const BASE_URL = 'http://127.0.0.1:8000/api'
const EMAIL = 'santoshkumarpatro23@gmail.com'
const PASSWORD = '12345'

export default () => {
    let loginRes = http.post(`${BASE_URL}/auth/login/`, {
        email: EMAIL,
        password: PASSWORD,
    })

    check(loginRes, {
        'logged in successfully': (resp) => resp.json('access_token') !== '',
    })

    let authHeaders = {
        headers: {
            Authorization: `Bearer ${loginRes.json('access_token')}`,
        },
    }

    let myObjects = http.get(`${BASE_URL}/auth/profile/`, authHeaders).json()
    check(myObjects, { 'retrieved crocodiles': (obj) => obj.length > 0 })

    sleep(1)
}
