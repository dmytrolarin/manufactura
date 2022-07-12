const modal = document.querySelector('.modal');
const modalContent = document.querySelector('.modal__content');
const closer = document.querySelector('.modal__close');
const wrapperList = document.querySelectorAll('.wrapper-main');
const title = document.querySelector('.detail__title');
const composition = document.querySelector('.detail__description');
const cost = document.querySelector('.detail__price');
const button  = document.querySelector('.detail__bagBtn');
wrapperList.forEach((list, index) => {
    const view = list.querySelector(".cancel");
    view.addEventListener('click', () => {
        modal.classList.add('modal--bg');
        modalContent.classList.add('modal__content--show');
        title.innerText = "name_main";
        composition.innerText = "composition_main";
        cost.innerText = "price_main";
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