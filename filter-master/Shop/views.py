from django.shortcuts import render
from django.views.generic import DetailView

from Shop.models import Product, Category, ApplicationArea


# Create your views here.

def show_index_page(request):
    category_filter = request.GET.get('category_filter')
    application_area_filter = request.GET.get('application_area_filter')
    price_filter = request.GET.get('price_filter')
    availability_filter = request.GET.get('availability_filter')
    rating_filter = request.GET.get('rating_filter')
    products = Product.objects.all()

    if category_filter == 'all' or category_filter is None:
        products = Product.objects.all()
    else:
        products = Product.objects.filter(category__title=category_filter)

    if application_area_filter == 'all' or application_area_filter is None:
        products = Product.objects.all()
    else:
        products = Product.objects.filter(application_area__title=application_area_filter)

    if price_filter == 'all' or price_filter is None:
        products = Product.objects.all()
    elif price_filter == 'low to high':
        products = products.order_by('price')
    elif price_filter == 'high to low':
        products = products.order_by('-price')

    if availability_filter == 'all' or availability_filter is None:
        products = Product.objects.all()
    elif availability_filter == 'Yes':
        products = products.filter(count__gt=0)
    elif availability_filter == 'No':
        products = products.filter(count=0)

    if rating_filter == 'all' or rating_filter is None:
        products = Product.objects.all()
    elif '1' <= rating_filter <= '5':
        products = products.filter(average_rating__gte=rating_filter)

    context = {'products': products, 'categories': Category.objects.all(),
               'application_areas': ApplicationArea.objects.all()}
    return render(request, 'Shop/index.html', context=context)


class DetailViewPage(DetailView):
    model = Product
    template_name = 'Shop/detail.html'
    pk_url_kwarg = 'product_id'
    context_object_name = 'product'
