document.addEventListener('DOMContentLoaded', function(){
    rightMenu = $(".right");
    menu = $(".menu-container");
    body = $("body")
    openButton = $(".iconify.toggle");
    closeButton = $(".iconify.close");
});

function showMenu(){
   rightMenu.addClass("show");
   body.addClass("show-menu");
}


function closeMenu(){
    rightMenu.removeClass("show");
    body.removeClass("show-menu");
}

window.addEventListener("click", function(event) {
    if (event.target == rightMenu[0]) {
        rightMenu.removeClass("show");
        body.removeClass("show-menu");
      }
});