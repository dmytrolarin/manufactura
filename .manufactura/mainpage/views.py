from django.shortcuts import render

# Показываем главную страницу
def show_mainpage(request):
    context = {
        'title':'Ресторан Мануфактура'
    }
    return render(request,'mainpage/home.html',context=context)
