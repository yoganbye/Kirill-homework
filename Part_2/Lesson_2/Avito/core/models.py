from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


def avatar_path(instance, filename):
    return 'user_{0}/avatars/{1}'.format(instance.user.id, filename)

def ad_path(instance, filename):
    return 'user_{0}/posts/{1}'.format(instance.author.id, filename)

    
class Profile(models.Model): 
    """
    Модель профиля
    """
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='user_profile'
    )
    birth_date = models.DateField('Date of birth', null=True, blank=True)
    avatar = models.ImageField(upload_to=avatar_path, default=None)
    friends = models.ManyToManyField(User, related_name='friends', blank=True)

    def __str__(self):
        return self.user.username


class CategoriesAd(models.Model):
    '''
    Модель категорий объявлений
    '''
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name 


class Ad(models.Model):
    """
    Модель объявлений
    """
    heading = models.CharField(max_length=30)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    categories = models.ForeignKey(CategoriesAd, on_delete=models.CASCADE)
    description = models.TextField(max_length=1000, blank=True)
    image = models.ImageField(upload_to=ad_path, default=None)
    date_pub = models.DateTimeField(default=timezone.now)
    date_edit = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return 'Author {}, date {}'.format(self.author.username, self.date_pub) 


