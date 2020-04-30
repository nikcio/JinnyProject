document.addEventListener("DOMContentLoaded", (function() {
    $("#scroll-down").click(function() {
        $('html, body').animate({
            scrollTop: $("#scroll-section").offset().top
        }, 500);
    });
}));