from django.shortcuts import render

from goods.models import Categories, Products


def catalog(request):


    products=Products.objects.all()

    

    context = {
        "title": "Каталог товаров",
        "categories": Categories.objects.all(),
        "products": products,
        
    }
    return render(request, "goods/catalog.html", context)


def product(request,product_slug):

    product=Products.objects.get(slug=product_slug)
    context = {
        
        "product": product,
       
    }
    return render(request, "goods/product.html", context)
