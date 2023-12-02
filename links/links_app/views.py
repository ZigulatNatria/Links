from django.shortcuts import render
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Bookmark, Collections
from .serializers import BookmarkSerializer, LinkSerializer, CollectionsSerializer


class BookmarkSerializerAPI(viewsets.ModelViewSet):
    queryset = Bookmark.objects.all()
    serializer_class = BookmarkSerializer


@api_view(['POST',])
def snippet_list(request):
    """
    List all code snippets, or create a new snippet.
    """
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