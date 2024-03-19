from django.urls import path
from . import views
urlpatterns = [
    path("user_signup/",views.user_signup,name="user_signup"),
    path("user_sign_in/",views.user_sign_in,name="user_sign_in"),
    path("user_logout/",views.user_logout,name="user_logout"),
    path("user_signup_page/<str:message>/<str:message_type>",views.user_signup_page,name="user_signup_page"),
    path("user_login_page/<str:message>/<str:message_type>",views.user_login_page,name="user_login_page"),
]