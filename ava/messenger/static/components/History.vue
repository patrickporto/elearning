<template>
    <div id="history" class="history-container">
        <slot></slot>
    </div>
</template>

<script>
export default {}
</script>

<style lang="sass">
    $background-color: #F7F7F7;

    .history {
        &-container {
            height: 75vh;
            overflow-y: auto;
        }
    }
</style>
