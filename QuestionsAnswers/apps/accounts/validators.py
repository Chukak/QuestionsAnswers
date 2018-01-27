from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
import re


def validate_username(name):
    if re.search(r'^[A-Za-z0-9_.-]*$', name, flags=re.IGNORECASE):
        return 'valid'
    raise ValidationError('', code='invalid')


def validate_first_name(name):
    if re.search(r'^[A-Za-z-]*$', name, flags=re.IGNORECASE) and len(name) < 30:
        return 'valid'
    raise ValidationError('', code='invalid')


def validate_last_name(name):
    if re.search(r'^[A-Za-z-]*$', name, flags=re.IGNORECASE) and len(name) < 150:
        return 'valid'
    raise ValidationError('', code='invalid')


