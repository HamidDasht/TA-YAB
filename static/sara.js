//
//var FirstScroll = 0;
//var Lbox_height;
//var Reqs_height;
//
//window.onresize = WindowResize;
//function WindowResize(){
//    FirstScroll = 0;
//    var loginbox = document.querySelector("#MyLogin");
//    var main = document.querySelector("main");
//    loginbox.classList.add("position-fixed");
//    main.classList.add("offset-md-4");
//    MakeLoginBoxChange();
//
//}
//
//window.addEventListener("scroll", MakeLoginBoxChange);
//
//function MakeLoginBoxChange(){
//
//     var requestbox = document.querySelector(".requests");  
//     var requestbox_height = requestbox.offsetHeight;
//     var loginbox = document.querySelector("#MyLogin");
//     var main = document.querySelector("main");
//     
//    if(window.innerWidth > 767){
//     
//         if(requestbox_height - window.scrollY <= 450){
//
//             if(!FirstScroll){
//
//                Lbox_height = loginbox.offsetHeight;
//                Reqs_height = requestbox.offsetHeight;
//                loginbox.classList.remove("position-fixed");
//                main.classList.remove("offset-md-4");
//                FirstScroll = 1;
//             }
//         }
//
//         else if(requestbox_height - window.scrollY > 450 && FirstScroll){
//
//              loginbox.style.marginTop = window.scrollY + 'px';
//         }
//
//        if(requestbox_height - window.scrollY < 450 && FirstScroll){
//
//              loginbox.style.marginTop = Reqs_height - Lbox_height + 40 + 'px';
//        }
//    }
//    else{
//
//        loginbox.classList.remove("position-fixed");
//        main.classList.remove("offset-md-4");
//        loginbox.style.marginTop = '1em';
//    }
//    console.log(requestbox_height);
//    console.log(loginbox.offsetHeight);
//}
//495, 450

//880, 484