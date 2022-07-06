
from django.contrib import admin
from django.urls import path
from movie_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('director/', views.director_list, name='director_all'),
    path('director/<int:id>/', views.director_list, name='director_all'),
    path('movies/', views.movie_list, name='movies_all'),
    path('movies/<int:id>/', views.movie_detail, name='movies_all'),
    path('review/', views.review_list, name='review_all'),
    path('review/<int:id>/', views.review_detail, name='review_all'),

]



