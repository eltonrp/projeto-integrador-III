<script setup>

import { ref, computed } from 'vue'
import { useStore } from 'vuex'

const store = useStore()

const loading = ref(true)
const search = ref('')

const points = computed(() => store.getters['points/getAll'].filter(point => {

    return point.name.toLowerCase().includes(search.value.toLowerCase())

}))

const getPoints = async () => {
    
    await store.dispatch('points/getPoints')
    
    loading.value = false
}

getPoints()

const deletePoint = async (id) => {
    
    if(confirm(`Deseja realmente excluir o ponto de coleta #${id}?`)) {
        
        loading.value = true

        await store.dispatch('points/deletePoint', id)

        getPoints()

    }

}

</script>

<template>
    <div class="points-list">

        <label class="search" v-if="!loading">
            <span class="icon">
                <Icon symbol="search" />
            </span>
            <input class="search-field" type="text" placeholder="Pesquisar..." v-model="search" />
        </label>

        <ul class="list" v-if="!loading">
            <li class="item" v-for="(point, index) in points" :key="index">
                <div>
                    <a class="show-in-map" href="javascript:void(0)">
                        <Icon symbol="geo-alt-fill" />
                    </a>
                </div>
                <div class="details">
                    <p class="id">#{{ point.id }}</p>
                    <p class="name"><strong>{{ point.name }}</strong></p>
                    <p class="address">{{ point.address }} - {{ point.cep }}</p>
                    <p class="phonenumber" v-if="point.phone">
                        <Icon symbol="telephone" /> {{ point.phone }}
                    </p>
                </div>
                <div class="buttons">
                    <Button label="Editar" icon="pencil" />
                    <Button label="Excluir" icon="dash-circle" color="danger" @click="deletePoint(point.id)" />
                </div>
            </li>
        </ul>

        <p class="empty" v-if="!loading && points.length == 0"><Icon symbol="exclamation-triangle" /> Nenhum ponto de coleta localizado.</p>

        <div class="loading" v-if="loading">
            <Loading />
        </div>

    </div>
</template>

<style lang="scss" scoped>

.points-list { position: relative }

.search {

    align-items: center;
    border-bottom: 1px solid #f4f8fb;
    display: flex;
    position: sticky;
    top: 0;
    z-index: 5;

    > .icon {
        
        fill: var(--theme-color);
        font-size: 1.2rem;
        margin: 0 2rem;

    }

    > .search-field {

        border: 0 none;
        border-radius: 3px;
        flex-grow: 1;
        padding: 1rem 1rem 1rem 0;

        &:focus { outline: none }

    }

}

.list {

    background-color: #fff;
    margin: 0;
    padding: 0 2rem;

    > .item {

        align-items: center;
        border-bottom: 1px solid #efefef;
        display: flex;
        list-style: none;
        margin-bottom: 0;
        padding: 2rem 0;

        > .details {

            flex-grow: 1;

            p { margin: 0 0 .4rem 0 }

            > .id {
                
                color: #999;
                font-size: 0.8rem;
                
            }

            .name {
                
                font-size: 1.2rem;
                font-weight: 700;
                
            }

        }

        > .buttons {

            display: flex;
            flex-direction: column;
            gap: 5px;

        }

        .show-in-map {

            fill: var(--theme-color);
            font-size: 2rem;
            padding: 0 3rem;

        }

    }

}

.empty {

    margin: 0;
    padding: 5rem 0;
    text-align: center;

}

.loading {

    align-items: center;
    display: flex;
    justify-content: center;
    height: 300px;

}

</style>