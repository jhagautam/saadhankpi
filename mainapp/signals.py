from django.db.models.signals import post_save
from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from mainapp.models import user_firm
from django.shortcuts import redirect
from django.conf import settings as s

def post_login(sender, user, request, **kwargs):
    pass

user_logged_in.connect(post_login)
