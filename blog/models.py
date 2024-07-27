from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    data_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name="post_like", blank=True)


    #TRACK OR COUNT OF LIKES
    def number_of_likes(self):
        return self.likes.count()

    def __str__(self):
       return self.title
  
    
    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"pk": self.pk})
    

    
class comment(models.Model):
    post =  models.ForeignKey(Post,related_name="comments" ,on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    body= models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.post.title,self.name)