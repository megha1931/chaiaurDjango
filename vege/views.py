from .models import *
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages


# Create your views here.
def recipes(request):
    if request.method == 'POST':
        data = request.POST
        recipe_img = request.FILES.get('recipe_img')
        recipe_name = data.get('recipe_name')
        recipe_description = data.get('recipe_description')

        Recipe.objects.create(
            recipe_name=recipe_name,
            recipe_img=recipe_img,
            recipe_description=recipe_description)
        return redirect('/recipes/')
    
    queryset = Recipe.objects.all()
    context = {'recipes': queryset }


    return render(request, 'recipes.html')

def all_recipes(request):
    recipes = Recipe.objects.all()
    return render (request, 'all_recipes.html',{'recipes': recipes })

