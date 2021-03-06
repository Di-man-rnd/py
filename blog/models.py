from django.db import models
from ckeditor.fields import RichTextField
from tinymce.models import HTMLField

class Main(models.Model):
    YEAR = (
        ('FR', 'Freshman'),
        ('SO', 'Sophomore'),
        ('JR', 'Junior'),
        ('SR', 'Senior'),
    )

    name = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True, null=True)
    point = models.CharField(choices=YEAR, default='SO', max_length=100, blank=True, null=True)
    date_create = models.DateField(auto_now_add=True, blank=True, null=True)
    comment = RichTextField(blank=True, null=True)
    tiny = models.TextField()     #HTMLField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'youtube'


class PhoneNotis(models.Model):
    main = models.ForeignKey(Main)
    phone = models.CharField(max_length=10, blank=True, null=True)
