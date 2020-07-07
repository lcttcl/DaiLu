import time

from django.shortcuts import render, get_object_or_404
from .models import MediumInfo, CategoryInfo, CountryInfo
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
import csv


# Create your views here.

def media_list(request, country_pk=0):
    if country_pk != 0:
        media = MediumInfo.objects.filter(is_deleted=False, country_info_id=country_pk)
    else:
        media = MediumInfo.objects.filter(is_deleted=False)
    countries = CountryInfo.objects.all()
    context = {
        'media': media,
        'countries': countries,
    }
    return render(request, 'index.html', context)


def country_list(request):
    pass


def world_map(request):
    countries = CountryInfo.objects.all()
    # 分页功能
    page_num = request.GET.get('page_num')
    pa = Paginator(countries, 2)
    try:
        pages = pa.page(page_num)
    except PageNotAnInteger:
        pages = pa.page(1)
    except EmptyPage:
        pages = pa.page(pa.num_pages)

    context = {
        'countries': countries,
        'pages': pages,
        'pa': pa,
    }
    return render(request, 'world_map.html', context)


def medium_info(request, medium_pk):
    medium = MediumInfo.objects.get(id=medium_pk)
    medium.add_time = medium.add_time.strftime("%Y-%m-%d")
    medium.update_time = medium.update_time.strftime("%Y-%m-%d")
    context = {
        'medium': medium,
    }
    return render(request, 'medium_info.html', context)
