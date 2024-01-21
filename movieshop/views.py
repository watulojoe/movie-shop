from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import Movie, Genre, Season, Episode
from . import myScraper
from .myScraper import var


# Create your views here.
def home(request):
    allSeries = Movie.objects.all()
    context = {"allSeries": allSeries}
    return render(request, "home.html", context)


def tv_series_list(request):
    allSeries = Movie.objects.all()
    context = {"allSeries": allSeries}
    return render(request, "tv_series_list.html", context)


def genre_list(request):
    return render(request, "genre_list.html")


def movie_detail(request, pk):
    series = get_object_or_404(Movie, pk=pk)
    genres = series.genre.all()
    context = {"series": series, "genres": genres}
    return render(request, "details.html", context)


# def scrape(req):
#     # add all the movies
#     for i in data:
#         movie = Movie.objects.create(
#             title=i["title"],
#             img=i["img"],
#             about=i["about"],
#             runtime=i["runtime"],
#             seasons=i["seasons"],
#             movie_url=i["url"],
#         )
#         print(movie)
#         for j in i["genre"]:
#             genre_query = Genre.objects.filter(title=j)
#             if len(genre_query) > 0:
#                 movie.genre.add(genre_query[0])
#             else:
#                 obj = Genre.objects.create(title=j)
#                 movie.genre.add(obj)
#
#     return HttpResponse("hi")

# def populate(request):
#     for movie in var.items():
#         # print(movie[0])  # movie title
#         movie_obj = Movie(title=movie[0])
#         movie_obj.save()
#         for sn in movie[1].items():
#             # print(sn[0])  # season title
#             sn_obj = Season(title=sn[0], movie=movie_obj)
#             sn_obj.save()
#             for ep in sn[1].items():
#                 print(f'{ep[0]} - {ep[1]}')  # ep and link
#                 ep_obj = Episode(title=ep[0], movie_url=ep[1], season=sn_obj)
#                 ep_obj.save()
#     return HttpResponse("hi")
