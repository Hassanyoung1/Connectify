document.addEventListener("DOMContentLoaded", () => {
  const registerForm = document.getElementById("registerForm");

  if (registerForm) {
    registerForm.addEventListener("submit", (e) => {
      e.preventDefault();

      var username = e.target[0].value;
      var email = e.target[1].value;
      var password = e.target[2].value;
      var confirmPassword = e.target[3].value;

      fetch("http://localhost:5000/register", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          username: username,
          email: email,
          password: password,
          confirmPassword: confirmPassword,
        }),
      })
        .then((response) => response.json())
        .then((data) => {
          if (data.success) {
            window.location.href = "../user_profile_page/index.html";
          } else {
            console.log(data.message);
          }
        });
    });
  }
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
