;(function($, win) {
    $.fn.inViewport = function(cb) {
        return this.each(function(i,el) {
            function visPx(){
                var elH = $(el).outerHeight(),
                    H = $(win).height(),
                    r = el.getBoundingClientRect(), t=r.top, b=r.bottom;
                return cb.call(el, Math.max(0, t>0? Math.min(elH, H-t) : Math.min(b, H)));
            }
            visPx();
            $(win).on("resize scroll", visPx);
        });
    };
}(jQuery, window));

$(document).ready(function() {
    $("a").on('click', function(event) {
        if (this.hash !== "") {
            event.preventDefault();
            var hash = this.hash;
            $('html, body').animate({
                scrollTop: $(hash).offset().top
            }, 600, function() {
                window.location.hash = hash;
            });
        }
    });

    $(".header-line").inViewport(function(px) {
        $(this).toggleClass("expand-from-center", !!px);
    });
});