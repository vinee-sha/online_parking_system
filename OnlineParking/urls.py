from django.urls import path
from . import views

urlpatterns = [
    path('', views.signin),
    path('signup/', views.signup, name = 'signup'),
    path('signup_submit/', views.signup_submit, name = 'signup_submit'),
    path('signin/', views.signin, name = 'signin'),
    path('signin_submit/', views.signin_submit, name = 'signin_submit'),
    path('forgot/', views.forgot, name = 'forgot'),
    path('forgot_submit/', views.forgot_submit, name = 'forgot_submit'),
    path('details/', views.details, name = 'details'),
    path('details_submit/', views.details_submit, name = 'details_submit'),
    path('fare/', views.fare, name = 'fare'),
    path('book/', views.booking, name = 'booking'),
]