from django.http import HttpResponse
from .models import AdminAdditionalInfo
from django.shortcuts import redirect, render
from django.views.generic import TemplateView, ListView
from django.contrib.auth import authenticate, login
from order.models import*
from menu.models import*

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
        
class ShowAllMenu(ListView):
    '''Для показа всех блюд'''
    model = Product
    template_name = 'restaurant_admin/menu.html'
    context_object_name = 'products'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Меню'
        context['category_selected'] = 0
        context['path_pref'] = '../../'
        context['showing_all_menu'] = True

        session_key = self.request.session.session_key
        if not session_key:
            self.request.session.cycle_key()
        

        context['categories'] = categories
        return context



# Список с категориями, расположеными в правильном порядке
categories = [
            Category.objects.get(slug='snacks'),
            Category.objects.get(slug='soups'),
            Category.objects.get(slug='salads'),
            Category.objects.get(slug='main_dish')
        ]
class ShowCategoryOfDish(ListView):
    '''Для показа блюд конкретной категории'''
    model = Product
    template_name = 'restaurant_admin/menu.html'
    context_object_name = 'products'
    
    def get_queryset(self):
        return Product.objects.filter(cat__slug = self.kwargs['cat_slug'])
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c = Category.objects.get(slug = self.kwargs['cat_slug'])
        context['title'] = c.name
        context['category_selected'] = c.pk
        context['categories']= categories
        context['path_pref'] = '../../../'


        session_key = self.request.session.session_key
        if not session_key:
            self.request.session.cycle_key()
        return context

def redir_login(request):
    return redirect('login_admin')


def set_order_status(request):
    data = request.POST
    order_pk = data.get('order_pk')
    cancel_reason = data.get('cancel_reason')
    order_format = data.get('order_format')
    new_order_status = data.get('new_status')
    if order_format == 'reservation':
        order = TableReservation.objects.get(pk=order_pk)
    elif order_format == 'takeaway':
        order = TakeAway.objects.get(pk=order_pk)
    if new_order_status == 'canceled':
        if not cancel_reason:
            cancel_reason = 'не вказано'
        order.reason_for_cancel = cancel_reason
    order.status = new_order_status
    order.save()

    return HttpResponse(None)