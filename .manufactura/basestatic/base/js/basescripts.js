function burgerMenu(selector_menu, selector_slider) {
    
    let menu = $(selector_menu);
    let button = menu.find('.burger-menu__button');
    let links = menu.find('.link');
    let overlay = menu.find('.burger-menu__overlay');

    let slider = $(selector_slider);
    let slider_ul = slider.find('ul')

    button.on('click', (e) =>{
        e.preventDefault();
        toggleMenu();
       
    });

    links.on('click', () => toggleMenu());
    overlay.on('click', () => toggleMenu());
    function toggleMenu() {
        menu.toggleClass('burger-menu_active');

        if (menu.hasClass('burger-menu_active')) {
            $('body').css('overflow', 'hidden');
        } else {
            $('body').css('overflow', 'visible');
            
        }
        
    }
}

burgerMenu('header','#slider');