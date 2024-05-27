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
