from django.shortcuts import render
from .models import Product
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, get_object_or_404
from django.db.models import Count

@login_required
def like_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if request.user in product.likes.all():
        product.likes.remove(request.user)
    else:
        product.likes.add(request.user)
    return redirect('product_list')

def product_list(request):
    query = request.GET.get('q')
    if query:
        products = Product.objects.filter(name__icontains=query)
    else:
        
        products = Product.objects.annotate(num_likes=Count('likes')).order_by('-num_likes')
    return render(request, 'product/product_list.html', {'product': products})
