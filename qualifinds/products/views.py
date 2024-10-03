from drf_spectacular.utils import extend_schema, OpenApiParameter
from rest_framework import status, serializers
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response

from products.application.get_products_use_case import GetProductsUseCase

from products.infrastructure.tiendasjumbo_products_repository import TiendasJumboProductsRepository


class GetProductsSerializer(serializers.Serializer):
    url = serializers.CharField(max_length=100, default='https://www.tiendasjumbo.co/supermercado/despensa/aceite')

class GetProductsView(APIView):
    permission_classes = [AllowAny]

    @extend_schema(
        request=GetProductsSerializer,
        responses={201: GetProductsSerializer, 400: 'Invalid data'},
        operation_id='getProducts',
        summary='Get products',
        description='Get products.',
    )
    def post(self, request):
        serializer = GetProductsSerializer(data=request.data)
        if serializer.is_valid():
            validated_data = serializer.validated_data
            url = validated_data['url']
            use_case = GetProductsUseCase(repository=TiendasJumboProductsRepository(url=url))
            result = use_case.execute(url=url)

            return Response(result, status=status.HTTP_201_CREATED)