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
