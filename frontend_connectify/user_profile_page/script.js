// DOM manipulation code
document.addEventListener("DOMContentLoaded", () => {
  const inviteButton = document.getElementById("invite-button");
  const messageButton = document.getElementById("message-button");
  const shareLinkDiv = document.getElementById("share-link");

  inviteButton.addEventListener("click", () => {
    const shareableLink = `${window.location.origin}/invite?user=new_user_id`;
    shareLinkDiv.innerHTML = `Share this link with your friends: <br> <a href="${shareableLink}" target="_blank">${shareableLink}</a>`;
    shareLinkDiv.style.display = "block";
  });

  messageButton.addEventListener("click", () => {
    window.location.href = "chat.html";
  });
});

// Count increment functions
function addSong() {
  var count = document.getElementById("song-count");
  count.textContent = parseInt(count.textContent) + 1;
}

function addAlbum() {
  var count = document.getElementById("album-count");
  count.textContent = parseInt(count.textContent) + 1;
}

function addPlaylist() {
  var count = document.getElementById("playlist-count");
  count.textContent = parseInt(count.textContent) + 1;
}

var modal = document.getElementById("myModal");
var img = document.querySelector(".profile-img");
var modalImg = document.getElementById("img01");
var captionText = document.getElementById("caption");
var imgUpload = document.getElementById("imgUpload");

img.onclick = function () {
  modal.style.display = "block";
  modalImg.src = this.src;
  captionText.innerHTML = this.alt;
};

var span = document.getElementsByClassName("close")[0];

span.onclick = function () {
  modal.style.display = "none";
};

imgUpload.onchange = function (e) {
  var reader = new FileReader();
  reader.onload = function (event) {
    img.src = event.target.result;
    modalImg.src = event.target.result;
  };
  reader.readAsDataURL(e.target.files[0]);
};

document
  .getElementById("registerForm")
  .addEventListener("submit", function (event) {
    event.preventDefault();

    // Validate form data here

    // If the data is valid, update the username title and redirect to the profile page
    var username = document.getElementById("usernameInput").value;
    document.getElementById("usernameTitle").textContent = username;
    window.location.href = "../Reg_page/reg.html";
  });

// Get the elements
let featuredTracksMessage = document.getElementById("featured-tracks-message");
let albumsMessage = document.getElementById("albums-message");
let recentlyLikedMessage = document.getElementById("recently-liked-message");

// Fetch the data from the Spotify API
// Note: You'll need to replace 'OUR_SPOTIFY_API_TOKEN' with your actual Spotify API token

// Fetch featured tracks
fetch("https://api.spotify.com/v1/me/top/tracks", {
  headers: {
    Authorization: `Bearer OUR_SPOTIFY_API_TOKEN`,
  },
})
  .then((response) => response.json())
  .then((data) => {
    // Update the messages based on the data
    if (data.items.length > 0) {
      featuredTracksMessage.textContent = "Showing your featured tracks...";
      let featuredTracksContainer = document.getElementById(
        "featured-tracks-container"
      );
      data.items.forEach((track) => {
        let trackElement = document.createElement("div");
        trackElement.textContent = track.name; // Assuming 'name' is a property of track. Add the right property here
        featuredTracksContainer.appendChild(trackElement);
      });
    } else {
      featuredTracksMessage.textContent =
        "No featured tracks yet. Start adding your favorite songs!";
    }
  });

// Fetch albums
fetch("https://api.spotify.com/v1/me/albums", {
  headers: {
    Authorization: `Bearer OUR_SPOTIFY_API_TOKEN`,
  },
})
  .then((response) => response.json())
  .then((data) => {
    if (data.items.length > 0) {
      albumsMessage.textContent = "Showing your albums...";
      let albumsContainer = document.getElementById("albums-container");
      data.items.forEach((album) => {
        let albumElement = document.createElement("div");
        albumElement.textContent = album.name; // Assuming 'name' is a property of album. Add the right property here
        albumsContainer.appendChild(albumElement);
      });
    } else {
      albumsMessage.textContent =
        "No albums added yet. Start adding your favorite albums!";
    }
  });

// Fetch recently liked tracks
fetch("https://api.spotify.com/v1/me/tracks", {
  headers: {
    Authorization: `Bearer OUR_SPOTIFY_API_TOKEN`,
  },
})
  .then((response) => response.json())
  .then((data) => {
    if (data.items.length > 0) {
      recentlyLikedMessage.textContent =
        "Showing your recently liked tracks...";
      let recentlyLikedTracksContainer = document.getElementById(
        "recently-liked-tracks-container"
      );
      data.items.forEach((track) => {
        let trackElement = document.createElement("div");
        trackElement.textContent = track.name; // Assuming 'name' is a property of track. Add the right property here
        recentlyLikedTracksContainer.appendChild(trackElement);
      });
    } else {
      recentlyLikedMessage.textContent =
        "No recently liked tracks. Start exploring music and like your favorites!";
    }
  });
