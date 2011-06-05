"""
urls.py

Created by Chris Wood on 2011-05-08.
"""
from django.conf.urls.defaults import *
from django.conf import settings
import potpiebear
from potpiebear.ppbapp.views import *
# from django.core.mail import send_mail
# 
# send_mail('from ppb', 'yooo', 'chris@example.com',
#     ['chrissddd314159@gmail.com'], fail_silently=False)
urlpatterns = patterns('',
    url(r'^riggs/$', heyman),
)

