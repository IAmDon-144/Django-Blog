from django.db import models
from embed_video.fields import EmbedVideoField

class Video(models.Model):
    title = models.CharField(null=True,max_length=350)
    content = models.TextField(blank=True)
    video = EmbedVideoField()
    updated = models.DateTimeField(auto_now=True,null=True)
    created = models.DateTimeField(auto_now_add=True,null=True)  

    def __str__(self):
        return f'{self.title}'
    
    class Meta:
        ordering = ['-created']