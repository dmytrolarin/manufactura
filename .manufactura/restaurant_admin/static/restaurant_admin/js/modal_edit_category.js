const modal_edit_category = document.querySelector('.modal-category');
const modalContent_edit_category = document.querySelector('.modal__content-category');
const closer_edit_category = document.querySelector('.modal__close-category');
const editList = document.querySelectorAll('.edit_cat');
const title_modal_edit_category = document.querySelector('.title-modal-category');
const button_edit_category = document.querySelector('.other-category');
const name_edit = document.querySelector('.cat_name input');
editList.forEach((list, index) => {
    const edit_category = list.querySelector('.btn-edit-cat');
    const name_nt_main = list.querySelectorAll(".cat-sp");
    const name_min = Array.from(name_nt_main).map(el => el.textContent);
    edit_category.addEventListener('click', () => {
        modal_edit_category.classList.add('modal-category--bg');
        modalContent_edit_category.classList.add('modal__content-category--show');
        title_modal_edit_category.innerText = "Редагування категорії";
        name_edit.setAttribute('value', name_min);
        document.getElementById('del-category').style.display = "flex";
        button_edit_category.innerText = "Зберегти";
    });
});
closer_edit_category.addEventListener('click', () => {
    modal_edit_category.classList.remove('modal-category--bg');
    modalContent_edit_category.classList.remove('modal__content-category--show');
});


button_edit_category.addEventListener('click', () => {
    modal_edit_category.classList.remove('modal-category--bg');
    modalContent_edit_category.classList.remove('modal__content-category--show');
});

modal_edit_category.addEventListener('click', () => {
    modal_edit_category.classList.remove('modal-category--bg');
    modalContent_edit_category.classList.remove('modal__content-category--show');
});