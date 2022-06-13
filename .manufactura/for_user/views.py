from django.shortcuts import render
from for_user.models import RestaurantInfo
# Показываем страницу "Про нас"
def show_about_us(request):
    context = {
        'title':'Про нас',
        'rest_info': RestaurantInfo.objects.all()[0],
        'path_pref':'../../'
    }
    return render(request, 'for_user/about_us.html',context=context)

# Показываем страницу с контактами
def show_contacts(request):
    context = {
        'title':'Про нас',
        'rest_info': RestaurantInfo.objects.all()[0],
        'path_pref':'../../'

    }
    return render(request, 'for_user/contacts.html',context=context)

# Показываем форму для отзыва
def show_review_form(request):
    context = {
        'title':'Ваш відгук',
        'rest_info': RestaurantInfo.objects.all()[0],
        'path_pref':'../../'

    }
    return render(request, 'for_user/review_form.html',context=context)