var button_addon1 = document.querySelector("#button-addon1");
var question_table = document.querySelector("tbody");
var question_input = document.querySelector("#question_input");
var k = 6;

button_addon1.addEventListener("click", function(){
   
    if(question_input.value){    

        tr = document.createElement('tr');
        tr.classList.add('alert');
        tr.classList.add('alert-dismissible');
        tr.classList.add('fade');
        tr.classList.add('show');
        tr.setAttribute("role", "alert");
        
        td = document.createElement('td');
        td.setAttribute("scope", "row");
        
        div = document.createElement('div');
        div.classList.add('custom-control');
        div.classList.add('custom-checkbox');
        
        button = document.createElement('button');
        button.setAttribute("type", "button");
        button.classList.add("close");
        button.setAttribute("data-dismiss", "alert");
        
        span = document.createElement('span');
        span.setAttribute("aria-hidden", "true");
        span.innerHTML = '&times;';
        
        input = document.createElement('input');
        input.setAttribute("type", "checkbox");
        input.classList.add('custom-control-input');
        input.setAttribute("id", "customCheck" + k);
        
        label = document.createElement('label');
        label.classList.add('custom-control-label');
        label.setAttribute("for", "customCheck" + k);
        label.innerHTML = question_input.value;

        button.appendChild(span);
        div.appendChild(button);
        div.appendChild(input);
        div.appendChild(label);
        td.appendChild(div);
        tr.appendChild(td);
        question_table.appendChild(tr);
        
        k = k + 1;
        question_input.value = '';
    }
    
    
});
  
$('input:checkbox').change(function(){
    
    var label = $("label[for='" + $(this).attr('id') + "']");  
    if($(this).is(":checked")) {
        
        label.removeClass('text-muted');
    } else {
        label.addClass('text-muted');
    }
});


