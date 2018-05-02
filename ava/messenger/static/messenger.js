
import Vue from 'vue/dist/vue';
import moment from 'moment';
import VueMoment from 'vue-moment'
import Message from './components/Message.vue'
import History from './components/History.vue'


Vue.use(VueMoment)


const app = new Vue({
  data: {
    roomName: 'aula',
    messageInput: ''
  },
  data: {
    roomName: 'aula',
    messageInput: '',
    chatLog: [],
  },
  components: {
    'chat-message': Message,
    'chat-history': History,
  },
  created() {
    this.chatSocket = new WebSocket(`ws://${window.location.host}/ws/chat/${this.roomName}/`)
    this.chatSocket.onmessage = this.receive.bind(this)
    this.chatSocket.onclose = this.close.bind(this)
  },
  methods: {
    receive(event) {
      const { message, sendingDate, author } = JSON.parse(event.data)
      const lastChatLog = this.chatLog[this.chatLog.length - 1]
      if (lastChatLog && lastChatLog.author.id === author.id) {
        lastChatLog.messages.push({
          content: message,
          sendingDate: sendingDate,
        })
      } else {
        this.chatLog.push({
          messages: [
            {
              content: message,
              sendingDate: sendingDate,
            }
          ],
          author,
        })
      }
      console.log(author.me)
      const objDiv = document.getElementById("history");
      objDiv.scrollTop = objDiv.scrollHeight;
    },
    close(event) {
      console.error('Chat socket closed unexpectedly');
    },
    send() {
      var message = this.messageInput;
      this.chatSocket.send(JSON.stringify({
          'message': message,
          'sendingDate': moment().format(),
      }));
      this.messageInput = '';
    },
    enter(event) {
      if (event.keyCode === 13) {
        this.send()
      }
    }
  }
}).$mount('#messenger')
