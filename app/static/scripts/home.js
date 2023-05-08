// $() is used for selecting items in the DOM




$(document).ready(function(){
    $("#hide").click(function(){
        $(this).hide();
        });
    

    $('#update').click(function(){
        
        const xhr = new XMLHttpRequest();
        const container = document.getElementById('container');
        
        xhr.onload = function() {
            if (this.status === 200) {
                    container.innerHTML = xhr.responseText;
                } else {
                    console.warn('Did not recieve 200 response code.')
                }};
        xhr.open('get', '/hobbies');
        xhr.send();
    });
    
    
    
        // $.getJSON('/card', {
        //     // Parameters to pass thru
        // }, function(data) {
        //     $('#card-heading').text(data['card-heading']);
        //     document.getElementById('card-image').src=data['card-image'];
        //     $('#card-description').text(data['card-description'])
        //     });
        // });  
});

function navbarToggle() {
    var x = document.getElementById("nav-bar-list");
    if (x.style.display === "block") {
      x.style.display = "none";
    } else {
      x.style.display = "block";
    }
  }


// xhr.onload = function() {
//     if (this.status === 200) {
//         container.innerHTML = xhr.responseText;
//     } else {
//         console.warn('Did not recieve 200 response code.')
//     }

// }


// xhr.open('get', '/hobbies');
// xhr.send();




// var loc = window.location.pathname;
// var dir = loc.substring(0, loc.lastIndexOf('/'));

// console.log(loc)
// console.log(dir)