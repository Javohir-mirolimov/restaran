from django.shortcuts import render
from .models import *



def index_view(request):
    context={
        'banner': Banner.objects.all().order_by('-id')[:3],
        'about_us': About_Us.objects.all().order_by('-id')[:2],
        'meal': Meal.objects.all().order_by('-id')[:3],
        'awards': Award.objects.all().order_by('-id')[:5],
        'testimonials': Testimonial.objects.all().order_by('-id')[:3],
        'info': Info.objects.last()
    }
    return render(request, 'index.html', context)
