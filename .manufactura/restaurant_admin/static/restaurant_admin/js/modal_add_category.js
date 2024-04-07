const modal_add_category = document.querySelector('.modal-category');
const modalContent_add_category = document.querySelector('.modal__content-category');
const closer_add_category = document.querySelector('.modal__close-category');
const addList = document.querySelectorAll('.add_cat');
const title_modal_add_category = document.querySelector('.title-modal-category');
const button_add_category = document.querySelector('.other-category');
const name_add = document.querySelector('.cat_name input');
const location_add = document.querySelector('.location');
addList.forEach((list, index) => {
    const add_category = list.querySelector('.h-scroller__item');
    add_category.addEventListener('click', () => {
        modal_add_category.classList.add('modal-category--bg');
        modalContent_add_category.classList.add('modal__content-category--show');
        title_modal_add_category.innerText = "Створення категорії";
        name_add.setAttribute('value', "");
        document.getElementById('del-category').style.display = "none";
        location_add.innerHTML = "";
        button_add_category.innerText = "Створити";
        button_add_category.setAttribute("value",'cat_add');
    });
});
closer_add_category.addEventListener('click', () => {
    modal_add_category.classList.remove('modal-category--bg');
    modalContent_add_category.classList.remove('modal__content-category--show');
});


button_add_category.addEventListener('click', () => {
    modal_add_category.classList.remove('modal-category--bg');
    modalContent_add_category.classList.remove('modal__content-category--show');
});

modal_add_category.addEventListener('click', () => {
    modal_add_category.classList.remove('modal-category--bg');
    modalContent_add_category.classList.remove('modal__content-category--show');
});