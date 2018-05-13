<template>
    <div id="history" class="history-container">
        <chat-message v-for="(item, index) in chatLog" :key="index" :type="item.type"
            :messages="item.messages" :author="item.author" :sending-date="item.sendingDate" />
    </div>
</template>

<script>
import Message from './Message.vue'

export default {
    props: ['chatLog'],
    components: {
        'chat-message': Message,
    }
}
</script>

<style lang="sass">
    .history {
        &-container {
            height: 75vh;
            overflow-y: auto;
        }
    }
</style>
