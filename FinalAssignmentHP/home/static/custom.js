$(document).ready(function(){
    $('.fa').hover(function(){
        $(this).css("color", "red")
    }, function(){
        $(this).css({color:'white'}); //mouseover
    });
});
