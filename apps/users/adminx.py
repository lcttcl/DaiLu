# -*- encoding: utf-8 -*-
"""
---------------------------------------
@File        :   adminx.py   
@Modify Time :   2020/5/17 15:13           
@Author      :   urchin_lct
@Contact     :   lichangtai17@gmail.com
@Version     :   0.0
---------------------------------------
"""
import xadmin
from .models import BannerInfo, EmailVerifyCode
from xadmin import views  # 配置Xadmin主题


class BaseXadminSetting(object):
    enable_themes = True
    use_bootswatch = True


class CommXadminSetting(object):
    site_title = '带路媒体后台管理系统'
    site_footer = 'cq & lct'
    menu_style = 'accordion'


class BannerInfoXadmin(object):
    list_display = ['image', 'url', 'add_time']
    search_fields = ['image', 'url']
    list_filter = ['image', 'url']


class EmailVerifyCodeXadmin(object):
    list_display = ['code', 'email', 'send_type', 'add_time']


xadmin.site.register(BannerInfo, BannerInfoXadmin)
xadmin.site.register(EmailVerifyCode, EmailVerifyCodeXadmin)
xadmin.site.register(views.BaseAdminView, BaseXadminSetting)  # 注册主题类
xadmin.site.register(views.CommAdminView, CommXadminSetting)  # 注册全局样式类
