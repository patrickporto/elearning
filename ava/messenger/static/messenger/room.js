import { Controller } from 'stimulus';
import { application } from '../app.js'


application.register("hello", class extends Controller {
  static get targets() {
    return [ "name", "output" ]
  }
  greet() {
    this.outputTarget.textContent =
      `Hello, ${this.nameTarget.value}!`
  }
})
