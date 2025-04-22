function validatePassword() {
    const password = document.getElementById('password').value;
    const confirmPassword = document.getElementById('Confirm_password').value;

    if (password !== confirmPassword) {
        alert("Passwords do not match!");
        return false; // Prevent form submission
    }
    return true; // Allow form submission
}
