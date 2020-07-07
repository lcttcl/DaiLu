# -*- encoding: utf-8 -*-
"""
---------------------------------------
@File        :   adminx.py   
@Modify Time :   2020/5/17 15:22           
@Author      :   urchin_lct
@Contact     :   lichangtai17@gmail.com
@Version     :   0.0
---------------------------------------
"""
import xadmin
from .models import CountryInfo, LanguageInfo, CategoryInfo, MediumInfo


class CountryInfoXadmin(object):
    list_display = ['name', 'continent', 'love_num', 'love_num', 'click_num', 'add_time']


class LanguageInfoXadmin(object):
    list_display = ['name']


class CategoryInfoXadmin(object):
    list_display = ['name']


class MediumInfoXadmin(object):
    list_display = ['logo_image', 'chn_name', 'en_name', 'url', 'desc', 'detail', 'love_num', 'click_num',
                    'country_info', 'language_info', 'category_info', 'add_time', 'update_time']


xadmin.site.register(CountryInfo, CountryInfoXadmin)
xadmin.site.register(LanguageInfo, LanguageInfoXadmin)
xadmin.site.register(CategoryInfo, CategoryInfoXadmin)
xadmin.site.register(MediumInfo, MediumInfoXadmin)
