//;(function($, win) {
//    $.fn.inViewport = function(cb) {
//        return this.each(function(i,el) {
//            function visPx(){
//                var elH = $(el).outerHeight(),
//                    H = $(win).height(),
//                    r = el.getBoundingClientRect(), t=r.top, b=r.bottom;
//                return cb.call(el, Math.max(0, t>0? Math.min(elH, H-t) : Math.min(b, H)));
//            }
//            visPx();
//            $(win).on("resize scroll", visPx);
//        });
//    };
//}(jQuery, window));

$(document).ready(function() {
    var $animation_elements = $('.header-line');
    var $window = $(window);

    function check_if_in_view() {
        var window_height = $window.height();
        var window_top_position = $window.scrollTop();
        var window_bottom_position = (window_top_position + window_height);

        $.each($animation_elements, function() {
            var $element = $(this);
            var element_height = $element.outerHeight();
            var element_top_position = $element.offset().top;
            var element_bottom_position = (element_top_position + element_height);

            //check to see if this current container is within viewport
            if ((element_bottom_position >= window_top_position) &&
                (element_top_position <= window_bottom_position)) {
                $element.addClass('expand-from-center');
            } else {
                $element.removeClass('expand-from-center');
            }
        });
    }

    $window.on('scroll resize', check_if_in_view);
    $window.trigger('scroll');

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

    //$(".header-line").inViewport(function(px) {
    //    $(this).toggleClass("expand-from-center", !!px);
    //});
});