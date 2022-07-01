const modal = document.querySelector('.modal');
const modalContent = document.querySelector('.modal__content');
const close = document.querySelector('.modal__close');
const modalImg = document.querySelector('.modal__img');
const productList = document.querySelectorAll('.product');
const title = document.querySelector('.detail__title');
const composition = document.querySelector('.detail__description');
const cost = document.querySelector('.detail__price');
const button  =document.querySelector('.detail__bagBtn')


productList.forEach((list, index) => {
  const view = list.querySelector('.btn');
  const productImg = list.querySelector('.product__img').getAttribute('src');
  const name_not_main = list.querySelectorAll(".name");
  const name_main = Array.from(name_not_main).map(el => el.textContent);
  const composition_not_main = list.querySelectorAll(".composition");
  const composition_main = Array.from(composition_not_main).map(el => el.textContent);
  const price_not_main = list.querySelectorAll(".price");
  const price_main = Array.from(price_not_main).map(el => el.textContent);


  view.addEventListener('click', () => {
    modal.classList.add('modal--bg');
    modalContent.classList.add('modal__content--show');
    modalImg.setAttribute('src', productImg);
    title.innerText = name_main;
    composition.innerText = composition_main;
    cost.innerText = price_main;
  });
});

close.addEventListener('click', () => {
  modal.classList.remove('modal--bg');
  modalContent.classList.remove('modal__content--show');
});

button.addEventListener('click', () => {
  modal.classList.remove('modal--bg');
  modalContent.classList.remove('modal__content--show');
});

modal.addEventListener('click', () => {
  modal.classList.remove('modal--bg');
  modalContent.classList.remove('modal__content--show');
});

    
    

