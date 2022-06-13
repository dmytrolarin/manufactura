from django.shortcuts import render
from for_user.models import RestaurantInfo
# Показываем главную страницу
def show_mainpage(request):
    context = {
        'title':'Ресторан Мануфактура',
        'rest_info':RestaurantInfo.objects.all()[0],

    }
    return render(request,'mainpage/home.html',context=context)
