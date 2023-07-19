from django.shortcuts import render, redirect
from django.views import View
from .models import Post
from .forms import PostForm
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin

### 게시글 조회
class Index(View):
    def get(self, request):
        post_objs = Post.objects.all()
        form = PostForm()
        
        context = {
            "posts": post_objs,
            "form": form
            }
        
        return render(request, "blog/post_list.html", context)


### 게시글 상세
class Detail(View):
    def get(self, request, pk):
        # 해당 글
        post = Post.objects.get(pk=pk)
        post.increase_hit()
        context = {
            "post": post
        }

        return render(request, 'blog/post_detail.html', context)


### 게시글 작성
class Write(LoginRequiredMixin, View):
    def get(self, request): # 글 작성 폼 출력

        form = PostForm()
        context = { 
            'form': form
        }
        return render(request, 'blog/post_write.html', context)
    
    def post(self, request): # submit시 동작(작성 폼 저장)
        form = PostForm(request.POST, request.FILES)
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

### 게시글 수정
class Update(View):
    def get(self, request, pk): # post_id
        post = Post.objects.get(pk=pk)
        # 양식이 이미 정해진 경우 initial
        form = PostForm(initial={'title': post.title, 'content': post.content})
        context = {
            'form': form,
            'post': post
        }
        return render(request, 'blog/post_edit.html', context)
    
    def post(self, request, pk):
        post = Post.objects.get(pk=pk)
        form = PostForm(request.POST)
        if form.is_valid():
            post.title = form.cleaned_data['title']
            post.content = form.cleaned_data['content']
            post.save()
            return redirect('blog:detail', pk=pk)
        
        form.add_error('폼이 유효하지 않습니다.')
        context = {
            'form': form
        }
        return render(request, 'blog/post_edit.html', context)
    

### 게시글 검색
class SearchList(View):
    def get(self, request):
        search_query = request.GET.get('search', '')
        posts = Post.objects.filter(
            Q(title__icontains=search_query) | Q(content__icontains=search_query)
        )
        context = {
            'search_query': search_query,
            'posts': posts
        }
        return render(request, 'blog/post_list.html', context)
    

### 카테고리별 게시글 목록
class CategoryPosts(View):
    def get(self, request, category_name):
        posts = Post.objects.filter(category=category_name)
        form = PostForm()
        context = {
            'category_name': category_name,
            'posts': posts,
            'form': form
        }
        return render(request, 'blog/post_list.html', context)