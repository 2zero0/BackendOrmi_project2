from django.shortcuts import render
from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from .forms import RegisterForm, LoginForm, ProfileEditForm
from django.contrib.auth import authenticate, login, logout
from .models import User
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash

### 회원가입
class Registration(View):
    # 회원가입 정보 입력받음
    def get(self, request):
        # if request.user.is_authenticated:
        #     return redirect('blog:list')
        
        # 회원가입 페이지
        # => 정보를 입력할 폼을 보여줘야함
        form = RegisterForm()
        context = {"form": form}
        return render(request, "user/user_register.html", context)

    # 제출 눌렀을 때 동작
    def post(self, request):
        # 요청 넣은 채로 폼 만듦
        form = RegisterForm(request.POST)
        if form.is_valid():
            # user모델 사용, form의 내용 저장
            user = form.save()
            # 로그인한 다음 이동
            return redirect("user:login")


### 로그인
class Login(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect("blog:list")

        form = LoginForm()
        context = {"form": form}
        return render(request, "user/user_login.html", context)

    def post(self, request):
        if request.user.is_authenticated:
            return redirect("blog:list")

        form = LoginForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            # boolean값으로 True/False로 반환
            user = authenticate(username=username, password=password)

            if user:
                login(request, user)
                return redirect("blog:list")

        form.add_error(None, "아이디가 없습니다.")

        # 에러가 들어있는 폼
        context = {"form": form}
        return render(request, "user/user_login.html", context)


### 로그아웃
class Logout(View):
    # 이미 로그인이 된 상태이므로 원래 유저가 정해져 있음
    def get(self, request):
        logout(request)
        return redirect("blog:list")
    

### 프로필 수정
class ProfileEdit(View):
    def get(self, request, username):
        user = get_object_or_404(User, username=username)
        form = ProfileEditForm(instance=user)
        # 수정한거
        password_change_form = PasswordChangeForm(user=request.user)
        context = {
            'user': user,
            'form': form,
            'password_change_form': password_change_form
        }
        return render(request, 'user/user_profile_edit.html', context)

    def post(self, request, username):
        user = get_object_or_404(User, username=username)
        form = ProfileEditForm(request.POST, instance=user)
        password_change_form = PasswordChangeForm(user=user, data=request.POST)

        if form.is_valid() and password_change_form.is_valid():
        # if form.is_valid():
            print(form.cleaned_data)
            form.save()
            # user.nickname = form.cleaned_data['nickname']
            print('view확인 ', user.nickname)
            # user.save()
            print('view-save후 확인 ', user.nickname)
            # print(User.objects.get(username=username).nickname)
            password_change_form.save()  # 수정
            # update_session_auth_hash(request, user)  # 수정
            user.refresh_from_db()
            login(request, user)
            print('Nickname after saving:', user.nickname)
            return redirect('blog:list')
        
        context = {
            'user': user,
            'form': form,
            'password_change_form': password_change_form
        }
        return render(request, 'user/user_profile_edit.html', context)