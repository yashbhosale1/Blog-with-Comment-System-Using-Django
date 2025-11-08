from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    path('post/new/', views.post_create, name='post_create'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('post/<int:pk>/delete/', views.post_delete, name='post_delete'),

    path('comment/<int:post_id>/', views.add_comment, name='add_comment'),

    # REST APIs
    path('api/posts/', views.PostListAPI.as_view(), name='post_list_api'),
    path('api/comments/', views.CommentListAPI.as_view(), name='comment_list_api'),
]
