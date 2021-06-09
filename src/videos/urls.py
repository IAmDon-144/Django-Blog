from django.urls import path
from videos import views

urlpatterns = [

    path('<pk>/<str:post_title>',views.myvideo,name='single-video'),
    path('allvideos/',views.allVideos,name='my-videos'),
    path('<pk>/editvideo/',views.editVideo,name='edit-videos'),
    path('<pk>/delete-video/confirm',views.deleteVdo,name='delete-videos'),
    
    
    ]