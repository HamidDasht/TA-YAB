//
//
//var replayslink = document.querySelector("#replays-link");
//var requestlink = document.querySelector("#request-link");
//var Replayscard = document.querySelector("#Replayscard");
//var RequestExplianation = document.querySelector("#RequestExplianation");
//var page_counter = document.querySelector("#page-counter");
//
//replayslink.addEventListener("click", function(){
//    
//    replayslink.firstElementChild.classList.add("active");
//    requestlink.firstElementChild.classList.remove("active");
//    Replayscard.style.display = 'inherit';
//    RequestExplianation.style.display = 'none';
//    page_counter.style.display = 'inherit';
//    
//});
//
//requestlink.addEventListener("click", function(){
//   
//    requestlink.firstElementChild.classList.add("active");
//    replayslink.firstElementChild.classList.remove("active");
//    RequestExplianation.style.display = 'inherit';
//    Replayscard.style.display = 'none';
//    page_counter.style.display = 'none';
//    
//});



$('.fa-bookmark').click(function(){
    
    console.log('sjkas');
    if($(this).hasClass('far')){
        $(this).removeClass('far');
        $(this).addClass('fas');
        $(this).attr('title', 'حذف درخواست');        
    }
    else{
        $(this).removeClass('fas');
        $(this).addClass('far');
        $(this).attr('title', 'ذخیره درخواست');
    }

});

//$('#pills-tab').children('.nav-item').children('.nav-link').click(function(){
//    
//    $('#pills-tab').children('.nav-item').children('.nav-link').css("background-color", "white");
//    $(this).css("background-color", "#eee");
//    $(this).css("color", "black");
//  
//
//});

$('#pills-tab').children('.nav-item').children('.nav-link').click(function(){
    
    $('#pills-tab').children('.nav-item').children('.nav-link').css("background-color", "white");
    $('#pills-tab').children('.nav-item').children('.nav-link').css("border-bottom-color", "white");
//    $(this).css("background-color", "#eee");
    $(this).css("border-bottom-color", "#1bb9b7");
    $(this).css("color", "black");
  

});