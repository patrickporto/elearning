<template>
    <div>
        <v-card class="card--flex-toolbar">
            <v-toolbar dark color="red">
                <v-toolbar-title>{{roomTitle}}</v-toolbar-title>
            </v-toolbar>
            <v-divider></v-divider>
        </v-card>
        <v-card-text>
            <chat-history :chat-log="chatLog" v-on:like="like" v-on:reply="reply" />
            <input type="text" class="message-input" v-model="messageContent" @keyup.enter="send()" placeholder="diga algo..." />
        </v-card-text>
    </div>
</template>

<script>
import History from './History.vue'
import moment from 'moment';


export default {
    props: ['roomName', 'roomTitle', 'papel'],
    data() {
        return {
            messageContent: '',
            chatLog: [],
        }
    },
    components: {
        'chat-history': History,
    },
    mounted() {
        this.chatSocket = new WebSocket(`ws://${window.location.host}/ws/chat/${this.roomName}/`)
        this.chatSocket.onmessage = this.receive.bind(this)
        this.chatSocket.onclose = this.close.bind(this)
    },
    methods: {
        receive(event) {
            const data = JSON.parse(event.data)
            if (data.type == 'chat_like') {
                this.handleLike(data)
            } else {
                this.handleMsg(data)
            }
        },
        handleLike({ messageId, likes }) {
            const messages = this.chatLog.reduce((list, log) => list.concat(log.messages), [])
            const msg = messages.find((msg) => msg.id == messageId)
            msg.likes += likes;
        },
        handleMsg({ type, id, message, sendingDate, author, likes }) {
            const lastChatLog = this.chatLog[this.chatLog.length - 1]
            if (lastChatLog && lastChatLog.type === type && lastChatLog.author.id === author.id) {
                lastChatLog.messages.push({
                    id,
                    content: message,
                    sendingDate,
                    likes,
                })
            } else {
                this.chatLog.push({
                type: type,
                messages: [
                    {
                        id,
                        content: message,
                        sendingDate,
                        likes,
                    }
                ],
                author,
                })
            }
            const objDiv = document.getElementById("history");
            objDiv.scrollTop = objDiv.scrollHeight;
        },
        close(event) {
            console.error('Chat socket closed unexpectedly');
        },
        send() {
            var message = this.messageContent;
            if (!message.trim()) return;
            this.chatSocket.send(JSON.stringify({
                'type': 'chat_message',
                'message': message,
                'sendingDate': moment().format(),
            }));
            this.messageContent = '';
        },
        like(messageId) {
            this.chatSocket.send(JSON.stringify({
                'type': 'chat_like',
                'messageId': messageId,
                'sendingDate': moment().format(),
            }));
        },
        reply(messageId) {
            this.chatSocket.send(JSON.stringify({
                'type': 'chat_add_question',
                'messageId': messageId,
            }));
        }
    }
}
</script>

<style lang="sass">
    .message-input {
        background: #800000;
        border-radius: 4px;
        color: #ffffff;
        overflow-y: auto;
        padding: 5px 15px;
        margin: 8px 0;
        width: 100%;
    }
</style>
