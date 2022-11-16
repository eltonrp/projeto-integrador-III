<script setup>

import AppHeader from "./components/AppHeader/AppHeader.vue"
import AppContent from "./components/AppContent/AppContent.vue";
// import AppFooter from "./components/AppFooter/AppFooter.vue";

</script>

<template>
    <main class="default-template">

        <AppHeader />
        
        <AppContent>
            
            <slot />

        </AppContent>
        
        <!-- <AppFooter /> -->

    </main>
</template>

<style lang="scss" scoped>

.default-template {

    display: flex;
    flex-direction: column;
    height: 100vh;

}

</style>