from django.urls import path
from matchingapp import views
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('',views.mypage, name='mypage')
]