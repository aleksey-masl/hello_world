from django.conf.urls import url
from . import views # импортируем из текущей дирректории views

urlpatterns = [
    url('^$', views.index, name='index'),
]