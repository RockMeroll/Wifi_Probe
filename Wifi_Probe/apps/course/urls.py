from django.conf.urls import url
from apps.course import views


urlpatterns = [
    url(r'elect_course/', views.elect_course),
]
