<script setup>

const props = defineProps({
    color: {
        default: 'theme',
        type: String
    },
    size: {
        default: 'medium',
        type: String
    }
})

</script>

<template>
    <div class="global-loading">

        <div :class="['spinner', `--color-${props.color}`, `--size-${props.size}`]"></div>

    </div>
</template>

<style lang="scss" scoped>



.global-loading {

    align-items: center;
    display: flex;
    justify-content: center;

}

.spinner {

    animation: spinner .5s linear infinite;
    border: 3px solid var(--theme-color);
    border-top-color: transparent;
    border-radius: 50%;
    height: 2rem;
    width: 2rem;

    &.--color-white {
        
        border-color: #fff;
        border-top-color: transparent;
        
    }

    &.--size-small {
        
        height: 1rem;
        width: 1rem;

    }

}

@keyframes spinner {

    0% { transform: rotate(0deg); }
    100% { transform: rotate(360deg); }

}

</style>