from django.conf.urls import url

from . import views

app_name = 'savingscalculator'

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^queries$', views.queries, name='queries'),
]