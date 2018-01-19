from django.db import models
from django.core.mail import send_mail
from django.core.validators import EmailValidator, validate_email, validate_image_file_extension
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _


# get path for avatar
def upload_avatar_path(instance, file):
    # {0} - id user, {1} - filename
    return 'users/images/avatars/{0}/{1}'.format(str(instance.id), file)


# override manager user model
class UserManager(BaseUserManager):
    # create user method
    def _create_user(self, username, password, email, **extra):
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra)
        user.set_password(password)
        user.save(using=self._db)
        return user

    # set superuser fields false and return create func
    def create_user(self, username, password, email, **extra):
        extra.setdefault('is_superuser', False)
        return self._create_user(username, password, email, **extra)

    # creates superuser method
    def create_superuser(self, username, password, email, **extra):
        email = self.normalize_email(email)
        user = self._create_user(username, password, email, **extra)
        user.is_admin = True
        user.save(using=self._db)


# custom user model with permission mixin methods
class User(AbstractBaseUser, PermissionsMixin):
    # id field
    id = models.AutoField(_('id'), auto_created=True, primary_key=True)
    # username field
    username = models.CharField(_('username'),  max_length=150, db_column='username', unique=True,
                                help_text=_('Required. 150 character or fewer. Letters, digits and ./-/_ only.'),
                                validators=[],
                                error_messages={
                                    'unique': _('A user with this name already exists.'),
                                    'invalid': _('Enter a valid username.'),
                                })
    # email field
    email = models.EmailField(_('email'), max_length=254, db_column='email',
                              help_text=_('Required.'),
                              validators=[validate_email],
                              error_messages={
                                    'invalid': _('Enter a valid email address.'),
                                })
    # first_name field
    first_name = models.CharField(_('first name'), max_length=30, db_column='first_name', blank=True,
                                  help_text=_('Not required. 30 character or fewer. Letters and - only.'),
                                  validators=[],
                                  error_messages={
                                      'invalid': _('Enter a valid first name.')
                                  })
    # last_name field
    last_name = models.CharField(_('last name'), max_length=150, db_column='last_name', blank=True,
                                 help_text=_('Not required. 150 character or fewer. Letters and - only.'),
                                 validators=[],
                                 error_messages={
                                     'invalid': _('Enter a valid last name.')
                                 })
    # avatar field
    avatar = models.ImageField(_('avatar'), db_column='avatar', blank=True, upload_to=upload_avatar_path,
                               validators=[validate_image_file_extension],
                               error_messages={
                                   'invalid': _('Please choice a valid image format.'),
                               })
    # rating field
    rating = models.IntegerField(_('rating'), db_column='rating', default=0)
    # active field
    is_active = models.BooleanField(_('active'), default=True)
    # admin field
    is_admin = models.BooleanField(_('admin'), default=False)
    # date joined
    date_joined = models.DateTimeField(_('date joined'), db_column='date_joined', auto_now_add=True)
    # manager for model
    objects = UserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    class Meta:
        verbose_name = _('user')
        db_table = 'user'

    def __str__(self):
        return self.username

    # get first_name + last_name
    def get_full_name(self):
        return '{0} {1}'.format(self.first_name, self.last_name).strip()

    # get only first_name
    def get_short_name(self):
        return '{0}'.format(self.first_name).strip()

    def email_user(self, subject, message, from_email=None, **kwargs):
        return send_mail(subject, message, from_email, [self.email], **kwargs)

    # override save method
    def save(self, *args, **kwargs):
        # set avatar and call func upload_to of ImageField with ID object
        # create path with id object after save
        if self.id is None and self.avatar:
            image = self.avatar
            self.avatar = None
            super().save(*args, **kwargs)
            self.avatar = image
        return super().save(*args, **kwargs)

    # check user is staff or not
    @property
    def is_staff(self):
        return self.is_admin
