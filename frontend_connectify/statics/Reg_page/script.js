const passwordValidator = require('password-validator');


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


      console.log("IN JS SCRIPT")
      if (password !== confirmPassword) {
        alert("Passwords do not match");
        return;
      }
      const schema = new passwordValidator();    
      schema
      .is().min(8)                                    // Minimum length 8
      .is().max(100)                                  // Maximum length 100
      .has().uppercase()                              // Must have uppercase letters
      .has().lowercase()                              // Must have lowercase letters
      .has().digits()                                // Must have at least 2 digits
      .has().not().spaces()                           // Should not have spaces
      .is().not().oneOf(['Passw0rd', 'Password123']); // Blacklist these values
      
      // Validate against a password string
      if (!schema.validate(password)) {
        validationDetails = schema.validate(password, { details: true })
        console.log(validationDetails)
        const messages = validationDetails.map((error) => error.message)
        // for (let msg of messages) {
        //     console.log(`${msg}`);
        //     alert(`${msg}`)
        // }
        alert(messages.join('\n'))
        return;
    }
      

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
