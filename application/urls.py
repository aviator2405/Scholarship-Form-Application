from django.contrib import admin
from django.urls import path
from application import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),    
    path('profile/', views.profile, name='profile'),    
    path('logout/', views.logoutfunc, name='logout'),    
    path('application/personal-info', views.appPerInfo, name='appPerInfo'),    
    path('application/education-info', views.appEduInfo, name='appEduInfo'),    
    path('application/bank-info', views.appBanInfo, name='appBanInfo'),    
    path('application/doc-info', views.appDocInfo, name='appDocInfo'),    
    path('check_username/', views.check_username, name='check_username'),
    path('newuser/',views.newUser,name="newuser")
]


if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)