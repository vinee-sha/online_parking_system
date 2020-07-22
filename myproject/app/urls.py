from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name = 'home'),
    path('signup/',views.something,name = 'signup'),
    path('forgot/',views.everything,name = 'forgot'),
    path('signup/details/',views.anything,name = 'details'),
    path('details/',views.anything,name = 'details'),
    path('forgot/details/',views.anything,name = 'details'),
    path('forgot/signin/',views.home,name = 'signin'),
    path('forgot/signin/details/',views.anything,name = 'details'),
    path('forgot/signin/details/page3/',views.nothing,name = 'page3'),
    path('signup/signin/',views.home,name = 'signin'),
    path('details/page3',views.nothing,name = 'page3'),
    path('signup/details/page3',views.nothing,name = 'page3'),
    path('forgot/details/page3',views.nothing,name = 'page3'),
]