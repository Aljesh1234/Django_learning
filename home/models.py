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
    address1 = models.CharField(max_length=500)
    address2 = models.CharField(max_length=500)
    phone = models.CharField(max_length=15)
    email = models.EmailField(max_length=100)
    time = models.CharField(max_length=100)
    def __str__(self):
        return self.address1

class Contact(models.Model):
    name = models.CharField(max_length=300)
    email = models.EmailField(max_length=200)
    subject = models.TextField()
    message = models.TextField()
    def __str__(self):
        return self.name


class Price(models.Model):
    rank = models.CharField(max_length=300)
    name = models.CharField(max_length=300)
    use_for = models.CharField(max_length=300)
    row_1 = models.CharField(max_length=300)
    row_2 = models.CharField(max_length=300)
    row_3 = models.CharField(max_length=200)
    price = models.IntegerField()

    def __str__(self):
        return self.name

class Skills(models.Model):
    skill = models.CharField(max_length=300)
    percentage = models.IntegerField()