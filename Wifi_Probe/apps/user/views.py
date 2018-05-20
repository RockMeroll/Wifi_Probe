from django.shortcuts import HttpResponse
from django.db import IntegrityError
from apps.user.models import User
from tools.froms import *
from tools.utils import *
import django.contrib.auth as auth

import re


my_apikey = "195e56cc7e198d5667e5e4bf54cad876"


def home(req):
    return HttpResponse("Index")


def captcha_send(req):
    """
    申请验证码
    """
    if req.method == "POST":
        phone = req.POST.get('phone')
        # 验证手机号格式
        phone_pat = re.compile('^(13\d|14[5|7]|15\d|166|17[3|6|7]|18\d)\d{8}$')
        # print(phone)
        if phone and re.match(phone_pat, phone):
            # 验证用户是否存在
            if User.objects.filter(phone=phone).count() == 0:
                captcha = gene_text()
                req.session['phone'] = phone
                req.session['captcha'] = captcha
                # TODO
                # req.session.set_expiry(1800)
                # return HttpResponse(captcha)
                # msg = "【懂车帝】您的注册验证码是%s，请在30分钟内提交。" % captcha
                # res = json.loads(str(send_yzm(my_apikey, msg, phone), 'utf-8'))
                # return HttpResponse(res)
                return HttpResponse(captcha)
            else:
                return HttpResponse("User %s already exists" % phone)
        else:
            return HttpResponse("Wrong phone number")
    return HttpResponse(status=403)


def captcha_verify(req):
    """
    验证验证码
    """
    if req.method == 'POST':
        captcha = req.POST.get("captcha")
        if captcha:
            if captcha == req.session.get("captcha"):
                req.session['verified'] = True
                return HttpResponse("Verify success")
            else:
                return HttpResponse("Wrong captcha")

    return HttpResponse(status=403)


def register(req):
    """
    注册
    """
    print("############")
    is_verified = req.session.get("verified")
    if req.method == 'POST' and is_verified:
        urf = UserRegisterForm(req.POST)
        if urf.is_valid():
            try:
                user = User(
                    username=urf.cleaned_data['username'],
                    first_name=urf.cleaned_data['first_name'],
                    last_name=urf.cleaned_data['last_name'],
                    email=urf.cleaned_data['email'],
                    phone=urf.cleaned_data['phone'],
                    mac=urf.cleaned_data['mac'],
                    is_teacher=urf.cleaned_data['is_teacher'],
                )
                user.set_password(urf.cleaned_data['password'])
                user.save()
                return HttpResponse("User {0} Register success".format(user.username))
            except IntegrityError as e:
                return HttpResponse("IntegrityError error: {0}".format(e))
        else:
            # TODO
            return HttpResponse(str(urf.cleaned_data))
    return HttpResponse(status=403)


def login(req):
    if req.method == 'POST':
        ulf = UserLoginForm(req.POST)
        if ulf.is_valid():
            user = auth.authenticate(
                username=ulf.cleaned_data['username'],
                password=ulf.cleaned_data['password'],)
            if user is not None:
                auth.login(req, user)
                req.session['user_id'] = user.id
                return HttpResponse("login success")
            else:
                return HttpResponse("用户名或密码错误")
        else:
            # TODO
            return HttpResponse(str(ulf.cleaned_data))
    else:
        return HttpResponse(status=403)


def logout(req):
    auth.logout(req)
    return HttpResponse("logout success")
