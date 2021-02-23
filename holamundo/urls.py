from django.urls import path 
from holamundo import views as local_views
from posts import views as posts_views

urlpatterns = [
    path('hello-world/', local_views.hello_world),
    path('hi/', local_views.hi),

    path('posts/', posts_views.list_posts),
]
