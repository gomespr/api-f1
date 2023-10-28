from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response

from ..models import Constructor
from ..serializers import ConstructorSerializer


@api_view()
def constructor_api_detail(request, constructorRef):
    constructors = get_object_or_404(Constructor, constructorRef=constructorRef)
    serializer = ConstructorSerializer(
        instance=constructors,
        many=False,
        context={'request': request},
    )
    return Response(serializer.data)