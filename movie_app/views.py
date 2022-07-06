from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from . import models, forms


def director_list(request):
    director = models.Director.objects.all()
    return render(request, 'director_list.html', context={'director': director})


def director_detail(request):
    director = get_object_or_404(models.Director, id=id)
    return render(request, 'director_detail.html',
                  {'director': director})


def add_director(request):
    method = request.method
    if method == 'POST':
        form = forms.DirectorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('Director added successfully created')
    else:
        form = forms.DirectorForm()
    return render(request, 'add_director.html', {'form': form})



def movie_list(request):
    movie = models.Movie.objects.all()
    return render(request, 'movie_list.html', context={'movie': movie})


def movie_detail(request):
    movie = get_object_or_404(models.Movie, id=id)
    return render(request, 'movie_detail.html',
                  {'movie': movie})


def add_movie(request):
    method = request.method
    if method == 'POST':
        form = forms.MovieForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('Movie added successfully created')
    else:
        form = forms.MovieForm()
    return render(request, 'add_movie.html', {'form': form})


def review_list(request):
    review = models.Review.objects.all()
    return render(request, 'review_list.html', {'review': review})


def review_detail(request):
    review = get_object_or_404(models.Review, id=id)
    return render(request, 'review_detail.html', {'review': review})


def add_review(request):
    method = request.method
    if method == 'POST':
        form = forms.ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('Review added successfully created')
    else:
        form = forms.ReviewForm()
    return render(request, 'add_review.html', {'form': form})
