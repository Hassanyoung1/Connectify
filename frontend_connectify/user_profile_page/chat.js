let musicQueue = [];
let currentTrackIndex = 0;

document
  .getElementById("music-upload")
  .addEventListener("change", async (event) => {
    const files = Array.from(event.target.files);
    if (files.length > 0) {
      musicQueue = files;
      currentTrackIndex = 0;
      playTrack(files[currentTrackIndex]);
    }
  });

async function playTrack(file) {
  const audioElement = document.getElementById("music-player");
  const songTitleElement = document.getElementById("song-title");
  const artistNameElement = document.getElementById("artist-name");
  const albumArtElement = document.getElementById("album-art");

  // Load the audio file
  const objectUrl = URL.createObjectURL(file);
  audioElement.src = objectUrl;
  audioElement.play();

  try {
    // Read metadata
    const metadata = await musicMetadata.parseBlob(file);

    // Update song title and artist name
    const title = metadata.common.title || "Unknown Title";
    const artist = metadata.common.artist || "Unknown Artist";
    songTitleElement.textContent = title;
    artistNameElement.textContent = artist;

    // Update album art
    if (metadata.common.picture && metadata.common.picture.length > 0) {
      const picture = metadata.common.picture[0];
      const blob = new Blob([picture.data], { type: picture.format });
      const albumArtUrl = URL.createObjectURL(blob);
      albumArtElement.src = albumArtUrl;
    } else {
      albumArtElement.src = "https://via.placeholder.com/80"; // Default image if no album art
    }
  } catch (error) {
    console.error("Error reading metadata:", error);
    songTitleElement.textContent = "Song";
    artistNameElement.textContent = "";
    albumArtElement.src = "https://via.placeholder.com/80"; // Default image if error
  }
}

document.getElementById("music-player").addEventListener("ended", () => {
  playNextTrack();
});

document.getElementById("prev-button").addEventListener("click", () => {
  playPreviousTrack();
});

document.getElementById("next-button").addEventListener("click", () => {
  playNextTrack();
});

function playPreviousTrack() {
  if (currentTrackIndex > 0) {
    currentTrackIndex--;
    playTrack(musicQueue[currentTrackIndex]);
  }
}

function playNextTrack() {
  if (currentTrackIndex < musicQueue.length - 1) {
    currentTrackIndex++;
    playTrack(musicQueue[currentTrackIndex]);
  }
}

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
  document.getElementById("music-player").play();
});

pauseButton.addEventListener("click", () => {
  pauseButton.style.display = "none";
  playButton.style.display = "block";
  document.getElementById("music-player").pause();
});
