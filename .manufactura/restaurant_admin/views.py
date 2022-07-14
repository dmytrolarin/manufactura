from django.http import HttpResponse
from .models import AdminAdditionalInfo
from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login
from order.models import*

class LoginAdmin(TemplateView):
    template_name = "restaurant_admin/login.html"
    def dispatch(self, request):
        context = {
            'title':'Вхід для адміністратора',
            'path_pref':'../../'
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

def orders_page(request,status_slug=None):
    context = {
        'title':'Керування замовленнями',
        'reservations':TableReservation.objects.all(),
        'takeaways':TakeAway.objects.all(),
        'path_pref':'../../'
    }
    if status_slug != None:
        context['reservations'] = TableReservation.objects.filter(status = status_slug)
        context['takeaways'] = TakeAway.objects.filter(status = status_slug)
        context['selected_status'] = status_slug
        context['path_pref'] = '../../../'
    else:
        context['selected_status'] = 'all'

    context['new_reservations'] = len(TableReservation.objects.filter(status='new'))
    context['new_takeaways'] = len(TakeAway.objects.filter(status='new'))
    

    try:
        if AdminAdditionalInfo.objects.get(admin_account=request.user).rights == 'order_management':
            return render(request, 'restaurant_admin/orders.html', context=context)
    except:
        
        return redirect('login_admin')
        


def redir_login(request):
    return redirect('login_admin')


# def set_order_active_status(request):
#     data = request.POST
#     order_pk = data.get('order_pk')
#     order_format = data.get('order_format')
#     if order_format == 'reservation':
#         order = TableReservation.objects.get(pk=order_pk)
#     elif order_format == 'takeaway':
#         order = TakeAway.objects.get(pk=order_pk)
#     order.status = 'active'
#     order.save()

#     return HttpResponse(None)