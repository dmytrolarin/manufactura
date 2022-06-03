from django.shortcuts import render

def show_about_us(request):
    context = {
        'title':'Про нас'
    }
    return render(request, 'for_user/about_us.html',context=context)

def show_contacts(request):
    context = {
        'title':'Про нас'
    }
    return render(request, 'for_user/contacts.html',context=context)

def show_review_form(request):
    context = {
        'title':'Ваш відгук'
    }
    return render(request, 'for_user/review_form.html',context=context)