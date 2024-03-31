/**
 * function to retrieve html content from a provided URL 
 * @param {String} pageid the URL for JQuery to fetch. Must start with a forward slash. ex: '/home' 
 */
function getPage(pageid){
    //console.log(pageid)
    const xhr = new XMLHttpRequest();
    const container = document.getElementById('content-container');
        
    xhr.onload = function() {
        if (this.status === 200) {
                container.innerHTML = xhr.responseText;
            } else {
                console.warn('Did not recieve 200 response code.')
            }};

    xhr.open('get', pageid);
    xhr.send();
}


/**
 * Function to assign NavBar buttons to their respetive URL's onload of base page.
 */
$(document).ready(function(){
    $('#btn_home').on('click', function(){ getPage('/home')} )
    $('#btn_personal_life').on('click', function(){ getPage('/personal')} )
    $('#btn_work_history').on('click', function(){ getPage('/work')})
    $('#btn_programming').on('click', function(){ getPage('/programming')} )
    $('#btn_contact').on('click', function(){ getPage('/test')} )
});