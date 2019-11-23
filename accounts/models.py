from django.db import models
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='profile_pics/default.jpg', upload_to='profile_pics',blank=True,null=True)
    bio = models.TextField(max_length=500, blank=True, help_text='Minha descrição')
    location = models.CharField(max_length=30, blank=True, help_text="Local onde mora")
    birth_date = models.DateField(null=True, blank=True, help_text='Data de Nascimento')
    signup_confirmation = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user.username} Profile'

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()