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



$('.accept_button').click(function() {
    $.ajax(  
      {
      url : "accept_reply",
      type : 'GET',
      dataType: 'json',
      data: {
          csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val(),
            id : $(this).attr('value')
        },
      success: function(json_resp)
      {
          let accept_button = "#accept" + json_resp.reply_id;
          let reject_button = "#reject" + json_resp.reply_id;

          $(accept_button).attr('disabled','true');
          $(accept_button).text('پذیرفته شده');
          $(accept_button).append(' <i class="far fa-handshake"></i>');
          $(reject_button).remove();
          $(accept_button).removeClass('accept_button');

          // Update buttons in bookmarked aira if exists (if is bookmarked)
          try {
            let bk_accept_button = "#bk-accept" + json_resp.reply_id;
            let bk_reject_button = "#bk-reject" + json_resp.reply_id;
            $(bk_accept_button).attr('disabled','true');
            $(bk_accept_button).text('پذیرفته شده');
            $(bk_accept_button).append(' <i class="far fa-handshake"></i>');
            $(bk_reject_button).remove();
            $(bk_accept_button).removeClass('accept_button');
          }
          catch(err) {
            
          }
      }
      
    });
  });

  
  $('.bookmark-reply').click(function() {
    let clicked_element = $(this);
    let action;
    if (clicked_element.hasClass('in-bookmark-aria'))
        action = 'delete';
    else
        action = 'add';
    $.ajax(
    {
        url : 'bookmark_reply',
        type : 'POST',
        dataType: 'json',
        data: {csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val(),
        id : $(this).attr('value'),
        action: action},
        success: function(json_resp)
        {
          if (json_resp.status == "removed")
          {
              if (clicked_element.hasClass("in-bookmark-aria"))
              {
                  clicked_element.closest("tbody").remove();
              }
          }
        }   
    });
});
  
$('.reject_button').click(function() {
    $.ajax(  
      {
      url : "reject_reply",
      type : 'GET',
      dataType: 'json',
      data: {
          csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val(),
            id : $(this).attr('value')
        },
      success: function(json_resp)
      {
          let accept_button = "#accept" + json_resp.reply_id;
          let reject_button = "#reject" + json_resp.reply_id;

          $(reject_button).attr('disabled','true');
          $(reject_button).text('رد شده');
          $(reject_button).append(' <i class="fas fa-handshake-slash"></i>');
          $(accept_button).remove();
          $(reject_button).removeClass('reject_button');

          try{
            let accept_button = "#bk-accept" + json_resp.reply_id;
            let reject_button = "#bk-reject" + json_resp.reply_id;

            $(reject_button).attr('disabled','true');
            $(reject_button).text('رد شده');
            $(reject_button).append(' <i class="fas fa-handshake-slash"></i>');
            $(accept_button).remove();
            $(reject_button).removeClass('reject_button');
          }
          catch(err)
          {

          }
      }
      
    });
  });

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

window.onload = WindowResize;

window.onresize = WindowResize;
function WindowResize(){

    $('#pills-tab').children('.nav-item').children('.nav-link').css("background-color", "white");
    $('#pills-tab').children('.nav-item').children('.nav-link').css("border-bottom-color", "white");

    $('#pills-tab').children('.nav-item').children('.active').css("border-bottom-color", "#1bb9b7");
    $('#pills-tab').children('.nav-item').children('.active').css("color", "balck");
}

$('.req-rmv-btn').click(function() {
  $.ajax(  
    {
    url : "delete_request",
    type : 'POST',
    dataType: 'json',
    data: {
        csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val(),
          id : $(this).attr('value')
      },
    success: function(json_resp)
    {
      window.location.replace(location.pathname);
    }
    
  });
});