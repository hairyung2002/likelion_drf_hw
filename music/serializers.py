from rest_framework import serializers
from .models import *

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

class SingerSerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)

    songs = serializers.SerializerMethodField(read_only=True)
    image = serializers.ImageField(use_url=True, required=False)


    def get_songs(self, instance):
        serializers = SongSerializer(instance.songs, many=True)
        return serializers.data
    
    tags = serializers.SerializerMethodField()
    def get_tags(self, instance):
        tag = instance.tags.all()
        return [t.name for t in tag]

    class Meta:
        model = Singer
        fields = '__all__'

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['id', 'title', 'release_date', 'singer', 'content', 'genre', 'link', 'album', 'created_at', 'updated_at']
        read_only_fields = ['singer']