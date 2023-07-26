
var i = 0;
var speed = 50;

function submitOnEnter(event) {
  if (event.which === 13 && !event.shiftKey) {
      if (!event.repeat) {
          const newEvent = new Event("submit", {cancelable: true});
          event.target.form.dispatchEvent(newEvent);
      }
  }
}

document.getElementById("chatbox").addEventListener("keydown", submitOnEnter);


// typewriter animation
function typeWriter(text) {
  if (i < text.length) {
    document.getElementById("chat").innerHTML += text.charAt(i);
    i++;
    setTimeout(typeWriter, speed);
  }
}
