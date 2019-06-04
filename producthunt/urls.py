from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from product.views import home_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page, name='home'),
    path('accounts/', include('account.urls')),
    path('products/', include('product.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

