from django.db.models import *


#user 
"""from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, email, password=None,):

        if not email:
            raise ValueError('Email must be!')
        
        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password=None, first_name='ADMIN1'):
        first_name.setdefault('is_staff', True)
        first_name.setdefault('is_superuser', True)
        return self.create_superuser(email, password, first_name)

class User(AbstractBaseUser):
    email = EmailField(unique=True)
    username = CharField(max_length=15, unique=True, blank=True, null=True)
    is_active = BooleanField(default=True)
    is_staff = BooleanField(default=False)
    is_superuser = BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ["username"]

    objects = UserManager()
    
    def __str__(self):
        return self.username"""

#user
class ModelsUser(Model):
    username = CharField(
        verbose_name="username: ",
        max_length=15,
    )
    bio = CharField(
        verbose_name="bio: ",
        max_length=43,
    )
    email = EmailField()


    def __str__(self):
        return f'{self.username}'


#post
class ModelsPost(Model):
    name = CharField(
        verbose_name="name: ",
        max_length=15,
    )
    desc = CharField(
        verbose_name="description: ",
        max_length=43,
    )
    image = ImageField(

    )
    creater = ForeignKey(ModelsUser, on_delete=CASCADE)











