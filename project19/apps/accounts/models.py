from django.db import models
from django.core.mail import send_mail
from django.core.validators import EmailValidator, validate_email, validate_image_file_extension
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _


def upload_avatar_path(instance, file):
    return 'images/users/avatars/{0}/{1}'.format(instance.pk, file)


class UserManager(BaseUserManager):
    def _create_user(self, username, password, email, **extra):
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, password, email, **extra):
        extra.setdefault('is_superuser', False)
        return self._create_user(username, password, email, **extra)

    def create_super_user(self, username, password, email, **extra):
        email = self.normalize_email(email)
        user = self._create_user(username, password, email, **extra)
        user.is_admin = True
        user.save(using=self._db)


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(_('username'),  max_length=150, db_column='username', unique=True,
                                help_text=_('Required. 150 character or fewer. Letters, digits and ./-/_ only.'),
                                validators=[],
                                error_messages={
                                    'unique': _('A user with this name already exists.'),
                                    'invalid': _('Enter a valid username.'),
                                })
    email = models.EmailField(_('email'), max_length=254, db_column='email',
                              help_text=_('Required.'),
                              validators=[validate_email],
                              error_messages={
                                    'invalid': _('Enter a valid email address.'),
                                })
    first_name = models.CharField(_('first name'), max_length=30, db_column='first_name', blank=True,
                                  help_text=_('Not required. 30 character or fewer. Letters and - only.'),
                                  validators=[],
                                  error_messages={
                                      'invalid': _('Enter a valid first name.')
                                  })
    last_name = models.CharField(_('last name'), max_length=150, db_column='last_name', blank=True,
                                 help_text=_('Not required. 150 character or fewer. Letters and - only.'),
                                 validators=[],
                                 error_messages={
                                     'invalid': _('Enter a valid last name.')
                                 })
    avatar = models.ImageField(_('avatar'), db_column='avatar', blank=True, upload_to=upload_avatar_path,
                               validators=[validate_image_file_extension],
                               error_messages={
                                   'invalid': _('Please choice a valid image format.'),
                               })
    rating = models.IntegerField(_('rating'), max_length=10000, db_column='rating', default=0)
    is_active = models.BooleanField(_('active'), default=True)
    date_joined = models.DateTimeField(_('date joined'), db_column='date_joined', auto_now_add=True)

    objects = UserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['username', 'email']

    class Meta:
        verbose_name = _('user')

    def __str__(self):
        return self.username

    def get_full_name(self):
        return '{0} {1}'.format(self.first_name, self.last_name).strip()

    def get_short_name(self):
        return '{0}'.format(self.first_name).strip()

    def email_user(self, subject, message, from_email=None, **kwargs):
        return send_mail(subject, message, from_email, [self.email], **kwargs)
