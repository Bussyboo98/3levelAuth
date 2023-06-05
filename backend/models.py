

from django.db import models

class Image(models.Model):
    name = models.CharField(max_length=255)
    mime = models.CharField(max_length=255)
    data = models.BinaryField()
    uname = models.CharField(unique=True, verbose_name="Username", max_length=255)
    umail = models.EmailField()
    password = models.CharField(max_length=255)
    profile = models.ImageField(default="", blank=True, null=True, help_text='Dimension 600px X 671px')
    def __str__(self):
        return self.name
    
    verbose_name = 'Us'
    
    def imga_get_absolute_url(self):
       if self.profile:
            return self.profile.url

class UserInfo(models.Model):
    umail = models.TextField()
    uspass = models.TextField()
