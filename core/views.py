from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.views import View
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.views.generic import CreateView
from django.views import View
from core.models import User
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView

def index(request):
    return render(request, 'match/index.html')

class IndexView(TemplateView):
    template_name = 'index.html'

def mypage (request):
    return render(request, 'match/mypage.html')

class MypageView(TemplateView) :
    template_name = 'mypage.html'

def register (request):
    return render(request, 'match/register.html')


class AccountCreateView(View):
    def get(self, request):
        return render(request, "match/register.html")

    # post を追加
    def post(self, request):
        # ユーザー情報を保存する
        User.objects.create_user(
            username=request.POST["username"],
            email=request.POST["email"],
            password=request.POST["password"],
        )
        # 登録完了画面を表示する
        return render(request, "match/register_success.html")
    



class AccountLoginView(LoginView):
    """ログインページのテンプレート"""
    template_name = 'match/login.html'

    def get_default_redirect_url(self):
        """ログインに成功した時に飛ばされるURL"""
        return "/mypage"
    

class AccountLogoutView(LogoutView):
    template_name = 'match/logout.html'

    def get_default_redirect_url(self):
        """ログアウトに成功した時に飛ばされるURL"""
        return "/"