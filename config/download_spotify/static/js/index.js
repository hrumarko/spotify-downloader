
download_button.classList.remove('hide');
document.querySelector('.spinner').classList.add('hide')

// download_button = document.querySelector('.download-btn')
// download_button.addEventListener('click', function(){
//   download_button.classList.add('hide');
//   document.querySelector('.spinner').classList.remove('hide')
// })


function check_file(url) {
   $.ajax({
    type: 'HEAD',
    url: url,
    success: function() {
      console.log('yra')
      document.querySelector('.spinner').classList.add('hide')   
    },  
    error: function() {
      setTimeout(check_file(url, fil), 10000);
    }
})
}


function getCookie(name) {
    // get csrftoken
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
