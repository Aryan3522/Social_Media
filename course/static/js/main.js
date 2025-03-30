const passwordField = document.getElementById("password")

function validatePasswords() {
    const password = document.getElementById('password').value;
    const confirmPassword = document.getElementById('Confirm_password').value;
    if (password !== confirmPassword) {
      document.getElementById('Signup_alert_modal_alert').innerText = "Passwords do not match!";
      document.getElementById('Signup_alert_modal').style.display = 'block'; // Show the modal

      // Hide the modal after 3 seconds
      setTimeout(() => {
        document.getElementById('Signup_alert_modal').style.display = 'none'; // Hide the modal after 3 seconds
      }, 5000);

      return false; // Prevent form submission
    }
    return true; // Allow form submission
  }

const handleMouseMove = event => {
    if (!document.querySelector("#password:is(:focus)") && !document.querySelector("#password1:is(:focus)") && !document.querySelector("#password:is(:user-invalid)")) {
        const eyes = document.getElementsByClassName('eye')
  
        for (let eye of eyes) {
               const x = eye.getBoundingClientRect().left + 10;
               const y = eye.getBoundingClientRect().top + 10;
               const rad = Math.atan2(event.pageX - x, event.pageY - y);
               const rot = (rad * (180 / Math.PI) * -1) + 180;
        
               eye.style.transform = `rotate(${rot}deg)`;
            }
    }
}

const handleFocusPassword = event => {
    document.getElementById('face').style.transform = 'translateX(30px)'
    const eyes = document.getElementsByClassName('eye')

    for (let eye of eyes) {
        eye.style.transform = `rotate(100deg)`;
     }
}

const handleFocusOutPassword = event => {
    document.getElementById('face').style.transform = 'translateX(0)'
    if(event.target.checkValidity()) {
        document.getElementById('ball').classList.toggle('sad')
    } else {
        document.getElementById('ball').classList.toggle('sad')
        const eyes = document.getElementsByClassName('eye')
  
        for (let eye of eyes) {
               eye.style.transform = `rotate(215deg)`;
            }
    }
}


document.addEventListener("mousemove", event => handleMouseMove(event))
passwordField.addEventListener('focus', event => handleFocusPassword(event))
passwordField.addEventListener('focusout', event => handleFocusOutPassword(event))

document.getElementById('submit').addEventListener("mouseover", event => document.getElementById('ball').classList.toggle('look_at'))
document.getElementById('submit').addEventListener("mouseout", event => document.getElementById('ball').classList.toggle('look_at'))
