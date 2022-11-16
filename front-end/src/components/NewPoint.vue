<script setup>

import { ref } from 'vue'
import { useStore } from 'vuex'
import Point from '@/store/model/Point'

const store = useStore()
const point = ref(new Point())
const loading = ref(false)

const insertNewPoint = async () => {
    
    loading.value = true

    await store.dispatch('points/insertNewPoint', point.value)
    await store.dispatch('points/getPoints')

    point.value = new Point()
    
    loading.value = false

}

</script>

<template>
    <form class="new-point" @submit.prevent="insertNewPoint">

        <h2 class="title">Cadastrar novo ponto de coleta</h2>

        <label for="name" class="label">Nome:</label>
        <input id="name" class="field" type="text" placeholder="Nome do ponto de coleta" required v-model="point.name" />

        <label for="cep" class="label">CEP:</label>
        <input id="cep" class="field" type="text" placeholder="00000-000" required v-model="point.cep" />

        <label for="address" class="label">Endereço:</label>
        <input id="address" class="field" type="text" placeholder="Endereço completo do ponto de coleta" required v-model="point.address" />

        <label for="phone" class="label">Telefone:</label>
        <input id="phone" class=" field" type="text" placeholder="(00) 00000-0000" v-model="point.phone" />

        <button :class="['button', {'--loading': loading}]" type="submit" :disabled="loading">
            <span class="button-label">Cadastrar</span>
            <Loading class="loading" size="small" />
        </button>

    </form>
</template>

<style lang="scss" scoped>

.new-point {

    color: #fff;
    margin: 0 auto 5rem auto;
    max-width: 600px;

}

.title {

    margin: 0 0 2rem 0;
    text-align: center;

}

.label {

    display: block;
    margin-bottom: .3rem;

}

.field {

    border: 0 none;
    border-radius: 3px;
    padding: 1rem;
    margin-bottom: 1rem;
    width: 100%;

}

.button {

    background: transparent;
    border: 3px solid #fff;
    border-radius: 3rem;
    color: #fff;
    cursor: pointer;
    display: block;
    font-size: 1.2rem;
    font-weight: 700;
    margin: 1rem auto 0 auto;
    padding: 1rem 2rem;
    position: relative;
    text-transform: uppercase;

    &:hover,
    &.--loading {

        background-color: #fff;
        color: var(--theme-color);

    }

    &.--loading {

        > .button-label { visibility: hidden }
        > .loading { display: flex }

    }

    > .loading {

        height: 100%;
        display: none;
        left: 0;
        position: absolute;
        top: 0;
        width: 100%;

    }

}

</style>