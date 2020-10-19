from django.db import models
from django.template.defaultfilters import slugify
from ckeditor.fields import RichTextField
# from django.db.models.signals import pre_save
# from os_project.utils import unique_slug_generator

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


STATUS_CHOICES = (
    ('draft', 'Draft'),
    ('published', 'PUBLISHED'),
)


class Post(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    blog_type = models.ForeignKey(Category, on_delete=models.CASCADE)
    text = models.TextField()
    text2 = RichTextField(null=True, blank=True)
    published_at = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now_add=True)
    status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default='draft')

    class Meta:
        ordering = ('published_at',)

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)
