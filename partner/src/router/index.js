import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'

const routes = [
    {
        path: '/',
        name: 'Home',
        component: Home,
    },
    {
        path: '/about',
        name: 'About',
        component: () => import('../views/About.vue'),
    },
    {
        path: '/auth/login',
        name: 'Login',
        component: () => import('../views/auth/Login.vue'),
    },
    {
        path: '/dashboard',
        name: 'Dashboard',
        component: () => import('../views/Dashboard.vue'),
        meta: { requiresAuth: true },
        children: [
            {
                path: 'overview',
                name: 'Overview',
                component: () => import('../views/dashboard/Overview.vue'),
                meta: { requiresAuth: true },
            },
            {
                path: 'bookings',
                name: 'Bookings',
                component: () => import('../views/dashboard/Bookings.vue'),
                meta: { requiresAuth: true },
            },
            {
                path: 'services',
                name: 'Services',
                component: () => import('../views/dashboard/Services.vue'),
                meta: { requiresAuth: true },
            },
        ],
    },
]

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes,
})

router.beforeEach((to, from, next) => {
    const loggedIn = localStorage.getItem('user')

    if (to.matched.some(record => record.meta.requiresAuth)) {
        // this route requires auth, check if logged in
        // if not, redirect to login page.
        if (!loggedIn) {
            next({
                path: '/auth/login',
                query: { redirect: to.fullPath },
            })
        } else {
            next()
        }
    } else {
        next() // make sure to always call next()!
    }
})

export default router
