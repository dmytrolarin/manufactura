from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .models import*
from .forms import MakeTableReservationForm
# Класс-представление возвращает шаблон с формой для резервирования
class MakeTableReservation(CreateView):
    form_class = MakeTableReservationForm
    template_name = 'order/reservation_form.html'
    success_url = reverse_lazy('all_menu')
    def get_context_data(self, **kwargs):
        #Распаковываем ранее созданый контекст
        context = super().get_context_data(**kwargs)
        context['title'] = 'Бронювання столику'
        context['selected'] = 'reservation'
        return context 

def show_form_takeaway(request):
    context = {
        'title':'Самовивіз',
        'selected':'takeaway'
    }
    return render(request, 'order/takeaway_form.html',context=context)

def show_form_delivery(request):
    context = {
        'title':'Доставка',
        'selected':'delivery'
    }
    return render(request, 'order/delivery_form.html',context=context)