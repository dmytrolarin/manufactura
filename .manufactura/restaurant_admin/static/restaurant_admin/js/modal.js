const modal = document.querySelector('.modal');
const modalContent = document.querySelector('.modal__content');
const closer = document.querySelector('.modal__close');
const productList = document.querySelectorAll('.order');
const title = document.querySelector(".title");
const warning = document.querySelector(".warning");
const reason_cancel = document.querySelector(".reason-cancel");
const but = document.querySelector(".but");
function modal_open(name_main){
    modal.classList.add('modal--bg');
    modalContent.classList.add('modal__content--show');
    title.innerText = name_main;
}
productList.forEach((list, index) => {
    const cancel = list.querySelector('.cancel');
    const enter = list.querySelector(".enter");
    const to_completed = list.querySelector(".to-completed");
    const name_not_main = list.querySelectorAll(".name");
    const name_main = Array.from(name_not_main).map(el => el.textContent);
    cancel.addEventListener('click', () => {
        modal_open(name_main);
        warning.innerText = "Ви дійсно хочече відхилити це замовлення?";
        reason_cancel.innerHTML = "<textarea class='big-field' name='review_text'  cols='30' rows='10' placeholder='Вкажіть причину відхилення(необов`язково)'></textarea>";
        but.innerHTML = "<input type='submit' value='Відхилити' class='btn_review no'>";
    });
    enter.addEventListener('click', () => {
        modal_open(name_main);
        warning.innerText = "Ви дійсно хочете підвердити це замовлення?";
        reason_cancel.innerHTML = "";
        but.innerHTML = "<input type='submit' value='Підвердити' class='btn_review yes'>";
    });
    to_completed.addEventListener('click', () => {
        modal_open(name_main);
        warning.innerText = "Ви дійсно хочете додати замовлення у завершені?";
        reason_cancel.innerHTML = "";
        but.innerHTML = "<input type='submit' value='У завершені' class='btn_review complete'>";
    })
});

closer.addEventListener('click', () => {
    modal.classList.remove('modal--bg');
    modalContent.classList.remove('modal__content--show');
});


modal.addEventListener('click', () => {
    modal.classList.remove('modal--bg');
    modalContent.classList.remove('modal__content--show');
});