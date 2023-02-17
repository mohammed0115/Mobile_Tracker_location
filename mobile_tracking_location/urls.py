"""mobile_tracking_location URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
admin.site.site_header = 'Mobile tracker using GPs'
from account.views import Welcome,First,Second,third,fourth
urlpatterns = [
    path('admin/', admin.site.urls),
    path("markers/api/", include("markers.api")),
    path("markers/", include("markers.urls")),
    path("api/", include("api.urls")),
    path('',Welcome,name="welcome"),
    path('first/',First,name="First"),
    path('second/',Second,name="second"),
    path('third/',third,name="third"),
    path('fourth/',fourth,name="fourth"),
    #
]
