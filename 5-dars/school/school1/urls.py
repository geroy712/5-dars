from django.urls import path
from .views import home, course

urlpatterns = [
    path('', home, name='home'),
    path('course/<int:course_id>/', course, name='courses'),
    # path('posts/<int:post_id>/', post_detail, name='post_detail'),
]