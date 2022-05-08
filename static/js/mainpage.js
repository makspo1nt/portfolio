function myFunction() {
    if (document.getElementsByClassName('todo_list')[0].style['display'] == 'none') {
        document.getElementsByClassName('todo_list')[0].style='display: '
    } else {
        document.getElementsByClassName('todo_list')[0].style='display: none'
    } 
};