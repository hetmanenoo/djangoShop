from django.db import models
from django.contrib.auth.models import User, AbstractUser, BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, email, username, password, ):
        user = self.model(
            email = self.normalize_email(email),
            username = username,)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, username):

        user = self.create_user(
            email = email,
            username=username,
            password=password,
        )

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user
class Register(AbstractUser):
    email = models.EmailField(null=False) #unique=True забрав для лоігна через github з своєю поштою
    username = models.CharField(max_length=25, unique=True)
    password = models.CharField(max_length=25)

    objects = UserManager()
    USERNAME_FIELD = "username"
    # REQUIRED_FIELDS = ["username",]

