from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .models import*
from .forms import MakeTableReservationForm
# Класс-представление возвращает шаблон с формой для резервирования
class MakeTableReservation(CreateView):
    form_class = MakeTableReservationForm
    template_name = 'reservation/form.html'
    success_url = reverse_lazy('all_menu')
    def get_context_data(self, **kwargs):
        #Распаковываем ранее созданый контекст
        context = super().get_context_data(**kwargs)
        context['title'] = 'Бронювання столику'
        return context 