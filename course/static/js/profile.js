function toggleLogoutModal() {
    var modal = document.getElementById('logoutModal');
    modal.style.display = modal.style.display === 'flex' ? 'none' : 'flex'; 
    if (modal.style.display === 'flex') {
        modal.classList.add('active'); 
    } else {
        modal.classList.remove('active'); 
    }
}
