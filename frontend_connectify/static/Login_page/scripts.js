document.addEventListener("DOMContentLoaded", () => {
  const loginForm = document.getElementById("loginForm");

  if (loginForm) {
    loginForm.addEventListener("submit", (e) => {
      e.preventDefault();
      console.log("submit button clicked");

      // Get form data
      const formData = new FormData(loginForm);
      const email = formData.get("email");
      const password = formData.get("password");  // Retrieve the password from the form data

      if (!email || !password) {
        console.error("Email and password are required");
        return;
      }

      // Send login data to the backend
      fetch("/login", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          email,
          password,
        }),
      })
        .then((response) => response.json())
        .then(() => {
          console.log("Login successful");
          window.location.replace("/");          
        })
        .catch((error) => {
          // Handle login error
          console.error(error);
        });
    });
  }
});
