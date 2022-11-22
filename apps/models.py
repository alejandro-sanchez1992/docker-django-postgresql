import datetime
import secrets

from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import serializers
import sys
import inspect


'''
Leave this Helper Class in the TOP of the file
'''
class Utils:
    @staticmethod
    def get_class(config, name: str) -> models.Model:
        return Utils.model_name_to_class(config[name])

    @staticmethod
    def get_manager(config, name: str) -> models.Manager:
        return Utils.get_class(config, name).objects

    @staticmethod
    def get_serializer(config, name: str):
        class Serializer(serializers.ModelSerializer):
            class Meta:
                model = Utils.get_class(config, name)
                fields = '__all__'

        return Serializer

    @staticmethod
    def model_name_to_class(name: str):
        all_classes = inspect.getmembers(sys.modules[__name__], inspect.isclass)
        for cls in all_classes:
            if cls[0] == name:
                return cls[1]
        # we are confident that never returns None
        return None

    @staticmethod
    def user_directory_path(instance, filename):
      
        # file will be uploaded to MEDIA_ROOT / user_<id>/<filename>
        return 'media/file_{0}/{1}'.format(secrets.token_hex(6), filename)

'''
Add your models below
'''

class Book(models.Model):
    class Meta:
        app_label = 'apps'

    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    image = models.ImageField(upload_to = Utils.user_directory_path)
    created_at = models.DateTimeField(auto_now_add=True)
    description = models.TextField()

    '''ForeignKey Example'''
    #client = models.ForeignKey(Client, blank=True, null=True, on_delete=models.DO_NOTHING)


# Create your models here.









