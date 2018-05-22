<template>
    <div id="history" class="history-container">
        <chat-message v-for="(item, index) in chatLog" :key="index" :type="item.type"
            :messages="item.messages" :author="item.author" :sending-date="item.sendingDate" v-on:like="like" v-on:reply="reply"  />
    </div>
</template>

<script>
import Message from './Message.vue'

export default {
    props: ['chatLog'],
    components: {
        'chat-message': Message,
    },
    methods: {
        like(msg) {
            this.$emit('like', msg)
        },
        reply(msg) {
            this.$emit('reply', msg)
        }
    }
}
</script>

<style lang="sass">
    .history-container {
        background: #ffffff;
        height: 75vh;
        overflow-y: auto;
    }
</style>
