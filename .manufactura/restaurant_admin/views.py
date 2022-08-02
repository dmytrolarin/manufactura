from django.http import HttpResponse
from .models import AdminAdditionalInfo
from django.shortcuts import redirect, render
from django.views.generic import TemplateView, ListView
from django.contrib.auth import authenticate, login, logout
from order.models import*
from menu.models import*
from .utils import MenuMixin
from transliterate import translit


def check_rights(request, rights, template_name, context):
    try:
        admin_rights = AdminAdditionalInfo.objects.get(admin_account=request.user).rights
        if admin_rights == rights or admin_rights == 'all_rights':
            return render(request, template_name, context=context)
        else:
            return redirect('login_admin')
    except:
        return redirect('login_admin')


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
                admin_rigths = AdminAdditionalInfo.objects.get(admin_account=request.user).rights
                if admin_rigths == 'order_management':
                    return redirect("orders") 
                elif admin_rigths == 'menu_editing':
                    return redirect('all_menu_for_editing')
                elif admin_rigths == 'rest_info_editing':
                    return redirect('rest_info_editing')
                elif admin_rigths == 'all_rights':
                    return redirect('select_task')
            else:
                context['error_text'] = 'Схоже, деякі дані введені некоректно!'

        return render(request, self.template_name, context=context)


def select_task_page(request):
    context = {
        'title':'Вибір задачі',
        'path_pref':'../../'
    }
    return render(request, 'restaurant_admin/select_task.html', context=context)


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

    return check_rights(request, 'order_management', 'restaurant_admin/orders.html', context)


def rest_info_editing_page(request):
    context = {
        'title':'Редагування інформації про ресторан',
        'path_pref':'../../'
    }
    return check_rights(request, 'rest_info_editing', 'restaurant_admin/rest_info_editing.html', context)
        
class ShowAllMenu(TemplateView, MenuMixin):
    '''Для показа всех блюд'''
         
    template_name = 'restaurant_admin/menu.html'
    def dispatch(self, request):
        context = {
            'products':Product.objects.all(),
            'title':'Редагування меню',
            'category_selected':0,
            'path_pref':'../../',
            'showing_all_menu':True,
            'categories':Category.objects.order_by('serial_number')
        }
    
        if request.method == 'POST':
            self.change_menu(request)         
        return check_rights(request, 'menu_editing', 'restaurant_admin/menu.html', context)


class ShowCategoryOfDish(TemplateView, MenuMixin):
    '''Для показа блюд конкретной категории'''
    template_name = 'restaurant_admin/menu.html'
    def dispatch(self, request, cat_slug):
        cat = Category.objects.get(slug = cat_slug)
        context = {
            'products':Product.objects.filter(cat__slug = cat_slug),
            'category_selected':cat.pk,
            'title':f'Редагування меню ({cat.name})',
            'path_pref':'../../../',
            'categories':Category.objects.order_by('serial_number')
        }
    
        if request.method == 'POST':
            self.change_menu(request)  
            if request.POST.get("modal-button") == "cat_del":
                return redirect('all_menu_for_editing')      
        return check_rights(request, 'menu_editing', 'restaurant_admin/menu.html', context)


# Функция для выхода админа
def logout_admin(request):
    logout(request)
    return redirect('login_admin')

# Функция для изменения статуса заказа
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