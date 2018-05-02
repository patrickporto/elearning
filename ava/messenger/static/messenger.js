
import Vue from 'vue/dist/vue';


const app = new Vue({
  data: {
    roomName: 'aula',
    messageInput: ''
  },
  data: {
    roomName: 'aula',
    messageInput: ''
  },
  created() {
    this.chatSocket = new WebSocket(`ws://${window.location.host}/ws/chat/${this.roomName}/`)
    this.chatSocket.onmessage = this.receive.bind(this)
    this.chatSocket.onclose = this.close.bind(this)
  },
  methods: {
    receive(event) {
      var data = JSON.parse(event.data);
      var message = data['message'];
      document.querySelector('#chat-log').value += (message + '\n');
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
