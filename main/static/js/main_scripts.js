


function previewFile() {
  const file = document.querySelector('input[type=file]').files[0];
  const reader = new FileReader();

  reader.addEventListener("load", function () {
    // convert image file to base64 string
    document.querySelector('body').style.backgroundImage = `url(${reader.result})`
    document.querySelector('body').style.backgroundSize = 'cover';
  }, false);

  if (file) {
    reader.readAsDataURL(file);
  }
}

$(document).ready(function () {

  $('input[name=image][type=file]').on('change', function () {
    previewFile()
  })

  $('input[type=url]').on('blur', function () {
    value = $(this).val()
    if (value.startsWith('https://') == false & value.startsWith('https://') == false) {
      $(this).val('http://' + value)
    }
  })

  $('input[type=range]').on('input', function () {
    display = $(this).parent().find('span.display')
    display.html(parseFloat($(this).val()).toFixed(2))
    console.log(display)
  })

  $('.grade_it').click(function () {
    target = $($(this).attr('data-target'))
    json_data = JSON.parse(target.attr('data-json'))
    article_id = json_data['pk']
    image_url = '/media/' + json_data['fields']['image']

    $('.display_image').css({
      'background': `url(${image_url})`,
      'background-size': 'cover',
      'background-position': 'center',
      'background-repeat': 'no-repeat',
      'border-radius': '10px'
    })


    $('.article_rating_cont form input[name=article]').val(article_id)
    setTimeout(() => {
      $('.article_rating_cont').slideDown()
    }, 200);
  })



  $('.data-item').each(function (item) {
    width = parseFloat($(this).attr('data-width') * 10)
    $(this).css({
      'transition': '1s',
      'width': `${width}%`
    })

  })



  var prevScrollpos = window.pageYOffset;
  window.onscroll = function () {
    var currentScrollPos = window.pageYOffset - 150;
    if (prevScrollpos > currentScrollPos) {
      $("#info_bar").css({'transition':"2s","top":"0" })
    } else {
      $("#info_bar").css({'transition':"1s","top":"-500px" })
    }
  }
})