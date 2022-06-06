from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .models import*
from .forms import DeliveryForm, MakeTableReservationForm, TakeAwayForm

class MakeTableReservation(CreateView):
    '''Класс-представление возвращает шаблон с формой для резервирования'''
    form_class = MakeTableReservationForm
    template_name = 'order/reservation_form.html'
    success_url = reverse_lazy('all_menu')
    
    def get_context_data(self, **kwargs):
        #Распаковываем ранее созданый контекст
        context = super().get_context_data(**kwargs)
        context['title'] = 'Бронювання столику'
        context['selected'] = 'reservation'
        if self.request.path_info.split('/')[-2] == 'reservation_only':
            context['show_format_choice'] = False
        return context 


class MakeTakeAway(CreateView):
    '''Класс-представление возвращает шаблон с формой для оформления заказов форматом самовівоза'''
    form_class = TakeAwayForm
    template_name = 'order/takeaway_form.html'
    success_url = reverse_lazy('all_menu')
    
    def get_context_data(self, **kwargs):
        #Распаковываем ранее созданый контекст
        context = super().get_context_data(**kwargs)
        context['title'] = 'Самовивіз'
        context['selected'] = 'takeaway'
        return context 


class MakeDelivery(CreateView):
    '''Класс-представление возвращает шаблон с формой для оформления заказов форматом доставки'''
    form_class = DeliveryForm
    template_name = 'order/delivery_form.html'
    success_url = reverse_lazy('all_menu')
    
    def get_context_data(self, **kwargs):
        #Распаковываем ранее созданый контекст
        context = super().get_context_data(**kwargs)
        context['title'] = 'Доставка'
        context['selected'] = 'delivery'
        return context 