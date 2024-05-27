document.querySelectorAll(".user-button").forEach((button) => {
  button.addEventListener("click", (e) => {
    const username = button.getAttribute("data-username");
    document.getElementById("chat-username").innerText = username;
    document.getElementById("chat-window").innerHTML = "";
  });
});

const sendButton = document.getElementById("send-button");
const chatInput = document.getElementById("chat-input");
const chatWindow = document.getElementById("chat-window");
const emojiButton = document.getElementById("emoji-button");
const emojiPicker = document.getElementById("emoji-picker");
const playButton = document.getElementById("play-button");
const pauseButton = document.getElementById("pause-button");

sendButton.addEventListener("click", () => {
  const message = chatInput.value;
  if (message.trim()) {
    const messageElement = document.createElement("div");
    messageElement.classList.add("message", "sent");
    messageElement.textContent = message;
    chatWindow.appendChild(messageElement);
    chatInput.value = "";
    chatWindow.scrollTop = chatWindow.scrollHeight;
  }
});

emojiButton.addEventListener("click", () => {
  emojiPicker.style.display =
    emojiPicker.style.display === "flex" ? "none" : "flex";
});

document.querySelectorAll(".emoji-picker button").forEach((button) => {
  button.addEventListener("click", () => {
    chatInput.value += button.textContent;
    chatInput.focus();
    emojiPicker.style.display = "none";
  });
});

document.addEventListener("click", (e) => {
  if (!emojiButton.contains(e.target) && !emojiPicker.contains(e.target)) {
    emojiPicker.style.display = "none";
  }
});

playButton.addEventListener("click", () => {
  playButton.style.display = "none";
  pauseButton.style.display = "block";
  // Add play functionality here
});

pauseButton.addEventListener("click", () => {
  pauseButton.style.display = "none";
  playButton.style.display = "block";
  // Add pause functionality here
});
