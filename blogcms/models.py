from django.db import models
from accounts.models import CustomUser

class BlogPost(models.Model):
    title = models.CharField(max_length=256, blank=False, null=False)
    content = models.TextField(max_length=256, blank=False, null=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=False)
    author  = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering =['created_on']
    


class PostComment(models.Model):
    blog = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE) 
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    
