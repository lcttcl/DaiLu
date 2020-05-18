from django.db import models
from datetime import datetime
from users.models import UserProfile
from mediums.models import MediumInfo


# Create your models here.

class UserLove(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name="收藏用户", on_delete=models.DO_NOTHING, null=True)
    love_id = models.IntegerField(verbose_name="收藏id")
    love_type = models.IntegerField(choices=((1, 'medium'), (2, 'country')), verbose_name="收藏类别")
    love_status = models.BooleanField(default=False, verbose_name="收藏状态")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = '收藏信息'
        verbose_name_plural = verbose_name


class UserComment(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name="评论用户", on_delete=models.DO_NOTHING, null=True)
    comment_course = models.ForeignKey(MediumInfo, verbose_name="评论媒体 ", on_delete=models.DO_NOTHING, null=True)
    comment_content = models.TextField(verbose_name="评论内容")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    def __str__(self):
        return self.comment_content

    class Meta:
        verbose_name = '用户评论课程信息'
        verbose_name_plural = verbose_name
