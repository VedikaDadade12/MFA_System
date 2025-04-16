// Toggle Password Visibility
document.querySelectorAll(".togglePassword").forEach((icon) => {
    icon.addEventListener("click", function () {
        let passwordField = this.previousElementSibling;

        if (passwordField.type === "password") {
            passwordField.type = "text";
            this.innerHTML = "&#128065;"; // Open eye icon
        } else {
            passwordField.type = "password";
            this.innerHTML = "&#128064;"; // Closed eye icon
        }
    });
});

// OTP Verification (Only allows 4-digit OTP)
document.getElementById("verifyBtn").addEventListener("click", function () {
    let otpInput = document.getElementById("otpInput").value.trim();
    let errorMsg = document.getElementById("otpError");

    if (!/^\d{4}$/.test(otpInput)) {
        errorMsg.textContent = "⚠ Please enter a valid 4-digit OTP.";
        errorMsg.style.color = "red";
    } else {
        errorMsg.textContent = "";
        alert("✅ OTP Verified Successfully!");
        // Proceed with OTP verification logic here
    }
});
