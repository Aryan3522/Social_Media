function toggleLogoutModal() {
    var modal = document.getElementById('logoutModal');
    modal.style.display = modal.style.display === 'flex' ? 'none' : 'flex'; 
    if (modal.style.display === 'flex') {
        modal.classList.add('active'); 
    } else {
        modal.classList.remove('active'); 
    }
}
function toggleDeleteModal() {
    var modal = document.getElementById('deleteModal');
    modal.style.display = modal.style.display === 'flex' ? 'none' : 'flex'; 
    if (modal.style.display === 'flex') {
        modal.classList.add('active'); 
    } else {
        modal.classList.remove('active'); 
    }
}

function confirmDelete(imageId) {
    document.getElementById('deleteId').innerText = imageId;
    document.getElementById('deleteModal').style.display = 'block';
    toggleDeleteModal();
}

function deleteRecord() {
    const imageId = document.getElementById('deleteId').innerText;
    window.location.href = "/delete_post/" + imageId;
}
