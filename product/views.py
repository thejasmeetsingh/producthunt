from django.shortcuts import render


def home_page(request):
    return render(request, 'product/home_page.html')
