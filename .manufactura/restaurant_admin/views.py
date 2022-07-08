from multiprocessing import context
from .models import AdminAdditionalInfo
from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login
from order.models import*

class LoginAdmin(TemplateView):
    template_name = "restaurant_admin/login.html"
    def dispatch(self, request):
        context = {
            'title':'Вхід для адміністратора'
        }
        if request.method == 'POST':

            admin_name = request.POST.get("admin_name")
            password = request.POST.get("password")
            admin = authenticate(request, username = admin_name, password = password)
            if admin is not None:
                login(request, admin)
                if AdminAdditionalInfo.objects.get(admin_account=request.user).rights == 'order_management':

                    return redirect("orders") 
            else:
                context['error_text'] = 'Схоже, деякі дані введені некоректно!'

        return render(request, self.template_name, context=context)

def orders_page(request):
    context = {
        'title':'Керування замовленнями',
        'reservations':TableReservation.objects.all(),
        'takeaways':TakeAway.objects.all()
    }
    try:
        if AdminAdditionalInfo.objects.get(admin_account=request.user).rights == 'order_management':
            return render(request, 'restaurant_admin/orders.html', context=context)
    except:
        return redirect('login_admin')
