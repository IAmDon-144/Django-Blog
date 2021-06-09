from django.db import models
from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import User
from embed_video.fields import EmbedVideoField
from ckeditor.fields import RichTextField

class Catagory(models.Model):
    name = models.CharField(max_length=40)
    image = models.ImageField(upload_to = 'Category', validators=[FileExtensionValidator(['png','jpg','jpeg'])],blank = False)

    def __str__(self):
        return self.name[0:20]



class images(models.Model):
    title = models.CharField(max_length=350)
    content = RichTextField(blank=True)
    image = models.ImageField(upload_to = 'gallary', validators=[FileExtensionValidator(['png','jpg','jpeg'])],blank = True)
    image1 = models.ImageField(upload_to = 'gallary', validators=[FileExtensionValidator(['png','jpg','jpeg'])],blank = True)
    image2 = models.ImageField(upload_to = 'gallary', validators=[FileExtensionValidator(['png','jpg','jpeg'])],blank = True)
    image3 = models.ImageField(upload_to = 'gallary', validators=[FileExtensionValidator(['png','jpg','jpeg'])],blank = True)
    subCat = models.CharField(blank=True,max_length=400)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    liked = models.ManyToManyField(User,default=None,related_name='likes',blank=True)
    category  = models.ManyToManyField(Catagory,default=None,related_name='catagory',blank=False,)





    def __str__(self):
        return f'{self.title[0:10]}'
    def num_likes(self):
        return self.liked.all().count()
    def CommentCount(self):
        return self.comment_set.all().count()
    
    class Meta:
        ordering = ['-created']



class Comment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(images,on_delete=models.CASCADE)
    body = models.TextField(max_length=300)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.pk)
    class Meta:
        ordering = ['-created']




class Like(models.Model):
    LIKE_CHOICES = (
        ('Like','Like'),
        ('Unlike','Unlike'),
        )
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(images,on_delete=models.CASCADE)
    value = models.CharField(max_length=8,choices=LIKE_CHOICES)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user}-{self.post}-{self.value}"

