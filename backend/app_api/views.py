#for getting json data JsonResponse
from django.http import JsonResponse,HttpResponse
from django.forms.models import model_to_dict
import json
from app_product.models import Products

#for django rest framework
from rest_framework.decorators import api_view
from rest_framework.response import Response
#for serializer
from app_product.serializers import ProductSerializer







# Create your views here.
#this is for Json
# def api_home(request):
#     #request->Httpresponse->Django
#     #print(dir(request))
#     #request.body
#     # body = request.body #byte string json data
#     # data_body = {}
#     # try:
#     #     data_body = json.loads(body) #string of jsdon data->python dict
#     # except:
#     #     pass
#     # print(data_body.keys())
#     # data = ["message : Hi there this is your first django API response"]
#     # return JsonResponse(data, safe=False)

#     model_data = Products.objects.all().order_by("?").first()
#     data= {}
#     if model_data:
#         # data['id']= model_data.id
#         # data['title']= model_data.title
#         # data['content']= model_data.content
#         # data['price']= model_data.price
#         #model instance (model_data)
#         # turn into python dict
#         #return json to my client
#         data = model_to_dict(model_data, fields=['id','title'])
#     return JsonResponse(data, safe=False)



#this is for rest framework
#for get method
# @api_view(["GET",])
# def api_home(request):
#     #drf api view
#     # if request.method=="POST":
#     #     return Response({"detail":"GET not allowed"},status=405)
#     instance = Products.objects.all().order_by("?").first()
#     data = {}
#     if instance:
#         #data = model_to_dict(instance,fields=['title','content','price','sale_price'])
#         #for serializers we can write
#         data = ProductSerializer(instance).data

#     return Response(data)


#for post method
@api_view(['POST'])
def api_home(request):
    serializer = ProductSerializer(data= request.data)
    if serializer.is_valid(raise_exception=True):
        #instance= serializer.save()
        print(serializer.data)
        return Response(serializer.data)
    return Response({"invalid":"not good data"},status=400)
   
