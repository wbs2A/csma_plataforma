from django.db import models
from django.conf import settings
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField


class Post(models.Model):
    CATEGORIAS = (("P", "Prevenção e Cuidado"), ("De", "Denuncias"), ("Do", "Doações"), ("B", "Blog"))
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=100, blank=True, null=True)
    text = RichTextUploadingField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    image = models.FileField(blank=True, null=True)
    categoria = models.CharField(max_length=2,choices=CATEGORIAS)
    slug = models.SlugField()

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def snippet(self):
        return self.description

    def __str__(self):
        return self.title