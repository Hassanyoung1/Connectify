document.addEventListener("DOMContentLoaded", () => {
  const socket = io();

  // User button functionality
  document.querySelectorAll(".user-button").forEach((button) => {
    button.addEventListener("click", (e) => {
      const username = button.getAttribute("data-username");
      document.getElementById("chat-username").innerText = username;
      document.getElementById("chat-window").innerHTML = "";
    });
  });

  // Message sending functionality
  const sendButton = document.getElementById("send-button");
  sendButton.addEventListener("click", () => {
    let message = document.getElementById("chat-input").value;
    if (message.trim()) {
      // Emit the message to the server
      socket.emit('message', message);
      // We no longer directly append the message here since it should be broadcasted by the server
      document.getElementById("chat-input").value = ''; // Clear input after sending
    }
  });

  // Listen for incoming messages
  socket.on('message', (msg) => {
    const messageElement = document.createElement("div");
    messageElement.classList.add("message", "received");
    messageElement.textContent = msg;
    document.getElementById("chat-window").appendChild(messageElement);
    document.getElementById("chat-window").scrollTop = document.getElementById("chat-window").scrollHeight;
  });

  // Emoji picker functionality
  const emojiButton = document.getElementById("emoji-button");
  const emojiPicker = document.getElementById("emoji-picker");

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

const audioPlayer = document.getElementById("music-player");
const musicUpload = document.getElementById("music-upload");
const songTitle = document.getElementById("song-title");
const artistName = document.getElementById("artist-name");
const albumArt = document.querySelector(".music-info img");
const playButton = document.getElementById("play-button");
const pauseButton = document.getElementById("pause-button");
const prevButton = document.getElementById("prev-button");
const nextButton = document.getElementById("next-button");
const progressBar = document.getElementById("progress-bar");
const volumeControl = document.getElementById("volume-control");

let currentTrackIndex = 0;
let tracks = [];

musicUpload.addEventListener("change", (event) => {
  const files = Array.from(event.target.files);
  console.log("files", files);
  tracks = files.map((file) => ({
    file,
    url: URL.createObjectURL(file),
    title: file.name.split("-")[0],

    // title: file.name.split(".").slice(0, -1).join("."),
    // artist: "Unknown Artist",
  }));

  currentTrackIndex = 0;
  loadTrack(currentTrackIndex);
});

playButton.addEventListener("click", () => {
  audioPlayer.play();
  playButton.style.display = "none";
  pauseButton.style.display = "block";
});

pauseButton.addEventListener("click", () => {
  audioPlayer.pause();
  playButton.style.display = "block";
  pauseButton.style.display = "none";
});

prevButton.addEventListener("click", () => {
  currentTrackIndex = (currentTrackIndex - 1 + tracks.length) % tracks.length;
  loadTrack(currentTrackIndex);
  audioPlayer.play();
});

nextButton.addEventListener("click", () => {
  currentTrackIndex = (currentTrackIndex + 1) % tracks.length;
  loadTrack(currentTrackIndex);
  audioPlayer.play();
});

audioPlayer.addEventListener("ended", () => {
  nextButton.click();
});

audioPlayer.addEventListener("timeupdate", () => {
  const progress = (audioPlayer.currentTime / audioPlayer.duration) * 100;
  progressBar.value = progress || 0;
});

progressBar.addEventListener("input", () => {
  const seekTime = (progressBar.value / 100) * audioPlayer.duration;
  audioPlayer.currentTime = seekTime;
});

volumeControl.addEventListener("input", () => {
  audioPlayer.volume = volumeControl.value / 100;
});

function loadTrack(index) {
  const track = tracks[index];
  audioPlayer.src = track.url;
  songTitle.textContent = track.title;
  artistName.textContent = track.artist;
  albumArt.src = "https://via.placeholder.com/80";
}
