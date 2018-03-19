from django.conf.urls import url
from . import views

app_name = 'accounts'

urlpatterns = [
    url(r'^register/$', views.UserRegView.as_view(), name='register'),
    url(r'^login/$', views.UserFormView.as_view(), name='login'),
]
