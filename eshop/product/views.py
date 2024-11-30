from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from .models import Product
from rest_framework.response import Response
from .serializers import ProductSerializer
from .filters import ProductsFilter
from rest_framework.pagination import PageNumberPagination

# Create your views here.

@api_view(['GET'])
def get_products(request):
    
    filterset = ProductsFilter(request.GET, queryset=Product.objects.all().order_by('id'))

    count = filterset.qs.count()

    #Pagination
    resPerPage = 2

    paginator = PageNumberPagination()
    paginator.page_size = resPerPage

    queryset = paginator.paginate_queryset(filterset.qs, request)
    
    serializer = ProductSerializer(queryset, many=True)

    return Response({
        'count': count,
        'resPerPage': resPerPage,
        'products': serializer.data
        })

@api_view(['GET'])
def get_product(request, pk):

    product = get_object_or_404(Product, id=pk)

    serializer = ProductSerializer(product, many=False)

    return Response({'product': serializer.data})
    

