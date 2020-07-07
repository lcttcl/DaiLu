from django.db import models
from datetime import datetime


# Create your models here.
class CountryInfo(models.Model):
    name = models.CharField(max_length=20, verbose_name="国家名称")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")
    continent = models.CharField(
        choices=(('Asia', '亚洲'), ('Africa', '非洲'), ('Europe', '欧洲'), ('Oceania', '大洋洲'), ('America', '美洲')),
        verbose_name="所处大洲", max_length=20)
    love_num = models.IntegerField(default=0, verbose_name="收藏数")
    click_num = models.IntegerField(default=0, verbose_name="点击数")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '国家信息'
        verbose_name_plural = verbose_name


class LanguageInfo(models.Model):
    name = models.CharField(max_length=20, verbose_name="语种名称")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '语种信息'
        verbose_name_plural = verbose_name


class CategoryInfo(models.Model):
    name = models.CharField(max_length=20, verbose_name="媒体类型名称")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '媒体类型信息'
        verbose_name_plural = verbose_name


class MediumInfo(models.Model):
    logo_image = models.ImageField(upload_to='medium/', max_length=200, verbose_name="媒体徽标")
    chn_name = models.CharField(max_length=30, verbose_name="媒体中文名称")
    en_name = models.CharField(max_length=50, verbose_name="媒体英文名称")
    url = models.URLField(default='http://lichangtai.cn', max_length=200, verbose_name="媒体链接")
    desc = models.TextField(verbose_name="媒体简介")
    detail = models.TextField(verbose_name="媒体详情")
    love_num = models.IntegerField(default=0, verbose_name="收藏数")
    click_num = models.IntegerField(default=0, verbose_name="点击数")
    country_info = models.ForeignKey(CountryInfo, null=True, on_delete=models.DO_NOTHING, verbose_name="所属国家")
    language_info = models.ForeignKey(LanguageInfo, null=True, on_delete=models.DO_NOTHING, verbose_name="语种")
    category_info = models.ForeignKey(CategoryInfo, null=True, on_delete=models.DO_NOTHING, verbose_name="所属类别")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")
    update_time = models.DateTimeField(auto_now=True, verbose_name="更新时间")
    is_deleted = models.BooleanField(default=False, verbose_name="删除状态")

    def __str__(self):
        return self.chn_name

    class Meta:
        verbose_name = '媒体信息'
        verbose_name_plural = verbose_name
