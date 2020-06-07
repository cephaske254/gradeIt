function previewFile() {
    const file = document.querySelector('input[type=file]').files[0];
    const reader = new FileReader();
  
    reader.addEventListener("load", function () {
      // convert image file to base64 string
      document.querySelector('body').style.backgroundImage=`url(${reader.result})`
      document.querySelector('body').style.backgroundSize='cover';
    }, false);
  
    if (file) {
      reader.readAsDataURL(file);
    }
}

$(document).ready(function(){

    $('input[name=image][type=file]').on('change', function(){
        previewFile()
    })

    $('input[type=url]').on('blur', function(){
        value = $(this).val()
        if (value.startsWith('https://') ==false & value.startsWith('https://') == false){
        $(this).val('http://'+value)
        }
    })
})