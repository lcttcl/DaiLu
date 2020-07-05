from django.shortcuts import render, get_object_or_404
from .models import MediumInfo, CategoryInfo, CountryInfo


# Create your views here.

def media_list(request):
    media = MediumInfo.objects.filter(is_deleted=False)
    countries = CountryInfo.objects.all()
    context = {'media': media,
               'countries': countries,
               }
    return render(request, 'index.html', context)


def world_map(request):
    return render(request, 'world_map.html')


def medium_info(request, medium_pk):
    medium = MediumInfo.objects.get(id=medium_pk)
    context = {
        'medium': medium,
    }
    return render(request, 'medium_info.html', context)
