from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from menu.models import Product
from .models import*
from .forms import*
from django.core.mail import send_mail
from manufactura import settings
from for_user.models import RestaurantInfo
from menu.models import ProductInCart

# Функция возвращает список с продуктами в корзине
def get_products_in_cart(request):
    session_key = request.session.session_key
    products_in_cart = ProductInCart.objects.filter(session_key = session_key)
    if len(products_in_cart) == 0:
        return 'empty'
    data_products_in_cart = list()
    for product in products_in_cart:
        # Первый элемент списка - объект продукта в модели, второй - количество продукта в корзине
        data_product = [Product.objects.get(name=product.name), product.quantity]
        data_products_in_cart.append(data_product)
    return data_products_in_cart

# Функция возвращает сумарную стоимость заказа в корзине
def get_total_order_price(data_products_in_cart):
    total_price = 0
    for data_product in  data_products_in_cart:
        total_price += data_product[1]*data_product[0].price

    return total_price

#  Функция возвращает заказ пользователя для отправки на почту 
def get_order(data_products_in_cart):
    order = ''
    if data_products_in_cart != 'empty': 
        for product_data in data_products_in_cart:
            order += f'\n{product_data[0].name} x{product_data[1]};'
    else:
        order = 'в закладі'
    return order


# Функция для обработки формы для брони столика
def make_table_reservation(request):
    context = {
        'title':'Бронювання столику',
        'selected':'reservation',
        'path_pref':'../../',
        'rest_info': RestaurantInfo.objects.all()[0],
        'data_products_in_cart':get_products_in_cart(request),
        
    }

    if context['data_products_in_cart'] != 'empty':
        context['total_order_price']=get_total_order_price(get_products_in_cart(request))
    else:
        context['total_order_price']=0

    if  request.method == 'POST':
        form = MakeTableReservationForm(request.POST)
        if form.is_valid():
            subject = 'Бронювання столику'
            client_name = form.cleaned_data.get('client_name')
            client_phone_number = form.cleaned_data.get('client_phone_number')
            date_reservation = form.cleaned_data.get('date_reservation')
            time_reservation = form.cleaned_data.get('time_reservation')
            amount_persons = form.cleaned_data.get('amount_persons')
            order_comment = form.cleaned_data.get('order')
            order = get_order(context['data_products_in_cart'])
            
            if order_comment == None:
                order_comment = '-'
            message =   f"""Клієнт: {client_name};
            \rНомер телефону: {client_phone_number}; 
            \rЧас бронвання: {time_reservation}; 
            \rДата бронювання: {date_reservation};
            \rКількість персон: {amount_persons};
            \rЗамовлення: {order}
            \rКоментар до замовлення: {order_comment}
            \rВартість замовлення: {context['total_order_price']};"""
            mail = send_mail(subject,message,settings.EMAIL_HOST_USER,[settings.EMAIL_HOST_USER], fail_silently=False)
            if mail:
                session_key = request.session.session_key
                ProductInCart.objects.filter(session_key=session_key).delete()
                form.save()
                messages.success(request, "Ваше замовлення оформлено! Ми скоро зв'яжемося з вами!")
                context['message_type'] = 'success'
                form = MakeTableReservationForm()
                return redirect('reservation')
            else:
                messages.error(request, 'Сталася помилка при оформленні замовлення. Спробуйте ще раз!')
                context['message_type'] = 'error'
        else:
            messages.error(request, 'Схоже, деякі дані введені некоректно. Спробуйте ще раз!')
            context['message_type'] = 'error'
    else:
        form = MakeTableReservationForm()
        context['message_type'] = 'success'
    if request.path_info.split('/')[-2] == 'reservation_only':
        context['show_format_choice'] = False

    context['form'] =  form

    

    return render(request, 'order/reservation_form.html', context=context)
    



