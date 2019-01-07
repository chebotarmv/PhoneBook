from PhoneneNumbers import views
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.clients),
    path('<name>', views.client),
    path('client/', views.client),
    path('create_client/', views.create_client),
    path('search/', views.search),
    path('clients/', views.clients_list),
    path('clients/<name>/', views.client_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)