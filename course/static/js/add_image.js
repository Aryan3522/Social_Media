function file(){
    document.getElementById('file_input').addEventListener('change', function(e) {
        console.log(e.target.files); // Logs the FileList object containing the selected files
    });

}
Input_photo = document.querySelector('#custom_file_upload')
preview_card = document.querySelector('#card')
preview_img = document.getElementById('blah');
image_upload_button = document.getElementById('image_upload_button');
preview_img.style = "display: none;"
image_upload_button.style = "display: none;"
preview_card.style = "display: none;"
file_input.onchange = evt => {
    const [file] = file_input.files
    if (file) {
        blah.src = URL.createObjectURL(file)
        image_upload_button.style = "display: block;"
        preview_img.style = "display: flex;"
        preview_card.style = "display: flex;"
        Input_photo.style = "display: none;"
    }
    else{
        preview_card.style = "display: none;"
        Input_photo.style = "display: block;"
        preview_img.style = "display: none;"
    }
  }