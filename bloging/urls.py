from django.urls import path
from . import views

urlpatterns = [
    path('',views.postListView.as_view(),name="blog_home"),
    path('about/',views.about,name="blog_about"),
    #path('post/<int:ss>/',views.detatil,name="post-detail"),
    #py convention details name the value it expected pk
    path('post/<int:pk>/',views.postDetailView.as_view(),name="post-detail"),
    path('post/new/',views.postCreateView.as_view(),name="post-create"),
    path('post/<int:pk>/update/',views.postUpdateView.as_view(),name="post-Update"),
    path('post/<int:pk>/delete/',views.postDeleteView.as_view(),name="post-delete"),
    path('user/<str:username>/',views.UserpostListView.as_view(),name="user-posts"),

]
