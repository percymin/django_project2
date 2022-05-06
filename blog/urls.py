from django.urls import path
from . import views

urlpatterns = [
    path('', views.Postlist.as_view()),
    # path('', views.post_list),
    path('<int:pk>/', views.PostDetail.as_view()),
    # path('<int:pk>/', views.post_detail),
    # path('<int:pk>/', views.single_post_page),

]
