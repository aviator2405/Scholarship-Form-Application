from django.urls import path,include
from api import views
urlpatterns = [
    path('formfilled/', views.formFilled),
    path('users/<int:userID>/', views.userDetails),
    path('users/hodapproved/', views.hodapproved),
    path('users/priapproved/', views.principalapproved),
    path('users/hodrejected/', views.hodrejected),
    path('users/prirejected/', views.principalrejected),
    path('users/approvedByHOD/', views.ApprovedByHOD),
    path('users/approvedByPRI/', views.ApprovedByPRI),
    path('users/deleteFormHOD/<int:userID>/', views.delete_user_form_HOD),
    path('users/deleteFormPRI/<int:userID>/', views.delete_user_form_PRI),
    path('users/getFormPerInfo/<int:userID>/', views.getPerInfo),

]
