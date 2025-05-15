from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, "menu/index.html")


def contact(request):
    return render(request, "menu/contact.html")


def contact_team(request):
    return render(request, "menu/index.html")


def product(request):
    return render(request, "menu/product.html")


def product_electronic(request):
    return render(request, "menu/electronic.html")


def product_clothing(request):
    return render(request, "menu/index.html")


def product_electronic_phone(request):
    return render(request, "menu/phone.html")


def product_electronic_notebook(request):
    return render(request, "menu/notebook.html")


def about(request):
    return render(request, "menu/index.html")


def about_project(request):
    return render(request, "menu/index.html")


def profile(request):
    return render(request, "menu/index.html")


def setting(request):
    return render(request, "menu/index.html")


def info(request):
    return render(request, "menu/index.html")


def links(request):
    return render(request, "menu/index.html")
