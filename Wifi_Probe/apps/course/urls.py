from django.conf.urls import url
from apps.course import views


urlpatterns = [
    url(r'home', views.elect_course),
]
