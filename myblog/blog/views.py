from django.shortcuts import render, redirect
from django.views import View
from .models import Post
from .forms import PostForm

### 게시글 조회
class Index(View):
    def get(self, request):
        post_objs = Post.objects.all()
        
        context = {"posts": post_objs}
        
        return render(request, "blog/post_list.html", context)


### 게시글 상세
class Detail(View):
    def get(self, request, pk):
        # 해당 글
        post = Post.objects.get(pk=pk)

        context = {
            "post": post
        }

        return render(request, 'blog/post_detail.html', context)


### 게시글 작성
class Write(View):
    def get(self, request): # 글 작성 폼 출력

        form = PostForm()
        context = { 
            'form': form
        }
        return render(request, 'blog/post_write.html', context)
    
    def post(self, request): # submit시 동작(작성 폼 저장)
        form = PostForm(request. POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.writer=request.user
            post.save()
            return redirect('blog:list')
        form.add_error(None, '폼이 유효하지 않습니다.')
        context = {
            'form': form
        }
        return render(request, 'blog/post_write.html')
    

### 게시글 삭제
class Delete(View):
    def post(self, requst, pk):
        post = Post.objects.get(pk=pk)
        post.delete()
        return redirect('blog:list')