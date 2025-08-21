from django.urls import path

from feed.form import PostForms
from feed.views import HomePageView
from feed.views import PostDetailView
from feed.views import AddPostView

app_name = 'feed'
urlpatterns = [
    path('', HomePageView.as_view(), name='index'),
    path('info/<int:pk>/', PostDetailView.as_view(), name='detail'),
    path('post/', AddPostView.as_view(), name='post'),
]