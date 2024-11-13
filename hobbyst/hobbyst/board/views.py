from django.shortcuts import render, redirect
# from board.forms import CommentForm, PostForm
from board.models import Post
# from django.views.decorators.http import require_POST


# Create your views here.

def home(request):
    # if not request.user.is_authenticated:
        # return redirect('/account/login')
    posts = Post.objects.all()
    # comment_form = CommentForm()
    context = {
        'board': posts                                              # board로 template에 전달해야함
        # 'comment_form': comment_form,
    }
    return render(request, 'board/home.html',context)

# def post_write(request):
#     if request.method == "POST":
#         form = PostForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#     else:
#         form = PostForm()
#     context = {'form':form}
#     return render(request, "board/post_write.html", context)

#교재 p.263 post요청만 처리하는 부분 수정
# @require_POST  
# def comment_add(request):
#     form = CommentForm(request.POST)
#     if form.is_valid():
#         # 'post' 필드를 hidden input에서 가져옴
#         post_id = request.POST.get('post')
#         post = Post.objects.get(id=post_id)
#         # Comment 객체를 생성하지만 아직 저장하지 않음 (commit=False)
#         comment = form.save(commit=False)
#         comment.post = post
#         comment.user = request.user  # 현재 로그인한 사용자를 댓글 작성자로 설정
#         comment.save()
#         return redirect('home')
#     return redirect('home')