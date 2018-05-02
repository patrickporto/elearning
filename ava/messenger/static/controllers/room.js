import { Controller } from 'stimulus';
import { application } from '../messenger.js'


class RoomController extends Controller {
  static targets = [ "name", "messageInput" ]

  connect() {
    const roomName = parseInt(this.data.get("name"))
    this.chatSocket = new WebSocket(`ws://${window.location.host}/ws/chat/${roomName}/`)
    this.chatSocket.onmessage = this.receive.bind(this)
    this.chatSocket.onclose = this.close.bind(this)
  }

  receive(event) {
    var data = JSON.parse(event.data);
    console.log(data)
    var message = data['message'];
    document.querySelector('#chat-log').value += (message + '\n');
  }

  close(event) {
    console.error('Chat socket closed unexpectedly');
  }

  send() {
    var message = this.messageInputTarget.value;
    this.chatSocket.send(JSON.stringify({
        'message': message
    }));

    this.messageInputTarget.value = '';
  }

  enter(event) {
    if (event.keyCode === 13) {
      this.send()
    }
  }
}

application.register('room', RoomController)
