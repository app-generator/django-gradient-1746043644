# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__
    username = models.TextField(max_length=255, null=True, blank=True)
    type_ account = models.TextField(max_length=255, null=True, blank=True)
    phone = models.TextField(max_length=255, null=True, blank=True)
    status = models.TextField(max_length=255, null=True, blank=True)

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Start_Company(models.Model):

    #__Start_Company_FIELDS__
    name = models.TextField(max_length=255, null=True, blank=True)
    adress = models.TextField(max_length=255, null=True, blank=True)
    phone = models.TextField(max_length=255, null=True, blank=True)
    email = models.TextField(max_length=255, null=True, blank=True)

    #__Start_Company_FIELDS__END

    class Meta:
        verbose_name        = _("Start_Company")
        verbose_name_plural = _("Start_Company")


class Start_Departments(models.Model):

    #__Start_Departments_FIELDS__
    start_company_id = models.ForeignKey(start_company, on_delete=models.CASCADE)
    name = models.TextField(max_length=255, null=True, blank=True)

    #__Start_Departments_FIELDS__END

    class Meta:
        verbose_name        = _("Start_Departments")
        verbose_name_plural = _("Start_Departments")


class Start_Sections(models.Model):

    #__Start_Sections_FIELDS__
    start_departments_id = models.ForeignKey(start_departments, on_delete=models.CASCADE)
    name = models.TextField(max_length=255, null=True, blank=True)

    #__Start_Sections_FIELDS__END

    class Meta:
        verbose_name        = _("Start_Sections")
        verbose_name_plural = _("Start_Sections")


class Start_Access(models.Model):

    #__Start_Access_FIELDS__
    start_users_id = models.TextField(max_length=255, null=True, blank=True)
    start_sections_id = models.ForeignKey(start_sections, on_delete=models.CASCADE)
    access_type = models.TextField(max_length=255, null=True, blank=True)

    #__Start_Access_FIELDS__END

    class Meta:
        verbose_name        = _("Start_Access")
        verbose_name_plural = _("Start_Access")



#__MODELS__END
