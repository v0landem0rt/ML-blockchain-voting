from django.conf.urls import url
from django.urls import path
from dappx import views
# SET THE NAMESPACE!
app_name = 'dappx'
# Be careful setting the name to just /login use userlogin instead!
urlpatterns=[
    path('register/',views.register,name='register'),
    path('user_login/',views.user_login,name='user_login'),
    path('verify/',views.verify,name='verify'),
    path('register_voting/',views.register_voting,name='register_voting'),
]
