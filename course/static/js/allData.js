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

// function showDeleteModal(id) {
//     document.getElementById('deleteId').innerText = id; 
//     document.getElementById('btn_logout').href = "{% url 'delete' __ID__ %}".replace('__ID__', id);
//     toggleDeleteModal(); 
// }