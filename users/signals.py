from django.db.models.signals import post_save 
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

#fire a signal when user is created , and we want to create profile  when user if created instead of doing 
#that manully in the admin page (note:user redirect to profile page with there name and email and empty pic
# but there is not profile created)


#when ever user get saved the reciver will notified and the function will invoked and created profile for that user
@receiver(post_save,sender=User)
def create_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)

#save the profile that got created
@receiver(post_save,sender=User)
def save_profile(sender,instance,**kwargs):
    try:
        instance.profile.save()
    except ObjectDoesNotExist:
        Profile.objects.create(user=instance)


