<script setup>



</script>

<template>
    <header class="app-header">

        <Icon class="icon" symbol="recycle" />
        <h1 class="title">Descate de Óleo Inteligente</h1>
        <p>Encontre um ponto de coleta de óleo próximo a você!</p>

    </header>
</template>

<style lang="scss" scoped>

.app-header {

    background-color: #f4f8fb;
    padding: 4rem 0 14rem 0;
    text-align: center;

    > .icon {
        
        fill: var(--theme-color);
        font-size: 4rem;
        
    }
    
    > .title { margin: 1rem 0 .5rem 0 }
    p { margin: 0 }

}

</style>