from django.urls import path
from . import views

app_name = "menu"

urlpatterns = [
    path('', views.index, name='index'),
    path('profile/', views.profile, name='profile'),
    path('profile/settings/', views.setting, name='settings'),
    path('profile/links/', views.links, name='links'),
    path('profile/info/', views.info, name='info'),
    path('contact/', views.contact, name='contact'),
    path('contact/team/', views.contact_team, name='contact_team'),
    path('products/', views.product, name='product'),
    path('products/electronic/', views.product_electronic, name='product_electronic'),
    path('products/clothing/', views.product_clothing, name='product_clothing'),
    path('products/electronic/phones/', views.product_electronic_phone, name='product_electronic_phone'),
    path('products/electronic/notebooks/', views.product_electronic_notebook, name='product_electronic_notebook'),
    path('about/', views.about, name='about'),
    path('about/project/', views.about_project, name='about_project'),
]