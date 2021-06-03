//
//var closebtn = document.querySelector(".close");
//
//closebtn.addEventListener("click", function closealert(){
// 
//    var alert = document.querySelector(".alert");
//    alert.style.background = 'red';
//    alert.style.display = 'none';
//    
//});

//
//setTimeout(function(){
//  document.querySelector(".alert").style.display = "none"; 
// }, 4000);


$('#pills-tab').children('.nav-item').children('.nav-link').click(function(){
    
    $('#pills-tab').children('.nav-item').children('.nav-link').css("background-color", "white");
    $('#pills-tab').children('.nav-item').children('.nav-link').css("border-bottom-color", "white");
//    $(this).css("background-color", "#eee");
    $(this).css("border-bottom-color", "#1bb9b7");
    $(this).css("color", "black");
  

});