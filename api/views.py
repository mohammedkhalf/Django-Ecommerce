from django.shortcuts import get_object_or_404
from django.db.models import Max
from api.serializers import ProductSerializer, OrderSerializer, ProductInfoSerializer
from api.models import Product, Order
from rest_framework.response import Response
from rest_framework.decorators import api_view

from rest_framework import generics 


class ProductListAPIView (generics.ListAPIView): 
    queryset = Product.objects.filter(stock__gt=0)
    serializer_class = ProductSerializer


class ProductDetailAPIView (generics.RetrieveAPIView): 
        queryset = Product.objects.all()
        serializer_class = ProductSerializer
        lookup_url_kwarg = 'product_id'
        
        
class OrderListAPIView(generics.ListAPIView):
    queryset = Order.objects.prefetch_related(
        'items', 'items__product'
    ).all()
    serializer_class = OrderSerializer



# @api_view(['GET'])
# def product_list(request):   # get all products
#     products = Product.objects.all()
#     serializer = ProductSerializer(products, many=True)
#     return Response(serializer.data)
    
# @api_view(['GET'])
# def product_details(request, pk):   # get single product
#     product = get_object_or_404(Product, pk=pk)
#     serializer = ProductSerializer(product)
#     return Response(serializer.data)


# @api_view(['GET'])
# def order_list(request):    # get all orders
#     orders = Order.objects.prefetch_related(
#         'items', 'items__product'
#     ).all()
#     serializer = OrderSerializer(orders, many=True)
#     return Response(serializer.data)
    
    
@api_view(['GET'])
def product_info(request):
    products = Product.objects.all()
    serializer = ProductInfoSerializer({
        'products': products,
        'count':len(products),
        'max_price':products.aggregate(max_price = Max('price'))['max_price']
    })
    return Response(serializer.data)


    