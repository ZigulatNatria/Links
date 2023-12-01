from rest_framework import serializers
from .models import Bookmark


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


class LinkSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bookmark
        fields = (
            'link',
        )