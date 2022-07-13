const modal = document.querySelector('.modal');
const modalContent = document.querySelector('.modal__content');
const closer = document.querySelector('.no');
const productList = document.querySelectorAll('.order');
const title = document.querySelector(".detail__title")

productList.forEach((list, index) => {
    const view = list.querySelector('.cancel');
    const name_not_main = list.querySelectorAll(".name");
    const name_main = Array.from(name_not_main).map(el => el.textContent);
    view.addEventListener('click', () => {
        modal.classList.add('modal--bg');
        modalContent.classList.add('modal__content--show');
        title.innerText = name_main;
    });
});

closer.addEventListener('click', () => {
    modal.classList.remove('modal--bg');
    modalContent.classList.remove('modal__content--show');
});


modal.addEventListener('click', () => {
    modal.classList.remove('modal--bg');
    modalContent.classList.remove('modal__content--show');
});