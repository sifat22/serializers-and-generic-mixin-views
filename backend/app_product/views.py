from django.shortcuts import render, get_object_or_404
#for generic view
from rest_framework import generics,mixins
#for function based
from rest_framework.decorators import api_view
from rest_framework.response import Response

from. models import Products
from.serializers import ProductSerializer

# Create your views here.


#these are class Based views



# class ProductListCreateAPIView(generics.ListCreateAPIView):
#     queryset = Products.objects.all()
#     serializer_class = ProductSerializer

#     def perform_create(self, serializer):
#         # serializer.save(user=self.request.user)
#         title = serializer.validated_data.get('title')
#         content = serializer.validated_data.get('content') or None
#         if content is None:
#             content = title
#         serializer.save(content=content)
#         # send a Django signal

# class ProductDetailAPIView(generics.RetrieveAPIView):
#     queryset = Products.objects.all()
#     serializer_class= ProductSerializer
#     #lookup_field= 'pk



#we don't need to use this list view because we can do this on ProductListCreateAPIView
# class ProductListAPIView(generics.RetrieveAPIView):
#     queryset = Products.objects.all()
#     serializer_class= ProductSerializer
#     #lookup_field= 'pk


# class ProductUpdateAPIView(generics.UpdateAPIView):
#     queryset = Products.objects.all()
#     serializer_class = ProductSerializer
#     lookup_field = 'pk'

#     def perform_update(self, serializer):
#         instance = serializer.save()
#         if not instance.content:
#             instance.content = instance.title

# class ProductDestroyAPIView(generics.DestroyAPIView):
#     queryset = Products.objects.all()
#     serializer_class = ProductSerializer
#     lookup_field = 'pk'

#     def perform_destroy(self, instance):
#         # instance 
#         super().perform_destroy(instance)



#these are function base view

# @api_view(['GET', 'POST'])
# def product_alt_view(request, pk=None, *args, **kwargs):
#     method = request.method 

#     if method == "GET":
#         if pk is not None:
#             # detail view
#             obj = get_object_or_404(Products, pk=pk)
#             data = ProductSerializer(obj, many=False).data
#             return Response(data)
#         # list view
#         queryset = Products.objects.all() 
#         data = ProductSerializer(queryset, many=True).data
#         return Response(data)

#     if method == "POST":
#         # create an item
#         serializer = ProductSerializer(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             title = serializer.validated_data.get('title')
#             content = serializer.validated_data.get('content') or None
#             if content is None:
#                 content = title
#             serializer.save(content=content)
#             return Response(serializer.data)
#         return Response({"invalid": "not good data"}, status=400)




#Mixin View

class ProductMixinView(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    generics.GenericAPIView
    ):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def get(self, request, *args, **kwargs): #HTTP -> get
        pk = kwargs.get("pk")
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
    def perform_create(self, serializer):
        # serializer.save(user=self.request.user)
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = "this is a single view doing cool stuff"
        serializer.save(content=content)

    # def post(): #HTTP -> post