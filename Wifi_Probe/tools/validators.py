import re
from django.core.exceptions import ValidationError


def sno_validator(value):
    if not (value.isdigit() and len(value) == 12):
        raise ValidationError('%s is not an correct number' % value)


def mac_address_validator(value):
    regex = r'^[A-F0-9]{2}(:[A-F0-9]{2}){5}$'
    regex = re.compile(regex)
    regex_matches = bool(regex.search(str(value)))
    if not regex_matches:
        raise ValidationError('%s is not a valid Mac Address' % value)


def phone_no_validator(value):
    regex = r'^[1][0-9]{10}$'
    regex = re.compile(regex)
    regex_matches = bool(regex.search(str(value)))
    if not regex_matches:
        raise ValidationError('%s is not a valid Phone Number' % value)

