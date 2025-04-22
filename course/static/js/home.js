console.log("Home.js Loaded successfully");

function togglePostModal() {
    const modal = document.getElementById("postModal");
    if (modal.style.display === "block") {
        closePostModal();
    } else {
        openPostModal();
    }
}

function openPostModal() {
    const modal = document.getElementById("postModal");
    modal.style.display = "block";
    modal.setAttribute("aria-hidden", "false");
}

function closePostModal() {
    const modal = document.getElementById("postModal");
    modal.style.display = "none";
    modal.setAttribute("aria-hidden", "true");
    document.getElementById("postContent").value = "";
}

// WritePostModal
function toggleWritePostModal() {
    const modal = document.getElementById("writePostModal");
    if (modal.style.display === "block") {
        closeWritePostModal();
    } else {
        openWritePostModal();
    }
}

function openWritePostModal() {
    const modal = document.getElementById("writePostModal");
    modal.style.display = "block";
    modal.setAttribute("aria-hidden", "false");
}

function closeWritePostModal() {
    const modal = document.getElementById("writePostModal");
    modal.style.display = "none";
    modal.setAttribute("aria-hidden", "true");
    document.getElementById("postContent").value = "";
}

// function toggleDeleteModal() {
//     var modal = document.getElementById('deleteModal');
//     modal.style.display = modal.style.display === 'flex' ? 'none' : 'flex'; 
//     if (modal.style.display === 'flex') {
//         modal.classList.add('active'); 
//     } else {
//         modal.classList.remove('active'); 
//     }
// }

// function confirmDelete(imageId) {
//     document.getElementById('deleteId').innerText = imageId;
//     document.getElementById('deleteModal').style.display = 'block';
//     toggleDeleteModal();
// }

// function deleteRecord() {
//     const imageId = document.getElementById('deleteId').innerText;
//     window.location.href = "/delete_post/" + imageId;
// }

document.addEventListener("DOMContentLoaded", function() {
    // Initialize all required elements
    const imagePreviewContainer = document.getElementById("imagePreviewContainer");
    const photoButton = document.getElementById("AddphotoButton");
    // const photoInput = document.getElementById("photoInput");
    const container = document.querySelector('.container');
    const postsContainer = document.getElementById("postsContainer");
    const postModal = document.getElementById("postModal");
    
    if (!imagePreviewContainer || !photoButton || !container || !postsContainer || !postModal) {
        console.error('Required DOM elements not found');
        return;
    }

    photoButton.addEventListener("click", function() {
        document.getElementById("AddphotoButton").addEventListener("click", function() {
    location.href = 'add_img';})
    });

   
});
