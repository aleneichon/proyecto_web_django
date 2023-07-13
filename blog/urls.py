from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
<<<<<<< HEAD
=======
    path('login/',views.login_view,name='login'),
>>>>>>> 2a24358cbeed6e98fb07b4dac7b4b79ad29addf3

]

