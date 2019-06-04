from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Product


def home_page(request):
    products = Product.objects.all
    return render(request, 'product/home_page.html', {'products': products})


@login_required
def create_product(request):
    if request.method == 'POST':
        product = Product()
        product.title = request.POST['title']
        product.body = request.POST['body']
        if request.POST['url'].startswith('http://') or request.POST['url'].startswith('https://'):
            product.url = request.POST['url']
        else:
            product.url = 'https://' + request.POST['url']
        product.icon = request.FILES['icon']
        product.image = request.FILES['image']
        product.pub_date = timezone.datetime.now()
        product.hunter = request.user
        product.save()
        return redirect('/products/' + str(product.id))

    else:
        return render(request, 'product/create_product.html')


def product_details(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'product/product_details.html', {'product': product})


@login_required
def upvote(request, product_id):
    if request.method == 'POST':
        product = get_object_or_404(Product, pk=product_id)
        product.votes_total += 1
        product.save()
        return redirect('/products/' + str(product.id))