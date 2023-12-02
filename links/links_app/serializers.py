from rest_framework import serializers
from .models import Bookmark, Collections


class BookmarkSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bookmark
        fields = (
            'id',
            'name',
            'link',
            'preview',
            'descriptions',
            'date_created',
            'date_change',
            'links_collections',
        )


class CollectionsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Collections
        fields = (
            'id',
            'name',
            'description',
            'date_created',
            'date_change',
        )


class LinkSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bookmark
        fields = (
            'link',
        )