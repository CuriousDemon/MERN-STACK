from django.urls import path
from signupform import views
urlpatterns = [
    path('', views.signup_page),
    path('signin/', views.signin_page),
    path('signin/dashboard/', views.dashboard),
    path('signin/dashboard/note/', views.manager),
]