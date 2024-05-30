document.addEventListener("DOMContentLoaded", () => {
  const registerForm = document.getElementById("registerForm");

  if (registerForm) {
    registerForm.addEventListener("submit", (e) => {
      e.preventDefault();

      // Get form data
      const formData = new FormData(registerForm);
      const username = formData.get("username");
      const email = formData.get("email");
      const password = formData.get("password");
      const confirmPassword = formData.get("confirm_password");

    /*  // Check if password and confirm password match
      if (password !== confirmPassword) {
        console.error("Passwords do not match");
        return;
      }

      if (email === "admin@gmail.com" && password === "user") {
        window.location.replace("/");
      } else {
        alert("Invalid information");
        return;
        'https://' + window.location.hostname + "/"
      }*/

      // Send registration data to the backend
      fetch("/register", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          username,
          email,
          password,
          confirm_password: confirmPassword,
        }),
      })
        .then((response) => response.json())
        .then(() => {
          console.log("Registration successful");
          window.location.replace("/");          
        })
        .catch((error) => {
          // Handle registration error
          console.error(error);
        }); 
    });
  }
});
