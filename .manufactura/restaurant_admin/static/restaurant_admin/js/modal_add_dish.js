const modal_add_menu = document.querySelector('.modal-menu');
const modalContent_add_menu = document.querySelector('.modal__content-menu');
const closer_add_menu = document.querySelector('.modal__close-menu');
const image_add = document.querySelector('.load-img');
const modalPrList = document.querySelectorAll('.modal_pr');
const title_modal_add_menu = document.querySelector('.title-modal-menu');
const cat_id_edit = document.querySelector('.chosen-prod-cat-id');
const title_add = document.querySelector('.detail__title input');
const composition_add = document.querySelector('.detail__description textarea');
const cost_add = document.querySelector('.detail__price input');
const button_add_menu = document.querySelector('.other-menu');
modalPrList.forEach((list, index) => {
    const add_menu = list.querySelector('.add-product-symb');
    const productCatId = list.querySelector('.prod-cat-id').getAttribute('value');
    add_menu.addEventListener('click', () => { 
        modal_add_menu.classList.add('modal-menu--bg');
        modalContent_add_menu.classList.add('modal__content-menu--show');
        title_modal_add_menu.innerText = "Створення страви";
        cat_id_edit.setAttribute('value', productCatId);
        console.log(productCatId);
        image_add.setAttribute('src', '../../media/photos/template_images/dish.png');
        title_add.setAttribute('value', "");
        composition_add.innerText = "";
        cost_add.setAttribute('value', "");
        document.getElementById('del-menu').style.display = "none";
        button_add_menu.innerText = "Створити";
        button_add_menu.setAttribute("value",'dish_add');
    });
});
closer_add_menu.addEventListener('click', () => {
    modal_add_menu.classList.remove('modal-category--bg');
    modalContent_add_menu.classList.remove('modal__content-category--show');
});
button_add_menu.addEventListener('click', () => {
    modal_add_menu.classList.remove('modal-category--bg');
    modalContent_add_menu.classList.remove('modal__content-category--show');
});
modal_add_menu.addEventListener('click', () => {
    modal_add_menu.classList.remove('modal-category--bg');
    modalContent_add_menu.classList.remove('modal__content-category--show');
});