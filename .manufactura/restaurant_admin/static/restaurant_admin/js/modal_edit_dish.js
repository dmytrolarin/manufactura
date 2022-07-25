const modal_edit_menu = document.querySelector('.modal-menu');
const modalContent_edit_menu = document.querySelector('.modal__content-menu');
const closer_edit_menu = document.querySelector('.modal__close-menu');
const image_edit = document.querySelector('.load-img');
const productList = document.querySelectorAll('.product');
const title_modal_edit_menu = document.querySelector('.title-modal-menu');
const title_edit = document.querySelector('.detail__title input');
const composition_edit = document.querySelector('.detail__description textarea');
const cost_edit = document.querySelector('.detail__price input');
const button_edit_menu = document.querySelector('.other-menu');
productList.forEach((list, index) => {
    const edit_menu = list.querySelector('.btn-edit-dish');
    const productImg = list.querySelector('.product__img').getAttribute('src');
    const name_not_main = list.querySelectorAll(".name");
    const name_main = Array.from(name_not_main).map(el => el.textContent);
    const composition_not_main = list.querySelectorAll(".composition");
    const composition_main = Array.from(composition_not_main).map(el => el.textContent);
    const price_not_main = list.querySelectorAll(".num");
    const price_main = Array.from(price_not_main).map(el => el.textContent);
    edit_menu.addEventListener('click', () => {
        modal_edit_menu.classList.add('modal-menu--bg');
        modalContent_edit_menu.classList.add('modal__content-menu--show');
        title_modal_edit_menu.innerText = "Редагування страви";
        image_edit.setAttribute('src', productImg);
        title_edit.setAttribute('value', name_main);
        composition_edit.innerText = composition_main;
        cost_edit.setAttribute('value', price_main);
        document.getElementById('del-menu').style.display = "flex";
        button_edit_menu.innerText = "Зберегти";
    });
});
closer_edit_menu.addEventListener('click', () => {
    modal_edit_menu.classList.remove('modal-menu--bg');
    modalContent_edit_menu.classList.remove('modal__content-menu--show');
});


button_edit_menu.addEventListener('click', () => {
    modal_edit_menu.classList.remove('modal-menu--bg');
    modalContent_edit_menu.classList.remove('modal__content-menu--show');
});

modal_edit_menu.addEventListener('click', () => {
    modal_edit_menu.classList.remove('modal-menu--bg');
    modalContent_edit_menu.classList.remove('modal__content-menu--show');
});
