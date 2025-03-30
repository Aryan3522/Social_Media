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
    modal.setAttribute("aria-hidden", "false"); // Update aria-hidden for accessibility
}

function closePostModal() {
    const modal = document.getElementById("postModal");
    modal.style.display = "none";
    modal.setAttribute("aria-hidden", "true"); // Update aria-hidden for accessibility
}
