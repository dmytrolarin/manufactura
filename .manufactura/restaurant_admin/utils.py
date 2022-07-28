from menu.models import Product
class MenuMixin:
    # Функция для внесения изменений в меню
    def change_menu(self, request):
        product_pk = request.POST.get('chosen-pk')
        # product_name = request.POST.get("product-name")
        if request.POST.get("modal-button") == "del":
            product_object = Product.objects.get(pk=product_pk)
            product_object.delete()
        
        elif request.POST.get("modal-button") == "edit":
            product_object = Product.objects.get(pk=product_pk)
            product_object.name = request.POST.get('product-name')
            product_object.composition = request.POST.get('product-description')
            product_object.price = request.POST.get('product-price')
            if 'product-image' in request.FILES:
                product_object.photo = request.FILES['product-image']
            product_object.save()

        elif request.POST.get("modal-button") == "add":
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