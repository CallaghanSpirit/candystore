from django.db import models
from django_extensions.db.fields import AutoSlugField
from transliterate import slugify
from django.urls import reverse

#Create my own manager
class Main_Manager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=Goods.Status.IN_STOCK)



# Create your models here.
class Goods(models.Model):
    class Status(models.IntegerChoices):
        OUT_OF_STOKE = 0, 'Не в наличии'
        IN_STOCK = 1, 'В наличии'

    name = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from = 'name')
    photo = models.ImageField(upload_to='images/',null=True)
    desc = models.TextField(blank=True)
    cats = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, related_name='goods')
    tags = models.ManyToManyField('Tags', blank=True, related_name='gtags')
    status = models.BooleanField(Status,default=Status.OUT_OF_STOKE)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    

    objects = models.Manager()
    manager = Main_Manager() 


    def slugify_function(self,content):
        return slugify(content)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Авто товары"
        verbose_name_plural = "Авто товары"
        ordering = ['-time_create']
        indexes = [
            models.Index(fields=['-time_create'])
        ]

    def get_absolute_url(self):
        return reverse('card-page', kwargs={'gd_slug': self.slug})

class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = AutoSlugField(populate_from = 'name')
    
    
    def __str__(self):
        return self.name
    
    def slugify_function(self,content):
        return slugify(content)
    
    def get_absolute_url(self):
        return reverse('cat', kwargs={'cat_slug': self.slug})
    
class Tags(models.Model):
    tag = models.CharField(max_length=100, db_index=True)
    slug = AutoSlugField(populate_from = 'tag')

    def __str__(self):
        return self.tag
    
    def slugify_function(self,content):
        return slugify(content)
    
    def get_absolute_url(self):
        return reverse('tag', kwargs={'tag_slug': self.slug})