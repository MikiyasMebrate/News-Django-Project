from django.urls import path, include
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
   path('', views.homepage, name='index'),
   path('about/', views.about, name='about'),
   path('contact/', views.contact, name='contact'),
   path('news/<str:pk>/', views.detail_news, name='detail_news'),
    path('api-auth/', include('rest_framework.urls')),
    path('latest_post/', views.homepage_json, name='homepage_json')
] 