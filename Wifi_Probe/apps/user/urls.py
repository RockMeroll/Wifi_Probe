from django.conf.urls import url
from apps.user import views


urlpatterns = [
    url(r'home', views.home),
    url(r'login/$', views.login),
    url(r'logout/$', views.logout),
    url(r'register/$', views.register),
    url(r'register/captcha/send', views.captcha_send),
    url(r'register/captcha/verify', views.captcha_verify),
]
