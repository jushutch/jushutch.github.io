window.addEventListener("scroll", parallax("slow"));
window.addEventListener("scroll", parallax("medium"));
window.addEventListener("scroll", parallax("fast"));

const Speeds = {
  slow: 0.1,
  medium: 0.3,
  fast: 0.7,
};

function parallax(selector) {
  var time = Date.now();
  return function () {
    if (time + 10 - Date.now() < 0) {
      var scrolled = window.pageYOffset;
      console.log(".parallax-" + selector);
      var speed = Speeds[selector];
      var coords = "-" + scrolled * speed + "px";
      var elements = document.querySelectorAll(".parallax-" + selector);
      // You can adjust the 0.4 to change the speed
      elements.forEach(function (element, _) {
        element.style.transform = "translateY(" + coords + ")";
      });

      time = Date.now();
    }
  };
}
