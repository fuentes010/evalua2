from django.conf.urls import url
from core import views

urlpatterns = [
    url(r'^$', views.project_info, name='project_info'),
]
