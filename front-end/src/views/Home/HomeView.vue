<script setup>

import AppHeader from '@/components/AppHeader.vue'
import AppTab from '@/components/AppTab.vue'
import AppFooter from '@/components/AppFooter.vue'
import NewPoint from '@/components/NewPoint.vue'

</script>

<template>
    <div class="home-view">

        <AppHeader />

        <Container>

            <AppTab />

        </Container>

        <NewPoint />

        <AppFooter />

    </div>
</template>

<style lang="scss" scoped>

.home-view {

    display: block;
    margin: 0 auto;

}

</style>