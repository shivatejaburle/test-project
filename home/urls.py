from django.urls import path, include
from home import views

app_name = 'home'

urlpatterns = [
    path('', views.IndexPage.as_view(), name = 'index')
]
