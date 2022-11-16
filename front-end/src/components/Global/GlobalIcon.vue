<script setup>

import { computed } from "vue";

const props = defineProps({
    
    symbol: String

})

const href = computed(() => `${new URL('../../assets/icons.svg', import.meta.url).href}#${props.symbol}`)

</script>

<template>
    <svg class="icon">
        <use :xlink:href="href" />
    </svg>
</template>

<style lang="scss" scoped>

.icon {
    display: inline-block;
    fill: inherit;
    height: 1em;
    transition: all .1s linear;
    vertical-align: top;
    width: 1em;
}

</style>