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
    text2 = RichTextField()
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


# def slug_genarator(sender, instance, *args, **kwargs):
#     if not instance.slug:
#         instance.slug = unique_slug_generator(instance)


# pre_save.connect(slug_genarator, sender=Post)


# class SubCategory(models.Model):
#     name = models.CharField(max_length=100)
#     category = models.ForeignKey(
#         Category, on_delete=models.CASCADE, blank=True)

#     def __str__(self):
#         return self.name
# class BlogPost(models.Model):
#     category = models.ForeignKey(
#         Category, on_delete=models.CASCADE, blank=True)
#     title = models.CharField(max_length=50)
#     thumbnaiul = models.ImageField(upload_to='main/blogimg')
#     description = models.TextField(max_length=1000)
#     # views = models.Model(default=0)

#     def __str__(self):
#         return self.title
