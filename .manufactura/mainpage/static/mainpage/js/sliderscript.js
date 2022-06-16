var responsiveSlider = function (){
    var slider = document.getElementById('slider');
    var sliderWidth = slider.offsetWidth;
    var slideList = document.getElementById('slider__content');
    var count = 1;
    var items = slideList.querySelectorAll('li').length;
    var prev = document.getElementById('slider__prev');
    var next = document.getElementById('slider__next');

    window.addEventListener('resize', function() {
        sliderWidth = slider.offsetWidth
    })

    var prevSlide = function () {
        if (count > 1){
            count = count - 2
            slideList.style.left = '-' + count * sliderWidth + 'px';
            count++;

        }
        else if(count=1){
            count = items - 1;
            slideList.style.left = '-' + count * sliderWidth + 'px';
            count ++;

        }
    };

    var nextSlide = function () {
        if (count < items){
            slideList.style.left = '-' + count * sliderWidth + 'px';
            count++;

        }
        else if(count=items){
            slideList.style.left = '0px';
            count = 1;

        }
    };

    next.addEventListener('click', function(){
        nextSlide();
    });
    prev.addEventListener('click', function(){
        prevSlide();
    });

    setInterval(function(){
        nextSlide()
    }, 10000);
 

}

window.onload = function(){
    responsiveSlider();
}