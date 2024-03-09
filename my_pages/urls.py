from django.urls import path

import my_pages.views as views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('test/', views.test, name='test'),
    path('help/', views.help, name='help'),
    path('django/', views.django, name='django')
]