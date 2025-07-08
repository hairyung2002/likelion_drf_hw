from rest_framework import serializers
from .models import *

class SingerSerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)

    songs = serializers.SerializerMethodField(read_only=True)

    def get_songs(self, instance):
        serializers = SongSerializer(instance.songs, many=True)
        return serializers.data
    
    class Meta:
        model = Singer
        fields = ['id', 'name', 'content', 'debut_date', 'birthday', 'nationality', 'created_at', 'updated_at', 'songs']

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['id', 'title', 'release_date', 'singer', 'content', 'genre', 'link', 'album', 'created_at', 'updated_at']
        read_only_fields = ['singer']