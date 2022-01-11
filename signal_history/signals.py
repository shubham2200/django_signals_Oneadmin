from django.db.models.enums import Choices
from django.db.models.fields.related_descriptors import create_forward_many_to_many_manager
from django.dispatch import *
from django.db.models.signals import post_save, pre_delete
from django.contrib.auth.models import User
from .models import *
from datetime import datetime


# from datetime import date, datetime

# # this is a signals function on here


# @receiver(post_save , sender = User)
# def register_save(sender, instance, created, **kwargs):
#     if created:
#         authenticate_history.objects.create( 
#         user_name = instance , 
#         # date_time = datetime.now()

#     )
      
# @receiver(post_save , sender = User)
# def login_datetime(sender , instance , created , **kwargs):
#     if created:
#         authenticate_history.objects.filter( 
#             recordstype 
#             date_time = datetime.now()
# )

