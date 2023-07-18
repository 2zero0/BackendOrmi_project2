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
    # 글 삭제
    path("detail/<int:pk>/delete/", views.Delete.as_view(), name="delete"),
    # 글 수정
    path("detail/<int:pk>/edit/", views.Update.as_view(), name="edit"),
    # 글 검색
    path('search/', views.SearchList.as_view(), name='search'),
    # 카테고리별 글 목록
    path("category/<str:category_name>/", views.CategoryPosts.as_view(), name="category_posts"),
]