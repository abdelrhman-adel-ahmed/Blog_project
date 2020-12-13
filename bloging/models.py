from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

#each table represented as class ,each class attribute is filed (attribute) in our table
#python manage.py sqlmigrate (name of the app)(name of the file that get created ) <-- show the sql statment

class post(models.Model):
    title=models.CharField(max_length=30)
    content=models.TextField()
    date=models.DateTimeField(default=timezone.now)
    #if user get deleted delete the post    
    author=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} {self.content}" 

    #redirect -> redirect to specific route reverse-> reutrn the url as string ,then the view(postview) 
    #will take that url and redirect us to the location we specified wich is the 'post/<int:pk>/'
    def get_absolute_url(self):
        return reverse("post-detail",kwargs={"pk":self.id})
  



