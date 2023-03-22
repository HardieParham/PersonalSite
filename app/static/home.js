// $ is a placeholder for saying 'jQuery'

// $(function() {
//     $('#update').bind('click', function() {
//         $.getJSON('/get_info', {
//             page_name: 'home'
//         }, function(data) {
//             $('#title').text(data.title);
//             $('#main').text(data.main);
//             });
//         });
//       return false;
//     });


// $(document).ready(function(){
//     $.getJSON('/get_info', {
//         page_name: 'home'
//     }, function(data) {
//         $('#title').text(data.title);
//         $('#main').text(data.main);
//         });
//     });


// Once page is loaded call this function
$(document).ready(function(){

    // If hide link is clicked, call this function
    $("#hide").click(function(){

        // Hide the update button
        $(this).hide();
        
        });
    
    // If update link is clicked, call this function (better way of doing above function)
    $('#update').click(function(){

        // Get JSON data from this link
        $.getJSON('/card', {

            // Parameters to pass thru
            //page_name: 'home'

        // On return run this function
        }, function(data) {

            // Set the title to the new data value
            $('#card-heading').text(data['card-heading']);

            // Set the main tedxt to the new data value
            //$('#card-image').text(data.card-image);
            // function changeImage(a) {
            document.getElementById('card-image').src=data['card-image'];

            //$('#card-image').src = data['card-image'];

            $('#card-description').text(data['card-description'])

            });
        
        });
    
    });

