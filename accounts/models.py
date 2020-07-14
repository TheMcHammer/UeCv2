from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin
)

class UserManager(BaseUserManager):
    def create_user(self, email, username, password=None, is_staff=False, is_admin=False, is_active=True, **extra_fields):

        if not email:
            raise ValueError("User must have email address")
        if not username:
            raise ValueError("User must have a username")
        if not password:
            raise ValueError("User must have a password")


        user_obj = self.model(
            email = self.normalize_email(email,
            #username=username,
            ** extra_fields)
        )
        user_obj.set_password(password)
        user_obj.staff = is_staff
        user_obj.admin = is_admin
        user_obj.active = is_active
        user_obj.save(using=self._db)
        return user_obj

    def create_staffuser(self, email, username, password=None, **extra_fields):
        user=self.create_user(
            email,
            username,
            password=password,
            is_staff=True,
            ** extra_fields
        )
        return user

    def create_superuser(self, email, username, password=None, **extra_fields):
        user = self.create_user(
            email,
            username,
            password=password,
            is_staff=True,
            is_admin=True,
            ** extra_fields
        )
        return user

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    username = models.CharField(max_length=255, unique=True, blank=True, null=True)
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
    #groups = models.ManyToManyField()
    #is_student = models.BooleanField(default=False)
    #is_counsel = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'

    REQUIRED_FIELDS = ['email']

    objects = UserManager()

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return "/users/%i/" % (self.pk)

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.staff
    @property
    def is_admin(self):
        return self.admin
    @property
    def is_active(self):
        return self.active


class user_type(models.Model):
     is_counsel = models.BooleanField(default=False)
     is_student = models.BooleanField(default=False)
     user = models.OneToOneField(User, on_delete=models.CASCADE)

     def __str__(self):
         if self.is_student == True:
             return User.get_username(self.user) + " - is_student"
         else:
             return User.get_username(self.user) + " - is_counsel"