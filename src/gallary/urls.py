from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from gallary import views



urlpatterns = [
    
    path('',views.newsFeed,name = 'newsfeed'),
    path('<pk>',views.newsFeed2,name = 'newsfeed2'),
    path('like-unlike/',views.like_unlike_post,name = 'like-unlike-post'),
    path('save_post/',views.save_post,name = 'save-post'),
    path('save-category/',views.save_category,name = 'save-category'),
    path('delete_post/<pk>',views.delete_post,name = 'delete-post'),

    path('update_post/<str:pk>',views.update_post,name = 'update-post'),
    path('delete_comment/',views.delete_comment,name = 'delete-comment'),
    

    path('<pk>/<str:title>',views.catagory_wise_filter,name = 'catagory-post'),


    path('<pk>/<str:post_title>/comment_post/',views.save_comments,name = 'save-comment'),


    path('<pk>/<post_title>/continue-reading/',views.ContinueReading,name = 'post-reading'),
    path('<pk>/<post_title>/<str:lang_name>/translated_by_google',views.ContinueReadingTranslate,name='post-translate'),
    
    path('allposts/',views.allposts,name='all-post'),
    path('about-page/',views.about,name='about'),
    path('terms-and-conditions/',views.termsAndConditions,name='terms-and-condition'),
    path('adminandusers/',views.admins,name='admin-and-users'),


]
