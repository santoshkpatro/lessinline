<template>
    <div class="container">
        <Tabs />
        <router-view></router-view>
    </div>
</template>

<script>
import Tabs from '@/components/Tabs.vue'

export default {
    name: 'Dashboard',
    components: {
        Tabs,
    },
}
</script>

<style>
</style>