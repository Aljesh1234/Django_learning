from django.db import models

# Create your models here.

class Services(models.Model):
    title = models.CharField(max_length = 300)
    description = models.TextField()
    logo = models.CharField(max_length = 100)

    def __str__(self):
        return self.title
class Feedback(models.Model):
    name = models.CharField(max_length=300)
    post = models.CharField(max_length=300)
    image = models.ImageField(upload_to='media')
    description = models.TextField()

    def __str__(self):
        return self.name
class SiteInfo(models.Model):
        address1 = models.CharField(max_length=300)
        address2 = models.CharField(max_length=300)
        phone = models.CharField(max_length=20)
        email = models.CharField(max_length=100)
        time = models.CharField(max_length=100)

        def __str__(self):
            return self.address1