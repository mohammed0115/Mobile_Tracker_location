from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api import views

urlpatterns = [
    path('user/', views.userList.as_view()),
    path('user/<int:pk>/', views.userDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)