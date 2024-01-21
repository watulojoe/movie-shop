from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),

    path("tv_series_list", views.tv_series_list, name="tv_series_list"),

    path("genre_list", views.genre_list, name="genre_list"),

    path("movie_detail/<int:pk>", views.movie_detail, name="movie_detail"),

    path("movie_detail/<int:m_pk>/<int:pk>", views.movie_detail, name="movie_detail"),

    # path("populate", views.populate, name="populate")
    # path('scrape', views.scrape),
]
