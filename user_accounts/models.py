from django.db import models
from django.contrib.auth.models import User, BaseUserManager, AbstractBaseUser

# Create your models here.
class FairyUserManager(BaseUserManager):

    def create_user(self, email, username, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
            username=username,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class FairyUser(AbstractBaseUser):
    email           = models.EmailField(verbose_name='email address', max_length=255, unique=True)
    username        = models.CharField(max_length=30, unique=True)
    date_of_birth   = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
    is_active       = models.BooleanField(default=True)
    is_admin        = models.BooleanField(default=False)

    objects = FairyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username',]

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin


class Profile(models.Model):
    user            = models.OneToOneField(FairyUser, on_delete=models.CASCADE)
    designation     = models.CharField(max_length=30, blank=True, null=True)
    rattings        = models.SmallIntegerField(blank=True, null=True)
    short_bio       = models.TextField(blank=True, null=True, max_length=500)
    avatar          = models.ImageField(upload_to='avatar/%s/%Y/%m/%d', max_length=255, blank=True, null=True)

    class Meta:
        ordering = ('-rattings', )


class EmployeeManager(models.Manager):
    def get_queryset():
        return super().get_queryset().filter(profile__designation='Employee')


class Employee(FairyUser):
    class Meta:
        ordering = ('email',)
        proxy = True
    
    objects = EmployeeManager()