from django.urls import path, include
from posts import views

app_name = 'posts'

urlpatterns = [
    path('', views.PostList.as_view(), name = 'all_posts'),
    path('create/', views.CreatePost.as_view(), name = 'create_post')
]
