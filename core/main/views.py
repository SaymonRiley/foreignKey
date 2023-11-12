from typing import Any
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views import generic
from .models import *


class HomeListView(generic.ListView):
    template_name = 'index.html'

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        categories = Category.objects.all()

        context = {
            "categories": categories,
        }

        return render(request, self.template_name, context=context)


class CategoryListView(generic.ListView):
    template_name = 'categories.html'

    def get(self, request, slug, *args: Any, **kwargs: Any) -> HttpResponse:
        categories = Category.objects.all()
        subcategories = Category.objects.filter(slug=slug)

        context = {
            "categories": categories,
            "subcategories": subcategories,
        }

        return render(request, self.template_name, context=context)


class ProductListView(generic.ListView):
    template_name = 'products.html'

    def get(self, request, slug, id, *args: Any, **kwargs: Any) -> HttpResponse:
        categories = Category.objects.all()
        subcategories = Category.objects.filter(slug=slug)
        products = SubCategory.objects.filter(pk=id)

        context = {
            "categories": categories,
            "subcategories": subcategories,
            "products": products,
        }

        return render(request, self.template_name, context=context)


class ProductDetailView(generic.DetailView):
    template_name = 'detail.html'

    def get(self, request, prod_id, *args: Any, **kwargs: Any) -> HttpResponse:
        single_prod = Product.objects.get(pk=prod_id)

        context = {

            "single_prod": single_prod,
        }

        return render(request, self.template_name, context=context)
