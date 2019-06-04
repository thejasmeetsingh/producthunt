from django.urls import path
from .views import (create_product, product_details, upvote)

urlpatterns = [
    path('create/', create_product, name='create'),
    path('<int:product_id>/', product_details, name='product_details'),
    path('<int:product_id>/upvote', upvote, name='upvote')
]
