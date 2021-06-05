from typing import Text
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, AbstractUser, UserManager, User
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField, EmailField, TextField
from django import forms


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=CASCADE)
    FRESHMAN = 'FR'
    SOPHOMORE = 'SO'
    PHD = 'PH'
    YEAR_IN_SCHOOL_CHOICES = [
        (FRESHMAN, 'Freshman'),
        (SOPHOMORE, 'Sophomore'),
        (PHD, 'PHD')
    ]
    year_in_school = models.CharField(
        max_length=2,
        choices=YEAR_IN_SCHOOL_CHOICES,
        default=FRESHMAN,
    )

    TEACHER = "1"
    STUDENT = "2"
    TYPE_CHOICES = (
    ("1", "TCH"),
    ("2", "STD"),
    )  

    COMPUTER = "1"
    MATHEMATICAION = "2"
    ELECTRIAL = "3"
    PHYSICS = "4"
    DEPT_CHOICES = (
        ("1", "COMP"),
        ("2", "MATH"),
        ("3", "ELCT"),
        ("4", "PHYS"),
    )
    department = models.CharField(
        max_length=4,
        choices=DEPT_CHOICES,
        default=COMPUTER,
    )
    type = models.CharField(
        max_length=3,
        choices=TYPE_CHOICES,
        default=STUDENT,
    )


"""
class MyAccountManager(UserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError("Users must have an email")
        if not username:
            raise ValueError("Users must have username")

        user = self.model(
            email = self.normalize_email(email),
            username=username,
        )
        user.set_password(password)
        user.save(user=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.model(
            email = self.normalize_email(email),
            password=password,
            username=username,
        )

        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user



class MyUsers(AbstractUser):
    FRESHMAN = 'FR'
    SOPHOMORE = 'SO'
    PHD = 'PH'
    YEAR_IN_SCHOOL_CHOICES = [
        (FRESHMAN, 'Freshman'),
        (SOPHOMORE, 'Sophomore'),
        (PHD, 'PHD')
    ]
    year_in_school = models.CharField(
        max_length=2,
        choices=YEAR_IN_SCHOOL_CHOICES,
        default=FRESHMAN,
    )

    TEACHER = "1"
    STUDENT = "2"
    TYPE_CHOICES = (
    ("1", "TCH"),
    ("2", "STD"),
    )  

    COMPUTER = "1"
    MATHEMATICAION = "2"
    ELECTRIAL = "3"
    PHYSICS = "4"
    DEPT_CHOICES = (
        ("1", "COMP"),
        ("2", "MATH"),
        ("3", "ELCT"),
        ("4", "PHYS"),
    )
    
    username = CharField(max_length=50,unique=True)
    password = CharField(max_length=50)
    first_name = CharField(max_length=50)
    last_name = CharField(max_length=50)
    email = EmailField(max_length=254,unique=True)
    department = models.CharField(
        max_length=4,
        choices=DEPT_CHOICES,
        default=COMPUTER,
    )
    type = models.CharField(
        max_length=3,
        choices=TYPE_CHOICES,
        default=STUDENT,
    )
    date_joined = models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="last login", auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = username
    REQUIRED_FIELDS = ['email',]

    objects = MyAccountManager()

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True
# Create your models here.
"""