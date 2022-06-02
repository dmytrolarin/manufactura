from django.shortcuts import render

# Create your views here.
def show_mainpage(request):
    context = {
        'title':'Ресторан Мануфактура'
    }
    return render(request,'mainpage/home.html',context=context)
