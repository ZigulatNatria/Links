from django.shortcuts import render
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
from rest_framework import viewsets, status
from rest_framework.decorators import api_view, permission_classes, schema
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.schemas import AutoSchema

from .models import Bookmark, Collections
from .serializers import BookmarkSerializer, LinkSerializer, CollectionsSerializer
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiExample
from drf_spectacular.types import OpenApiTypes


class BookmarkSerializerAPI(viewsets.ModelViewSet):
    queryset = Bookmark.objects.all()
    serializer_class = BookmarkSerializer
    permission_classes = (IsAuthenticated,)


@extend_schema(
    parameters=[OpenApiParameter(
        name='link',
        type={'type': 'string'},
        location=OpenApiParameter.QUERY,
        required=False,
        style='form',
        explode=False,
    )],
    request=OpenApiTypes.STR, responses=OpenApiTypes.STR
)
@api_view(['POST',])
@permission_classes([IsAuthenticated])
def snippet_list(request):
    if request.method == 'POST':
        serializer = LinkSerializer(data=request.data)
        if serializer.is_valid():
            print(request.data['link'])
            r = requests.get(request.data['link'])

            soup = bs(r.text, "html.parser")
            meta_tags = soup.find_all('meta', property=['og:title', 'og:image', 'og:type', 'og:description'])

            values = []
            for m_t in meta_tags:
                values.append(m_t['content'])

            keys = ["title", "image", "descriptions", "type"]

            dictionary = dict(zip(keys, values))
            print(dictionary)

            my_link = Bookmark.objects.create(
                name=dictionary['title'],
                descriptions=dictionary['descriptions'],
                link=request.data['link'],
                preview=dictionary['image'],
            )
            my_link.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CollectionsSerializerAPI(viewsets.ModelViewSet):
    queryset = Collections.objects.all()
    serializer_class = CollectionsSerializer
    permission_classes = (IsAuthenticated,)