application.register("hello", class extends Stimulus.Controller {
  static get targets() {
    return [ "name", "output" ]
  }
  greet() {
    this.outputTarget.textContent =
      `Hello, ${this.nameTarget.value}!`
  }
})
