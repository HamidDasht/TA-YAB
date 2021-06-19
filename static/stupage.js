
//
//var replayslink = document.querySelector("#replays-link");
//var requestlink = document.querySelector("#request-link");
//var Replayscard = document.querySelector("#Replayscard");
//var RequestExplianation = document.querySelector("#Requests");
//var page_counter = document.querySelector("#page-counter");
//
//replayslink.addEventListener("click", function(){
//    
//    replayslink.firstElementChild.classList.add("active");
//    requestlink.firstElementChild.classList.remove("active");
//    Replayscard.style.display = 'inherit';
//    RequestExplianation.style.display = 'none';
//    page_counter.style.display = 'none';
//    
//});
//
//requestlink.addEventListener("click", function(){
//   
//    requestlink.firstElementChild.classList.add("active");
//    replayslink.firstElementChild.classList.remove("active");
//    RequestExplianation.style.display = 'inherit';
//    Replayscard.style.display = 'none';
//    page_counter.style.display = 'inherit';
//    
//});

$('.fa-bookmark').click(function(){
    
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

$(function()
{
    
    /*
         
        // for bootstrap 3 use 'shown.bs.tab', for bootstrap 2 use 'shown' in the next line
        $('a[data-toggle="pill"]').on('shown.bs.tab', function (e) {
            // save the latest tab; use cookies if you like 'em better:
            localStorage.setItem('lastTab', $(this).attr('href'));
        });
    
        // go to the latest tab, if it exists:
        var lastTab = localStorage.getItem('lastTab');
        if (lastTab) 
        {
            $('[href="' + lastTab + '"]').tab('show');
        }
        
        if (lastTab == '#pills-profile' )
        {
            $('#pills-tab').children('.nav-item').children('.nav-link').css("background-color", "white");
            $('#pills-tab').children('.nav-item').children('.nav-link').css("border-bottom-color", "white");
            tab.css("border-bottom-color", "#1bb9b7");
            tab.css("color", "black");
        }

        $(window).load();
        //$("#pills-tabContent").removeStyle('display');
    */
           
            
});

$('#pills-tab').children('.nav-item').children('.nav-link').click(function(){
    
    $('#pills-tab').children('.nav-item').children('.nav-link').css("background-color", "white");
    $('#pills-tab').children('.nav-item').children('.nav-link').css("border-bottom-color", "white");
//  $(this).css("background-color", "#eee");
    $(this).css("border-bottom-color", "#1bb9b7");
    $(this).css("color", "black");
  

});
$('#msg-modal-body').children('table').children('tbody').children('tr').children('td').click(function(){
    

    $('#chat-modal-header').css("display", "inherit");
    $('#chat-modal-body').css("display", "inherit");
    $('#chat-modal-footer').css("display", "inherit");
    
    $('#msg-modal-header').css("display", "none");
    $('#msg-modal-body').css("display", "none");
    
});

$('#chat-modal-header').children('.right-msg').children('.fa-angle-left').click(function(){
    

    $('#chat-modal-header').css("display", "none");
    $('#chat-modal-body').css("display", "none");
    $('#chat-modal-footer').css("display", "none");
    
    $('#msg-modal-header').css("display", "inherit");
    $('#msg-modal-body').css("display", "inherit");
    
});
//
//$('.p-text').css('background', 'green');
window.onload = WindowResize;

window.onresize = WindowResize;
function WindowResize(){

    $('#pills-tab').children('.nav-item').children('.nav-link').css("background-color", "white");
    $('#pills-tab').children('.nav-item').children('.nav-link').css("border-bottom-color", "white");

    $('#pills-tab').children('.nav-item').children('.active').css("border-bottom-color", "#1bb9b7");
    $('#pills-tab').children('.nav-item').children('.active').css("color", "balck");
    
    if(window.innerWidth > 1200){
        
        $('.alert').children('p').css('width', String( window.innerWidth - $('.leftside')[0].offsetWidth - $('.profile')[0].offsetWidth - 300) + 'px');
        $('.p-text').css('width', String( window.innerWidth - $('.leftside')[0].offsetWidth - $('.profile')[0].offsetWidth - 260) + 'px');    
    }
    else if (window.innerWidth > 767){
        
        $('.alert').children('p').css('width', String( window.innerWidth - $('.leftside')[0].offsetWidth - $('.profile')[0].offsetWidth - 220) + 'px');
        $('.p-text').css('width', String( window.innerWidth - $('.leftside')[0].offsetWidth - $('.profile')[0].offsetWidth - 180) + 'px');
    }
    else{
        
        $('.alert').children('p').css('width', String( $('.leftside')[0].offsetWidth - 140) + 'px');
        $('.p-text').css('width', String( $('.leftside')[0].offsetWidth - 100) + 'px');
    }

}

$('.bookmark-request').click(function() {
    $.ajax(
    {
        url : 'bookmark_request',
        type : 'POST',
        dataType: 'json',
        data: {csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val(),id : $(this).attr('value')},
        success: function(json_resp){
        }   
    });
});

$('.send_rep').click(function() {
  $.ajax(  
    {
    url : 'sendrep',
    type : 'GET',
    dataType: 'json',
    data: {csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val(),id : $(this).attr('value')},
    success: function(json_resp){
        $('.alltimes').remove();
        document.getElementById("send_rep_button").hidden=false
        message_area = document.getElementById("message-text").disabled=false
        message_area = document.getElementById("message-text").innerHTML=""
        if (json_resp.status == "200")
        {
        //var resp = JSON.parse(json_resp);
        document.getElementById("recipient-name").value = json_resp.course_name;
        //document.getElementById("recipient-name").value = json_resp.times[0];
        //$('#recipient-name').value(resp)
        //all_times = document.getElementsByClassName('alltimes')
        //if (all_times)
          //  all_times.remove()
            
        let form = document.getElementById("myform");
        if (json_resp.number_of_timings == 0)
        {
            let div = document.createElement('div');
            div.classList.add("custom-control");
            div.classList.add("alltimes");

            let inp = document.createElement('p');
            lbl = document.createElement('label');
            lbl.innerHTML = "هیچ ساعت مشخص شده ای وجود ندارد"

            div.appendChild(inp);
            div.appendChild(lbl);
            form.appendChild(div);
        }
        for (var i = 0; i < json_resp.number_of_timings;i++)
        {
            let div = document.createElement('div');
            div.classList.add("custom-control");
            div.classList.add("custom-checkbox");
            div.classList.add("alltimes");

            let inp = document.createElement('input');
            inp.setAttribute('type', 'checkbox');
            inp.setAttribute('id', 'time' + i)
            inp.setAttribute('name', 'time' + i)
            inp.setAttribute('value', json_resp.times[i])
            inp.classList.add("custom-control-input");
            lbl = document.createElement('label');
            lbl.classList.add("custom-control-label");
            lbl.setAttribute('for', 'time' + i)
            lbl.innerHTML = json_resp.times[i]

            div.appendChild(inp);
            div.appendChild(lbl);
            form.appendChild(div);
        }
        }
        else if (json_resp.status == "403")
        {
            document.getElementById("send_rep_button").hidden=true
            document.getElementById("recipient-name").value = json_resp.course_name
            message_area = document.getElementById("message-text")
            message_area.innerHTML = json_resp.reply_text
            message_area.disabled = true
            
            let form = document.getElementById("myform");
            if (json_resp.number_of_timings == 0)
            {
                let div = document.createElement('div');
                div.classList.add("custom-control");
                div.classList.add("alltimes");

                let inp = document.createElement('p');
                lbl = document.createElement('label');
                lbl.innerHTML = "هیچ ساعت مشخص شده ای وجود ندارد"

                div.appendChild(inp);
                div.appendChild(lbl);
                form.appendChild(div);
            }
            for (var i = 0; i < json_resp.number_of_timings;i++)
            {
                let div = document.createElement('div');
                div.classList.add("custom-control");
                div.classList.add("custom-checkbox");
                div.classList.add("alltimes");

                let inp = document.createElement('input');
                inp.setAttribute('type', 'checkbox');
                inp.setAttribute('id', 'time' + i);
                inp.setAttribute('name', 'time' + i);
                inp.setAttribute('value', json_resp.times[i]);
                inp.setAttribute('disabled', true);
                inp.classList.add("custom-control-input");
                lbl = document.createElement('label');
                lbl.classList.add("custom-control-label");
                lbl.setAttribute('for', 'time' + i)
                lbl.innerHTML = json_resp.times[i]

                div.appendChild(inp);
                div.appendChild(lbl);
                form.appendChild(div);
            }

        }
    }
  });
});
//   $.ajax(  
//     {
//     url : 'sendrep',
//     type : 'GET',
//     dataType: 'json',
//     data: {csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()},
//     success: function(json_resp){
//         //var resp = JSON.parse(json_resp);
//         //var resp = JSON.parse("{'course_name': 'پایگاه داده 2 - محمودزاده', 'number_of_timings': '1', 'start_time1': '18:10:00', 'end_time1': '19:10:00', 'day1': '5'}")
//         document.getElementById("recipient-name").value = json_resp.number_of_timings;
//         //$('#recipient-name').value(resp)
//     }
    
//   });
// });


//#007bff
//$('.alert').hover(function(){
//    
//    $(this).removeClass('alert-primary'); 
//    $(this).addClass('alert-info');      
//
//
//});
//$('.alert').mouseout(function(){
//    
//    $(this).removeClass('alert-info');
//    $(this).addClass('alert-primary'); 
//
//
//});



//
//
//var SendReplayCard = document.querySelector("#SendReplayCard");
//
//window.onresize = WindowResize;
//window.onload = WindowResize;
//function WindowResize(){
//        
//      
//    if(window.innerWidth >= 1200){
//        
//        SendReplayCard.style.width = '44.5%';
//        SendReplayCard.style.right = '29%';
//        
//    }
//    else if(window.innerWidth >= 992){
//        
//        SendReplayCard.style.width = '45%';
//        SendReplayCard.style.right = '28%';
//    }
//    else if(window.innerWidth >= 768){
//        
//        
//          SendReplayCard.style.width = '61%';
//          SendReplayCard.style.right = '3%';
//    } 
//    else if(window.innerWidth >= 576){
//       
//        
//        SendReplayCard.style.width = '80%';
//        SendReplayCard.style.right = '10%';
//    }
//
//}
//
//
//var cancel_btn = document.querySelectorAll(".cancel-btn");
//
//for(var i=0; i<cancel_btn.length; i++){
//    
//    cancel_btn[i].addEventListener("click", CloseSendReplayCard);
//}
//
//
//function CloseSendReplayCard(){
//    
//    SendReplayCard.style.display = 'none';
//};
//
//var send_btn = document.querySelectorAll(".send-btn");
//
//for(var i=0; i<send_btn.length; i++){
//    
//    send_btn[i].addEventListener("click", OpenSendReplayCard);
//}
//
//
//function OpenSendReplayCard(){
//    
//    SendReplayCard.style.display = 'inherit';
//};

