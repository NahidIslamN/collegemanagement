var carousel = new bootstrap.Carousel(document.getElementById('carouselExampleCaptions'), {
    interval: false
});

document.getElementById('carouselExampleCaptions').addEventListener('slide.bs.carousel', function (evt) {
    var activeIndex = evt.to;
    var slidesLength = evt.target.querySelectorAll('.carousel-item').length;

    if (activeIndex === slidesLength - 1) {
        // If the last slide is reached, loop back to the first slide
        carousel.to(0);
    }
});


$(document).ready(function() {
    $('.modal-trigger').click(function() {
        var targetModal = $(this).data('bs-target');
        $(targetModal).modal('show');
    });
});