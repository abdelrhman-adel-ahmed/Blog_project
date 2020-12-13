from django.db import models
from django.contrib.auth.models import User
#pillow (Python Imaging Library)
from PIL import Image
#wfrom django.contrib.auth.models import AbstractUser ,BaseUserManager


#User model (built in) doesnot have pic filed ,so we will extened it and add one to one realation ship
#one user can have one profile  and one profile  associated with one user

class Profile(models.Model):
    #one to one relation with the User,if user deleted deleted the profile but not vice versta
    user=models.OneToOneField(User,on_delete=models.CASCADE)

    #defult formate ,and dirctoray the pics get upload to
    #need pillow lib to work
    image=models.ImageField(default='default.jpg',upload_to='profile_pics')


    def __str__(self):
        return f"{self.user.username} profile"
        

    #we need to auto_resize the image if it large because the image filed is aroung 125px so we dont need very
    #larege image that will slow the site while uploading and sending and also space for saving
    #we need to over 
    def save(self, *args, **kwargs):
        #run save method that exist in pareent calls to save the image 
        super().save(*args, **kwargs)

        #open the image of the current instance 
        img=Image.open(self.image.path)

        #crop the img to 300 
        if img.height >300 or img.width>300:
            output_size=(300,300)   
            img.thumbnail(output_size)
            #overwrite the large image version
            img.save(self.image.path)

# class CustomUser(AbstractUser ):
#     email=models.EmailField(verbose_name="email",unique=True)
#     date_of_birth = models.DateField()
#     is_active = models.BooleanField(default=True)
#     is_admin = models.BooleanField(default=False)
#     is_staff= models.BooleanField(default=False)
#     is_superuser= models.BooleanField(default=False)

#     USERNAME_FIELD='email'
#     REQUIRED_FIELDS=['email,']

#     def has_perm(self,perm,obj=None):
#         return self.is_admin
    
#     def has_module_perms(self,app_label)
