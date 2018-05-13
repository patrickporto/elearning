<template>
    <div>
        <div class="row">
            <chat-history :chat-log="chatLog" />
        </div>
        <div class="row">
            <v-text-field
                v-model="messageContent"
                @keyup.enter="send()"
                max="120"
                full-width
                multi-line
                single-line>
            </v-text-field>
        </div>
    </div>
</template>

<script>
import History from './History.vue'
import moment from 'moment';


export default {
    props: ['roomName'],
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
        const { type, message, sendingDate, author } = JSON.parse(event.data)
        const lastChatLog = this.chatLog[this.chatLog.length - 1]
        if (lastChatLog && lastChatLog.type === type && lastChatLog.author.id === author.id) {
            lastChatLog.messages.push({
            content: message,
            sendingDate: sendingDate,
            })
        } else {
            this.chatLog.push({
            type: type,
            messages: [
                {
                content: message,
                sendingDate: sendingDate,
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
          'message': message,
          'sendingDate': moment().format(),
      }));
      this.messageContent = '';
    }
  }
}
</script>
