from django.db import models

# Create your models here.
class TelegramFile(models.Model):
    uploaded_at = models.DateTimeField(auto_now_add=True)
    number = models.CharField(max_length=100,blank=True,null=True)
    disk_link= models.CharField(max_length=2000,blank=True,null=True)
    user_link= models.CharField(max_length=2000,blank=True,null=True)
    

    def __str__(self) -> str:
        return self.user_link