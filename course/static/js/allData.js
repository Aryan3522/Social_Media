document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("skeleton-loader").style.display = "none";
});

function toggleDeleteModal() {
    var modal = document.getElementById('deleteModal');
    modal.style.display = modal.style.display === 'flex' ? 'none' : 'flex'; 
    if (modal.style.display === 'flex') {
        modal.classList.add('active'); 
    } else {
        modal.classList.remove('active'); 
    }
}

function confirmDelete(recordId) {
    document.getElementById('deleteId').innerText = recordId;
    document.getElementById('deleteModal').style.display = 'block';
    toggleDeleteModal();
}

function deleteRecord() {
    const recordId = document.getElementById('deleteId').innerText;
    window.location.href = "/delete/" + recordId;
}
