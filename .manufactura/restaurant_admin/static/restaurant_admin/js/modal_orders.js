const modal = document.querySelector('.modal');
const modalContent = document.querySelector('.modal__content');
const closer = document.querySelector('.modal__close');
const productList = document.querySelectorAll('.order');
const title = document.querySelector(".title");
const warning = document.querySelector(".warning");
const reason_cancel = document.querySelector(".reason-cancel");
const but = document.querySelector(".but");
function modal_open(name_main,order_pk,order_format){
    modal.classList.add('modal--bg');
    modalContent.classList.add('modal__content--show');
    title.innerText = name_main;
    document.getElementById('order_pk').value = order_pk;
    document.getElementById('order_format').value = order_format;
}
productList.forEach((list, index) => {
    const cancel = list.querySelector('.cancel');
    const enter = list.querySelector(".enter");
    const to_completed = list.querySelector(".to-completed");
    const name_not_main = list.querySelectorAll(".name");
    const order_pk_sel = list.querySelectorAll(".pk");
    const order_format_sel= list.querySelectorAll(".format");
    const name_main = Array.from(name_not_main).map(el => el.textContent);
    const order_pk = Array.from(order_pk_sel).map(el => el.textContent);
    const order_format = Array.from(order_format_sel).map(el => el.textContent);
    cancel.addEventListener('click', () => {
        modal_open(name_main,order_pk,order_format);
        warning.innerText = "Ви дійсно хочече відхилити це замовлення?";
        document.getElementById('new_status').value = 'canceled';
        reason_cancel.innerHTML = "<textarea class='big-field' name='review_text' id='cancel-reason'  cols='30' rows='10' placeholder='Вкажіть причину відхилення'></textarea>";
        but.innerHTML = "<input type='submit' value='Відхилити' class='btn_review to-cancel btn_modal'>";
    });
    enter.addEventListener('click', () => {
        modal_open(name_main,order_pk,order_format);
        warning.innerText = "Ви дійсно хочете підвердити це замовлення?";
        document.getElementById('new_status').value = 'active';
        reason_cancel.innerHTML = "<textarea hidden id='cancel-reason'></textarea>";
        but.innerHTML = "<input type='submit' value='Підвердити' class='btn_review to-active btn_modal'>";
    });
    to_completed.addEventListener('click', () => {
        modal_open(name_main,order_pk,order_format);
        warning.innerText = "Ви дійсно хочете додати замовлення у завершені?";
        document.getElementById('new_status').value = 'completed';
        reason_cancel.innerHTML = "<textarea hidden id='cancel-reason'></textarea>";
        but.innerHTML = "<input type='submit' value='У завершені' class='btn_review to-complete btn_modal'>";
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