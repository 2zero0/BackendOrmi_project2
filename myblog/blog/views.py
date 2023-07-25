from django.shortcuts import render, redirect
from django.views import View
from .models import Post, Comment, ImageUpload
from .forms import PostForm, CommentForm
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

### 게시글 조회
class Index(View):
    def get(self, request):
        post_objs = Post.objects.all().order_by('-created_at')
        form = PostForm()
        
        context = {
            "posts": post_objs,
            "form": form
            }
        
        return render(request, "blog/post_list.html", context)


### 게시글 상세
class Detail(View):
    def get(self, request, pk):
        try:
            post = Post.objects.get(pk=pk)
        except:
            return render(request,'blog/post_detail_error.html')
        
        comments = Comment.objects.filter(post=post)
        comment_form = CommentForm()

        # 조회수 증가
        post.increase_hit()
        context = {
            "post": post,
            "comments": comments,
            "comment_form": comment_form,
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
        form = PostForm(instance=post)
        context = {
            'form': form,
            'post': post
        }
        return render(request, 'blog/post_edit.html', context)
    
    def post(self, request, pk):
        post = Post.objects.get(pk=pk)
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            # post.title = form.cleaned_data['title']
            # post.content = form.cleaned_data['content']
            # post.save()
            form.save()
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
        ).order_by('-created_at')
        context = {
            'search_query': search_query,
            'posts': posts
        }
        return render(request, 'blog/post_list.html', context)
    

### 카테고리별 게시글 목록
class CategoryPosts(View):
    def get(self, request, category_name):
        posts = Post.objects.filter(category=category_name).order_by('-created_at')
        form = PostForm()
        context = {
            'category_name': category_name,
            'posts': posts,
            'form': form
        }
        return render(request, 'blog/post_list.html', context)
    

### 이미지 업로드 (toast ui)
class ImgUpload(View):
    def post(self, request):
        image = request.FILES['image']
        imageUpload = ImageUpload.objects.create(image=image)
        url = imageUpload.image
        data = {
            'url': str(url)
        }
        return JsonResponse(data)

### 댓글 작성
class CommentWrite(View):
    def post(self, request, pk):
        form = CommentForm(request.POST)
        # 해당 아이디에 해당하는 글 불러옴(댓글은 어떤 한 글의 댓글이므로)
        post = Post.objects.get(pk=pk)
        
        if form.is_valid():
            # 사용자에게 댓글 내용 받아옴
            content = form.cleaned_data["content"]
            
            # 유저 정보 가져오기
            writer = request.user
            # 댓글 객체 생성
            comment = Comment.objects.create(post=post, content=content, writer=writer)
            return redirect("blog:detail", pk=pk)
        
        form.add_error(None, '폼이 유효하지 않습니다.')
        context = {
            'post': post,
            'comment_form': form,
            'comments': post.comment_set.all(),
        }
        return render(request, 'blog/post_detail.html', context)


### 댓글 삭제
class CommentDelete(View):
    def post(self, request, pk):
        comment = Comment.objects.get(pk=pk)
        post_id = comment.post.id
        comment.delete()

        return redirect("blog:detail", pk=post_id)