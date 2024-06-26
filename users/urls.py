from django.urls import path
from .views import UserUpdateView, UserLoginView, UserRegisterView, UserLogoutView

app_name = "users"

urlpatterns = [
    path("register/", UserRegisterView.as_view(), name="register"),
    path("login/", UserLoginView.as_view(), name="login"),
    path("logout/", UserLogoutView.as_view(), name="logout"),
    path("<int:pk>/update", UserUpdateView.as_view(), name="update"),
]
