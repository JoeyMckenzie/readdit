from django.conf.urls import url
from . import views

app_name = 'accounts'

urlpatterns = [
    url(r'^create_account/', views.create_account, name="create_account"),
    url(r'^login_user/', views.login_user, name="login_user"),
    url(r'^logout_user/', views.logout_user, name="logout_user")
]
