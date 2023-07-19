from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# 게시글 테이블
class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    # writer = models.CharField(max_length=10)
    category = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    hit = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to = "images/", null=True, blank=True)

    # 조회수 증가 함수
    def increase_hit(self):
        self.hit += 1
        self.save(update_fields=['hit'])
