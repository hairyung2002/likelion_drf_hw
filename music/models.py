from django.db import models

# Create your models here.
class Tag(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
def image_upload_path(instance, filename):
    return f'{instance.pk}/{filename}'

class Singer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    debut_date = models.DateField()
    birthday = models.DateField()
    nationality = models.CharField(max_length=50, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    tags = models.ManyToManyField(Tag, blank=True, related_name='singers')
    image = models.ImageField(upload_to=image_upload_path, blank=True, null=True)

    def __str__(self):
        return str(self.id)

class Song(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    release_date = models.DateField()
    singer = models.ForeignKey(Singer, blank=False, on_delete=models.CASCADE, related_name='songs')
    content = models.TextField()
    genre = models.CharField(max_length=50, blank=True)
    link = models.URLField(blank=True)
    album = models.CharField(max_length=100, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)