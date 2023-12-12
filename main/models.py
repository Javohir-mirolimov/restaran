from django.db import models

class  Banner(models.Model):
    title = models.CharField(max_length=55)
    text = models.CharField(max_length=255)
    img = models.ImageField(upload_to='banner_photo/')




    def __str__(self):
        return self.title




class About_Us(models.Model):
    title = models.CharField(max_length=55)
    text = models.TextField()
    img = models.ImageField(upload_to='about_photo/')
    is_right = models.BooleanField(default=False)
    is_left = models.BooleanField(default=True)


    def __str__(self):
        return self.title



class Meal(models.Model):
    name = models.CharField(max_length=55)
    price = models.IntegerField()
    img = models.ImageField(upload_to='meal_photo/')



    def __str__(self):
        return self.name


class Award(models.Model):
    img = models.ImageField(upload_to='award_photo/')


class Testimonial(models.Model):
    client_name = models.CharField(max_length=25)
    client_last_name = models.CharField(max_length=25)
    client_avatar  = models.ImageField(upload_to='avatar_photo/')
    comment = models.CharField(max_length=255)


    def __str__(self):
        return self.client_name



class Order(models.Model):
    last_name = models.CharField(max_length=25)
    day = models.DateField()
    time = models.TimeField()
    select_person = models.IntegerField()
    message  = models.TextField()




class Info(models.Model):
    brand = models.CharField(max_length=25)
    facebook = models.CharField(max_length=55)
    instagram = models.CharField(max_length=55)
    twitter = models.CharField(max_length=55)
    img = models.ImageField(upload_to='info_photo/')
