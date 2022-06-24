from django.contrib import messages
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from menu.models import Product
from .models import*
from .forms import*
from django.core.mail import send_mail
from manufactura import settings
from for_user.models import RestaurantInfo

# Функция для обработки формы для брони столика
def make_table_reservation(request):
    context = {
        'title':'Бронювання столику',
        'selected':'reservation',
        'path_pref':'../../',
        'rest_info': RestaurantInfo.objects.all()[0]

    }
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
            if order_comment == None:
                order_comment = '-'
            message =   f"""Клієнт: {client_name};
            \rНомер телефону: {client_phone_number}; 
            \rЧас бронвання: {time_reservation}; 
            \rДата бронювання: {date_reservation};
            \rКількість персон: {amount_persons};
            \rКоментар до замовлення: {order_comment}."""
            mail = send_mail(subject,message,settings.EMAIL_HOST_USER,[settings.EMAIL_HOST_USER], fail_silently=False)
            if mail:
                form.save()
                messages.success(request, "Ваше замовлення оформлено! Ми скоро зв'яжемося з вами!")
                context['message_type'] = 'success'
                form = MakeTableReservationForm()
            else:
                messages.error(request, 'Сталася помилка при оформленні замовлення. Спробуйте ще раз!')
                context['message_type'] = 'error'
        else:
            messages.error(request, 'Схоже, деякі дані введені некоректно. Спробуйте ще раз!')
            context['message_type'] = 'error'
    else:
        form = MakeTableReservationForm()
    if request.path_info.split('/')[-2] == 'reservation_only':
        context['show_format_choice'] = False

    context['form'] =  form
    # list_products = []
    # for cookie_key in list(request.COOKIES):
    #     if cookie_key != 'sessionid' and cookie_key != 'csrftoken':
    #         product_info = [Product.objects.get(slug=cookie_key),
    #         request.COOKIES[cookie_key].split()[0],
    #         request.COOKIES[cookie_key].split()[-1]
    #         ]

    #         list_products.append(product_info)


    # context['list_products'] = list_products
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

# def add_to_cart(request):
#     rend = render(request, 'order/reservation_form.html')
#     if request.POST['product_slug'] not in request.COOKIES:
#         rend.set_cookie(request.POST['product_slug'],request.POST['product_price']+' '+request.POST['product_amount'])
#     else:
#         new_amount = int(request.COOKIES[request.POST['product_slug']].split()[-1]) + int(request.POST['product_amount'])
#         rend.set_cookie(request.POST['product_slug'],request.POST['product_price']+' '+str(new_amount))
#     return rend
    