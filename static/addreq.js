var AoutoTimeSelection = document.querySelector('#inlineRadio1');
var HandTimeSelection = document.querySelector('#inlineRadio2');
var division_time = document.querySelector('#division-time');

AoutoTimeSelection.addEventListener("click", function(){
    
    division_time.style.display = 'inherit';
    
});

HandTimeSelection.addEventListener("click", function(){
    
    division_time.style.display = 'none';
    
});



function GetTime(minute, hour){
    
    var t = parseInt(hour);
    if(minute > 0 && minute <= 15)
        t += 0.25;
    else if(minute > 15 && minute <=30)
        t += 0.5;
    else if(minute > 30 && minute <= 59)
        t += 0.75;

    return t;
    
}

$('#add-btn').click(function(){
    
    var t1= document.querySelector('#Time1').value;
    var t2 = document.querySelector('#Time2').value;
    var starttime = GetTime(t1[3] + t1[4] , t1[0] + t1[1]);
    var endtime = GetTime(t2[3] + t2[4] , t2[0] + t2[1]);
    var day = document.querySelector('#Day').value;
    var CourseName = document.querySelector('#CourseName').value;
    
    if(starttime >= endtime){
        $('#time-error').css('display', 'inherit');
    }
    

    let colspan = (endtime - starttime) * 4;
    starttime = (starttime - 8) * 4 + 1;
    endtime = (endtime - 8) * 4;

    for(let x = starttime; x <= endtime; x++){

        let td = document.getElementById(day + '-' + x);

        console.log(day + '-' + x);
        if( x < endtime ){
            console.log(day + '-' + x);
            td.remove();
        }

        else{
            
            if (starttime < endtime){
                $.ajax({type:'POST', url:"add_time", data: {csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val(), Time1:t1,
        Time2:t2, Day:day}});
            }
            
            td.style.backgroundColor = 'rgba(179,217,255, .3)';
            td.setAttribute('colspan',colspan);
            let p =document.createElement('small');
            p.innerHTML = CourseName;
            p.style.textAlign = 'center';
            td.appendChild(p);
        }
    }           

});

$('#time-error').children('.close').click(function(){
    
    $('#time-error').css('display', 'none');
    
});
    
var days = new Array("day", "sat", "sun", "mon", "tu", "wed");
var fa = new Array("روز / ساعت", "شنبه", "یکشنبه", "دوشنبه", "سه شنبه", "چهارشنبه");
var time = document.getElementById('time');

for(var i=0; i<6; i++){

    let tr = document.createElement('tr');
    let th = document.createElement('th');

    th.style.border = '1px solid #ced4da';


    th.innerHTML = fa[i];
    tr.appendChild(th);
    time.appendChild(tr);

    if( i == 0 ){

        var t = 8;
        for(var j=1; j<13; j++){
            let th = document.createElement('th');
            th.style.border = '1px solid #ced4da';

            if(t < 10)
                th.innerHTML = '0';
            th.innerHTML += t + ':00' + '<br/>';

            if(t < 9)
                th.innerHTML += '0';    
            th.innerHTML += (t+1) + ':00';

            t += 1;
            th.setAttribute('colspan', '4');
            th.style.lineHeight = '200%';
            tr.appendChild(th);
        }
    }
    else{

        for(var j=1; j<49; j++){
            let td = document.createElement('td');
            td.setAttribute('id', days[i]+ '-' + j);
            if(j==48){
                td.style.borderLeft = '1px solid #ced4da';
            }
            tr.appendChild(td);
        }
    }
}
