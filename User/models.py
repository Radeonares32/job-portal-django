from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.text import slugify


class CustomUser(AbstractUser):
    is_Student = models.BooleanField(default=False)
    is_Business = models.BooleanField(default=False)


class Student(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, null=True)
    image = models.ImageField(
        upload_to='students/%Y/%m/%d', null=True, default='default.jpg')
    name = models.CharField(max_length=20, null=True)
    slug = models.SlugField(verbose_name='slug', null=True)
    phone = models.CharField(max_length=10, verbose_name='phone', null=True)
    about = models.TextField(verbose_name='about', null=True)
    skills = models.CharField(max_length=200, verbose_name='skills', null=True)
    university = models.CharField(
        max_length=100, verbose_name='university', null=True)
    department = models.CharField(
        max_length=100, verbose_name='department', null=True)
    grade_average = models.IntegerField(null=True)
    classes = models.CharField(max_length=1, verbose_name='class', null=True)

    def __str__(self) -> str:
        return self.user.email

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user.email)
        super().save(*args, **kwargs)





class Business(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='business/%Y/%m/%d', default='default.jpg')
    business_name = models.CharField(
        max_length=100, null=True)
    phone = models.CharField(max_length=10, verbose_name='phone', null=True)
    slug = models.SlugField(verbose_name='slug', null=True)
    about = models.TextField(verbose_name='about', null=True)
    gmail_password = models.CharField(verbose_name='gmail password',null=True,max_length=100)

    def __str__(self) -> str:
        return self.user.email

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user.email)
        super().save(*args, **kwargs)
class Post(models.Model):
    title = models.CharField(max_length=100, null=True, verbose_name='title')
    description = models.TextField(null=True, verbose_name='description')
    tags = models.CharField(max_length=100, null=True, verbose_name='tags')
    address = models.CharField(max_length=100, null=True, verbose_name='address')
    students = models.ManyToManyField(Student, null=True, related_name='joined_jobs')
    slug = models.SlugField(verbose_name='slug', null=True)
    businesses = models.ForeignKey(Business,null=True,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)