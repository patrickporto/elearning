
import Vue from 'vue/dist/vue';
import Message from './components/Message.vue'
import History from './components/History.vue'


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
      const { message } = JSON.parse(event.data);
      this.chatLog.push({
        content: message,
        profileImg: 'https://placeimg.com/192/192/people',
      })
      const objDiv = document.getElementById("history");
      objDiv.scrollTop = objDiv.scrollHeight;
    },
    close(event) {
      console.error('Chat socket closed unexpectedly');
    },
    send() {
      var message = this.messageInput;
      this.chatSocket.send(JSON.stringify({
          'message': message
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
