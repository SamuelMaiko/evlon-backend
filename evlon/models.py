from django.db import models
from accounts.models import CustomUser

# Create your models here.
class Post(models.Model):
    imageURL=models.CharField(max_length=200)
    caption=models.CharField(max_length=100, null=True, blank=True)
    Location=models.CharField(max_length=100, null=True, blank=True)
    Time=models.CharField(max_length=100, null=True, blank=True)
    timeRemaining=models.IntegerField( null=True, blank=True)
    Attendance=models.IntegerField( null=True, blank=True)
    likesCount=models.IntegerField( null=True, blank=True)
    commentsCount=models.IntegerField( null=True, blank=True)
    smallProfile=models.CharField(max_length=200, default="./Rong.jpg", null=True, blank=True)
    name=models.CharField(max_length=50, null=True, blank=True)
    counter=models.IntegerField( null=True, blank=True)
    
    class Meta:
        db_table="EvlonPosts"
    
    def __str__(self):
        return self.name

class Comment(models.Model):
    user=models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="comments")
    description=models.TextField()
    likesCount=models.IntegerField()
    
    class Meta:
        db_table="EvlonComments"
    
    def __str__(self):
        return f"{self.user.username}'s comment"
    
    
