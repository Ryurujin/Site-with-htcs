from django.urls import path, include 
from .views import *

urlpatterns = [
    #user
    path('user/', User_views_list.as_view()),
    path('user/<int:pk>/', User_views_detail.as_view()),

    #post
    path('post/', Post_views_list.as_view()),
    path('post/<int:pk>/', Post_views_detail.as_view),

    path('auth/', include('dj_rest_auth.urls')),

]