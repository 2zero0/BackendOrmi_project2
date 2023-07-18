from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    # 글 목록 조회
    path("", views.Index.as_view(), name="list"),
    # 글 상세 조회
    path("detail/<int:pk>/", views.Detail.as_view(), name="detail"),
    # 글 작성
    path("write/", views.Write.as_view(), name="write"),
]