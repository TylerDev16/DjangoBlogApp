from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostList.as_view(), name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.post_detail, name='post_detail')
]