document.addEventListener("DOMContentLoaded", () => {
  const loginForm = document.getElementById("loginForm");

  if (loginForm) {
    loginForm.addEventListener("submit", (e) => {
      e.preventDefault();

      const email = loginForm.querySelector('input[type="email"]').value;
      const password = loginForm.querySelector('input[type="password"]').value;

      fetch("/login", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ email, password }),
      })
      .then((response) => response.json())
      .then((data) => {
        if (data.message) {
          console.log(data.message);
          // Redirect to the profile page or perform other actions upon successful login
        } else if (data.error) {
          console.error(data.error);
          // Handle errors, such as displaying a message to the user
        }
      })
      .catch((error) => {
        console.error('Error:', error);
      });
    });
  }
});
