from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CompanySerializer, ProductSerializer, ServiceSerializer, ReviewSerializer, DocumentSerializer 
from project_tc_gen.models import Company, Document, Review, Service, Product
@api_view(['GET'])
def getRoutes(request):
    routes = [
            {'GET': 'api/project_tc_gen'},
            {'POST': 'api/users/token'},
            ]
    return Response(routes)

@api_view(['GET'])
def getCompany(request):
    companys = Company.objects.all()
    serialize = CompanySerializer(companys, many=True)
    return Response(serialize.data)

@api_view(['GET'])
def getDocument(request):
    documents = Document.objects.all()
    serialize = DocumentSerializer(documents, many=True)
    return Response(serialize.data)

@api_view(['GET'])
def getReview(request):
    reviews = Review.objects.all()
    serialize = ReviewSerializer(reviews, many=True)
    return Response(serialize.data)

@api_view(['GET'])
def getService(request):
    services = Service.objects.all()
    serialize = ServiceSerializer(services, many=True)
    return Response(serialize.data)

@api_view(['GET'])
def getProduct(request):
    products = Product.objects.all()
    serialize = ProductSerializer(products, many=True)
    return Response(serialize.data)
