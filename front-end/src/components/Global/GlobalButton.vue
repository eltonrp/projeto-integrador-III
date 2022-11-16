<script setup>

import { computed } from "vue"

const props = defineProps({
    
    type: {
        type: String,
        default: 'button'
    },
    label: String,
    icon: String,
    description: String,
    color: {
        type: String,
        default: 'primary'
    }

})

const buttonClass = computed(() => [
    'button',
    `--${props.color}`
])

const title = computed(() => props.description || props.label)

</script>

<template>
    <button
        :type="type"
        :class="buttonClass"
        :title="title"
    >
        
        <span v-if="icon" class="icon">
            <Icon :symbol="icon" />
        </span>
        
        <span v-if="label" class="label">{{ label }}</span>

    </button>
</template>

<style lang="scss" scoped>

.button {

    align-items: stretch;
    background-color: var(--primary-color);
    border-radius: 3px;
    color: #fff;
    fill: #fff;
    display: flex;
    overflow: hidden;
    padding: 0;
    position: relative;

    &.--primary { background-color: var(--primary-color) }
    &.--secondary { background-color: var(--secondary-color) }
    &.--success { background-color: var(--success-color) }
    &.--danger { background-color: var(--danger-color) }
    &.--warning { background-color: var(--warning-color) }
    &.--info { background-color: var(--info-color) }
    &.--light { background-color: var(--light-color) }
    &.--dark { background-color: var(--dark-color) }
    
    &.--light {
        
        color: var(--font-color);
        fill: var(--font-color);

    }
        
    &.--link {

        background-color: transparent;
        color: var(--font-color);
        fill: var(--font-color);

        &:hover {

            color: var(--theme-color);
            fill: var(--theme-color);

        }

        &::after { background-color: transparent; }

    }

    &::after {

        background-color: #fff;
        content: '';
        display: block;
        height: 100%;
        opacity: 0;
        position: absolute;
        pointer-events: none;
        transition: all .1s linear;
        width: 100%;

    }

    &:hover::after { opacity: .3; }

    > .icon {

        align-items: center;
        display: flex;
        height: 2rem;
        padding: 0 .5rem;
        
        svg {  }

    }

    > .label {

        background-color: rgba(0, 0, 0, .1);
        flex-grow: 1;
        height: 2rem;
        padding: .5rem .8rem;

    }

}

</style>