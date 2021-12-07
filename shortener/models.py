# import random
# import string
from django.contrib.auth.models import AbstractUser, User as U
from django.db import models
from core.models import TimeStampedModel


# Create your models here.

class PayPlan(TimeStampedModel):
    name = models.CharField(max_length=20)
    price = models.IntegerField()


class Member(AbstractUser, TimeStampedModel):
    pay_plan = models.ForeignKey(PayPlan, on_delete=models.DO_NOTHING, null=True)

# class UserDetail(TimeStampedModel):
#     user = models.OneToOneField(U, on_delete=models.CASCADE)
#     pay_plan = models.ForeignKey(PayPlan, on_delete=models.DO_NOTHING, null=True)

# class Organization(TimeStampedModel):
# class Industries(models.TextChoices):
#     PERSONAL = 'personal'
#     RETAIL = 'retail'
#     MANUFACTURING = 'manufacturing'
#     EDUCATION = 'education'
#     IT = 'Information Technology'
#     OTHERS = 'others'
#
# name = models.CharField(max_length=50)
# industry = models.CharField(max_length=30, choices=Industries.choices, default=Industries.OTHERS)
# pay_plan = models.ForeignKey(PayPlan, on_delete=models.DO_NOTHING, null=True)
#

# class Member(TimeStampedModel):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     full_name = models.CharField(max_length=100, null=True)
#     organization = models.ForeignKey(Organization, on_delete=models.DO_NOTHING, null=True)
#
#
# class EmailVerification(TimeStampedModel):
#     user = models.ForeignKey(Member, on_delete=models.CASCADE)
#     key = models.CharField(max_length=100, null=True)
#     verified = models.BooleanField(default=False)
#
#
# class Categories(TimeStampedModel):
#     name = models.CharField(max_length=100)
#     organization = models.ForeignKey(Organization, on_delete=models.DO_NOTHING, null=True)
#     creator = models.ForeignKey(Member, on_delete=models.CASCADE)
#
#
# class ShortenerUrls(TimeStampedModel):
#     class UrlCreatedVia(models.TextChoices):
#         WEBSITE = 'website'
#         TELEGRAM = 'telegram'
#
#     def rand_string(self):
#         str_pool = string.digits + string.ascii_letters
#         return ("".join([random.choice(str_pool) for _ in range(6)])).lower()
#
#     nick_name = models.CharField(max_length=100)
#     category = models.ForeignKey(Categories, on_delete=models.DO_NOTHING, null=True)
#     prefix = models.CharField(max_length=50)
#     creator = models.ForeignKey(Member, on_delete=models.CASCADE)
#     create_via = models.CharField(max_length=8, choices=UrlCreatedVia.choices, default=UrlCreatedVia.WEBSITE)
