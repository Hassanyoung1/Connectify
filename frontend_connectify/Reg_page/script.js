document.addEventListener("DOMContentLoaded", () => {
  const registerForm = document.getElementById("registerForm");

  if (registerForm) {
    registerForm.addEventListener("submit", (e) => {
      e.preventDefault();
      // Add our form submission logic here
      alert("Registration form submitted!");
    });
  }
});

document
  .getElementById("registerForm")
  .addEventListener("submit", function (event) {
    event.preventDefault();

    // Validate form data here

    // If the data is valid, redirect to the profile page
    window.location.href = "../user_profile_page/index.html";
  });

function onSignIn(googleUser) {
  var profile = googleUser.getBasicProfile();
  console.log("ID: " + profile.getId());
  console.log("Name: " + profile.getName());
  console.log("Image URL: " + profile.getImageUrl());
  console.log("Email: " + profile.getEmail());

  // Populate the form fields with the user's info
  var emailField = document.querySelector('.input-box input[type="email"]');
  if (emailField) {
    emailField.value = profile.getEmail();
  }

  alert("Google Sign-In successful!");
}

function signOut() {
  var auth2 = gapi.auth2.getAuthInstance();
  auth2.signOut().then(function () {
    console.log("User signed out.");
    alert("User signed out.");
  });
}
