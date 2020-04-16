from django.db.models import BooleanField
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    is_provider = BooleanField(verbose_name="Is provider ?", default=False)