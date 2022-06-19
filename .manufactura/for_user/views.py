from django.shortcuts import render
from for_user.models import RestaurantInfo
from django.views.generic import TemplateView
from django.core.mail import send_mail
from manufactura import settings
from django.contrib import messages
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

class SendReview(TemplateView):
    template_name = 'for_user/review_form.html'
    def dispatch(self, request):
        context = {
            'path_pref':'../../',
            'title':'Ваш відгук',
            'rest_info': RestaurantInfo.objects.all()[0],
        }

        if request.method == "POST":
            username = request.POST.get("name_user") 
            email_user = request.POST.get("email_user") 
            review_text = request.POST.get("review_text") 
            subject = "Відгук"
            message = f"""Ім'я: {username};
            \rEMAIL: {email_user}; 
            \rВідгук: {review_text}; """
            mail = send_mail(subject,message,settings.EMAIL_HOST_USER,[settings.EMAIL_HOST_USER], fail_silently=False)
            if mail:
                messages.success(request, "Дякуюємо за відгук!")
                context['message_type'] = 'success'
                print(10000)
            else:
                messages.error(request, 'Сталася помилка при надсиланні відгуку. Спробуйте ще раз!')
                context['message_type'] = 'error'

        return render(request,self.template_name, context=context)
# Показываем форму для отзыва
# def show_review_form(request):
#     form = ReviewForm
#     context = {
#         'form':form,
#         'title':'Ваш відгук',
#         'rest_info': RestaurantInfo.objects.all()[0],
#         'path_pref':'../../'
#     }
#     if request.method == 'POST':
#         form = ReviewForm(request.POST)
#         if form.is_valid():
#             subject = "Відгук"
#             name_user = form.cleaned_data.get('name_user')
#             email_user = form.cleaned_data.get('email_user')
#             images_user = form.cleaned_data.get('images_user')
#             review_user = form.cleaned_data.get('review_user')
#             message = f"""Ім'я: {name_user};
#             \rEMAIL адреса: {email_user}; 
#             \rЗображення: {images_user}; 
#             \rВідгук: {review_user}."""
#             mail = send_mail(subject,message,settings.EMAIL_HOST_USER,[settings.EMAIL_HOST_USER], fail_silently=False)
#             if mail:
#                 messages.success(request, "Відгук залишено! Дякуємо!")
#                 context['message_type'] = 'success'
#             else:
#                 messages.error(request, 'Помилка при оформленні відгукую! Спробуйте ще раз!')
#                 context['message_type'] = 'error'
#     return render(request, 'for_user/review_form.html',context=context)