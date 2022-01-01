from django.contrib import admin
from django.urls import path

from catalog.views import ProductAPIView

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('api/products/', ProductAPIView.as_view())
]
