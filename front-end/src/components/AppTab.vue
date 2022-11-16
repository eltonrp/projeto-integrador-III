<script setup>

import PointsList from './PointsList.vue'
import GoogleMaps from './GoogleMaps.vue'

import { ref } from 'vue'

let activeTab = ref('points')

const changeTab = (tab) => activeTab.value = tab

</script>

<template>
    <main class="app-tab">

        <ul class="tabs">
            <li class="tab-button">
                <a href="javascript:void(0)" title="Mapa" @click="changeTab('map')" :class="{ 'active': activeTab == 'map' }">
                    <span>Mapa</span>
                </a>
            </li>
            <li class="tab-button">
                <a href="javascript:void(0)" title="Pontos de Coleta" @click="changeTab('points')" :class="{ 'active': activeTab == 'points' }">
                    <span>Pontos de Coleta</span>
                </a>
            </li>
        </ul>

        <section class="tab-content" v-if="activeTab == 'map'">

            <GoogleMaps />

        </section>

        <section class="tab-content --points" v-if="activeTab == 'points'">

            <PointsList />

        </section>

    </main>
</template>

<style lang="scss" scoped>

.app-tab {

    margin: -10rem auto 5rem auto;
    max-width: 900px;

    > .tabs {

        display: flex;
        flex-direction: row;
        gap: 1px;
        margin: 0;
        padding: 0;

        > .tab-button {

            flex-grow: 1;
            list-style: none;
            width: 50%;

            > a {

                background-color: #fff;
                border: 1px solid transparent;
                color: #777;
                display: block;
                font-weight: 700;
                text-align: center;
                padding: 2rem 0;
                text-transform: uppercase;

                > span {

                    border-bottom: 4px solid transparent;
                    padding-bottom: .3rem;

                }

                &:hover {

                    color: var(--theme-color);
                    text-decoration: none;

                }

                &.active {

                    color: var(--theme-color);
                    
                    > span { border-bottom-color: var(--theme-color); }

                }

            }

        }

    }

    > .tab-content {

        background-color: #fff;
        max-height: 70vh;
        overflow: auto;

        &.--points { margin-top: 1px }

    }

}

</style>