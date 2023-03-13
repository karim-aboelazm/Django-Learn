from django.urls import path
from myapp.views import *

app_name = "myapp"

urlpatterns = [
    # path('',HomePageView.as_view(),name='home'),
    path('',PostsPageView.as_view(),name='home'),
    path('post/<int:pk>/',PostsDetailPageView.as_view(),name='post_details'),
    path('post/add/',PostsAddPageView.as_view(),name='post_add'),
    path('post/<int:pk>/edit',PostsUpdatePageView.as_view(),name='post_edit'),
    path('post/<int:pk>/delete',PostsDeletePageView.as_view(),name='post_delete'),
    path('reply/<str:title>',CommentReplyView.as_view(),name='reply_comment'),
    path('post-react/<int:pk>/',PostReactView.as_view(),name="post_react")

]