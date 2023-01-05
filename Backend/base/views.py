from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import Product
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
# Create your views here.


#  /////////////// login start
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # Add custom claims
        token['username'] = user.username
        # ...
        return token
 
 
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

@api_view(['POST'])
def register(request):
    user = User.objects.create_user(
                username=request.data['username'],
                email=request.data['email'],
                password=request.data['password']
            )
    user.is_active = True
    user.is_staff = True
    user.save()
    return Response("new user born")


# /////////////////////// login end

# public index
@api_view(['GET'])
def index(request):
    return Response("hello")

# login test
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def test(request):
    return Response("test")

# login with data test
@api_view(['GET','POST','DELETE','PUT','PATCH'])
@permission_classes([IsAuthenticated])
def products(req):
    if req.method =='GET':
        user= req.user
        ar=[]
        for pro in  user.product_set.all():
            ar.append({"id":pro.id, "desc":pro.desc, "price":pro.price})
        return Response(ar)
    if req.method =='POST':
       
        return Response ("post...")



