from rest_framework import status, generics, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import CategorySerializer, SkillSerializer
from .models import Category, Skill




class CategoryAPI(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class SkillAPI(viewsets.ModelViewSet):
    serializer_class = SkillSerializer
    queryset = Skill.objects.all()






class CreateCategoryAPI(generics.GenericAPIView):
    serializer_class = CategorySerializer
    def post(self, request):
        serializer = self.get_serializer(data = request.data) 
        if serializer.is_valid():#Valida que los tipos de datos sean correctos
            test = Category.objects.filter(name=request.data["name"])
            if not(test):
                category = serializer.save()              
                return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


class ConsultCategory_idAPI(APIView):

    def get(self, request, *args, **kwargs):
        queryset = Category.objects.filter(id=kwargs["id"])
        returned = CategorySerializer(queryset, many=True).data
        if returned:
            return Response({"Category": returned}, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(f"No existe Categoria en la base de datos", status=status.HTTP_404_NOT_FOUND)

    def put(self, request, *args, **kwargs):
            try:
                model = Category.objects.get(id=request.data['id'])
            except Category.DoesNotExist:
                return Response(f"No existe la categoria en la base de datos", status=status.HTTP_404_NOT_FOUND)

            serializer = CategorySerializer(model, data=request.data)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)