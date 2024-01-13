from django.urls import path
from .views import *

urlpatterns = [
    path('login/', loginUser, name="login"),
    path('logout/', logoutUser, name="logout"),
    path('register/', registerUser, name="register"),

    path('account/', userAccount, name="account"),

    path('edit-account/', editAccount, name="edit-account"),

]
