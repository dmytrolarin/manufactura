from unicodedata import name

from django.db import IntegrityError
from django.shortcuts import redirect
from menu.models import Category, Product
from transliterate import translit
class MenuMixin:
    # Функция для внесения изменений в меню
    def change_menu(self, request):
        product_pk = request.POST.get('chosen-pk')
        # product_name = request.POST.get("product-name")
        if request.POST.get("modal-button") == "dish_del":
            product_object = Product.objects.get(pk=product_pk)
            product_object.delete()
        
        elif request.POST.get("modal-button") == "dish_edit":
            product_object = Product.objects.get(pk=product_pk)
            product_object.name = request.POST.get('product-name')
            product_object.composition = request.POST.get('product-description')
            product_object.price = request.POST.get('product-price')
            if 'product-image' in request.FILES:
                product_object.photo = request.FILES['product-image']
            product_object.save()

        elif request.POST.get("modal-button") == "dish_add":
            product_object = Product(
                name = request.POST.get('product-name'),
                composition = request.POST.get('product-description'),
                price = request.POST.get('product-price'),
                cat_id = request.POST.get('chosen-prod-cat-id')

                )  
            if 'product-image' in request.FILES:
                product_object.photo = request.FILES['product-image']
            else:
                product_object.photo = 'empty'
            product_object.save()    

        elif request.POST.get("modal-button") == "cat_add":
            cat_name = request.POST.get("cat_name")
            cat_slug = translit(request.POST.get("cat_name"), 'uk',reversed=True).replace(' ','-')
            serial_number = len(Category.objects.all())
            
            cat_is_created = False
            while not cat_is_created:
                try:
                    Category.objects.create(name = cat_name, slug = cat_slug, serial_number=serial_number)
                    cat_is_created = True
                except IntegrityError:
                    cat_slug += '_'

        elif request.POST.get("modal-button") == "cat_edit" or request.POST.get("modal-button") == "cat_move_left" or request.POST.get("modal-button") == "cat_move_right":
            cat_name = request.POST.get("cat_name")
            cat_pk = request.POST.get("cat_pk")
            cat = Category.objects.get(pk = cat_pk)
            cat.name = cat_name
            try:
                if request.POST.get("modal-button") == "cat_move_left":
                    closest_cat = Category.objects.get(serial_number = cat.serial_number-1)
                    closest_cat.serial_number = cat.serial_number
                    closest_cat.save()
                    cat.serial_number = cat.serial_number-1
                elif request.POST.get("modal-button") == "cat_move_right":
                    closest_cat = Category.objects.get(serial_number = cat.serial_number+1)
                    closest_cat.serial_number = cat.serial_number
                    closest_cat.save()
                    cat.serial_number = cat.serial_number+1
                cat.save()
            except:
                None

        elif request.POST.get("modal-button") == "cat_del":
            cat_pk = request.POST.get("cat_pk")
            cat = Category.objects.get(pk = cat_pk)
            cat.delete()
            for i, cat in enumerate(Category.objects.all(), 0):
                cat.serial_number = i
                cat.save()

            