# Функция для обработки формы для самовывоза 
def make_take_away(request):
    context = {
        'title':'Самовивіз',
        'selected':'takeaway',
        'path_pref':'../../',
        'rest_info': RestaurantInfo.objects.all()[0]
    }
    if  request.method == 'POST':
        form = MakeTakeAwayForm(request.POST)
        if form.is_valid():
            subject = 'Замовлення на самовивіз'
            client_name = form.cleaned_data.get('client_name')
            client_phone_number = form.cleaned_data.get('client_phone_number')
            time_cooking = form.cleaned_data.get('time_cooking')
            order_comment = form.cleaned_data.get('order')
            if order_comment == None:
                order_comment = '-'
            message =   f"""Клієнт: {client_name};
            \rНомер телефону: {client_phone_number}; 
            \rЧас приготування: {time_cooking}; 
            \rКоментар до замовлення: {order_comment}."""
            mail = send_mail(subject,message,settings.EMAIL_HOST_USER,[settings.EMAIL_HOST_USER], fail_silently=False)
            if mail:
                form.save()
                messages.success(request, "Ваше замовлення оформлено! Ми скоро зв'яжемося з вами!")
                context['message_type'] = 'success'
                form = MakeTakeAwayForm()
            else:
                messages.error(request, 'Сталася помилка при оформленні замовлення. Спробуйте ще раз!')
                context['message_type'] = 'error'
        else:
            messages.error(request, 'Схоже, деякі дані введені некоректно. Спробуйте ще раз!')
            context['message_type'] = 'error'
    else:
        form = MakeTakeAwayForm()

    context['form'] =  form
    return render(request, 'order/takeaway_form.html', context=context)

# context = {
#         'title':'Доставка',
#         'selected':'delivery',
#         'path_pref':'../../',
#         'rest_info': RestaurantInfo.objects.all()[0]
#     }


# Функция для обработки формы для доставки 
def make_delivery(request):
    context = {
        'title':'Самовивіз',
        'selected':'takeaway',
        'path_pref':'../../',
        'rest_info': RestaurantInfo.objects.all()[0]
    }
    if  request.method == 'POST':
        form = MakeDeliveryForm(request.POST)
        if form.is_valid():
            subject = 'Замовлення на доставку'
            client_name = form.cleaned_data.get('client_name')
            client_phone_number = form.cleaned_data.get('client_phone_number')
            adress = form.cleaned_data.get('adress')
            time_delivery = form.cleaned_data.get('time_delivery')
            order_comment = form.cleaned_data.get('order')
            
            if order_comment == None:
                order_comment = '-'
            message =   f"""Клієнт: {client_name};
            \rНомер телефону: {client_phone_number};
            \rАдреса доставки: {adress}; 
            \rЧас доставки: {time_delivery}; 
            \rКоментар до амовлення: {order_comment}."""

            mail = send_mail(subject,message,settings.EMAIL_HOST_USER,[settings.EMAIL_HOST_USER], fail_silently=False)
            if mail:
                form.save()
                messages.success(request, "Ваше замовлення оформлено! Ми скоро зв'яжемося з вами!")
                context['message_type'] = 'success'
                form = MakeDeliveryForm()
            else:
                messages.error(request, 'Сталася помилка при оформленні замовлення. Спробуйте ще раз!')
                context['message_type'] = 'error'
        else:
            messages.error(request, 'Схоже, деякі дані введені некоректно. Спробуйте ще раз!')
            context['message_type'] = 'error'
    else:
        form = MakeDeliveryForm()

    context['form'] =  form
    return render(request, 'order/delivery_form.html', context=context)

def update_cart(request):
    
    if request.method == 'POST':
        session_key = request.session.session_key
        product_name = request.POST.get('product_name')
        product_qty = request.POST.get('product_qty')

        product_name =  rf"\n{product_name}".replace(r'\n','')
        product_name = product_name.split()
        product_name = ' '.join(product_name)

        product_qty =  rf"\n{product_qty}".replace(r'\n','')
        
        prod_in_cart = ProductInCart.objects.get(session_key=session_key,name = product_name)
        prod_in_cart.quantity = product_qty
        prod_in_cart.save()
    return HttpResponse(None)


def delete_cart(request):
    if request.method == 'POST':
        session_key = request.session.session_key
        product_name = request.POST.get('product_name')

        product_name =  rf"\n{product_name}".replace(r'\n','')
        product_name = product_name.split()
        product_name = ' '.join(product_name)

        prod_in_cart = ProductInCart.objects.get(session_key=session_key,name = product_name)
        prod_in_cart.delete()
    return HttpResponse(None)
