from django.db import models

# 게시글 테이블
class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    # writer = models.ForeignKey(User, on_delete=models.CASCADE)
    writer = models.CharField(max_length=10)
    category = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # def formatted_created_at(self):
    #     return self.created_at.strftime("%Y-%m-%d | %p %H:%M")
