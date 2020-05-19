# -*- encoding: utf-8 -*-
"""
---------------------------------------
@File        :   forms.py   
@Modify Time :   2020/5/19 11:26           
@Author      :   urchin_lct
@Contact     :   lichangtai17@gmail.com
@Version     :   0.0
---------------------------------------
"""
from django import forms
from django.core.exceptions import ValidationError


class UserRegisterForm(forms.Form):
    username = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True, min_length=6, max_length=30, error_messages={
        'required': '密码必须填写',
        'min_length': '密码必须大于6位',
        'max_length': '密码必须填写',
    })
    password_confirm = forms.CharField(required=True, min_length=6, max_length=30)


