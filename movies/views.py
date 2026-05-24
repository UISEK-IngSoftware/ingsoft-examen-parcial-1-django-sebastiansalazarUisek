from django.shortcuts import render
from .models import Movie
# Create your views here.
def index(request):
    movies = Movie.objects.all()
    return render(request, 'index.html', {'movies':movies})

def movie_details(request, id):
    movie = Movie.objects.get(id=id)
    return render(request, 'details.html', {'movie': movie})