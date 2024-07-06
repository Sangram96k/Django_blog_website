from django.http import JsonResponse
from django.shortcuts import render,redirect,get_object_or_404,redirect
from .models import Post, Comment
from .forms import CommentForm
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def BASE(request):
    return render(request, 'main/base.html')
# Create your views here.
def INDEX(request):
    post=Post.objects.filter(section='Popular').order_by('-id')[:4]
    all_post=Post.objects.all()
    paginator = Paginator(all_post, 6)
    print(request.GET)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    context = {'post':post,
              'all_post':posts,
              'paginator': paginator
               
               
               
               }
    return render(request, 'main/index.html',context)
   

def POST_DETAIL(request,slug):
    post = get_object_or_404(Post, slug=slug)
    related_posts = Post.objects.filter(cat=post.cat).exclude(slug=post.slug)[:4]
    comments = post.comments.filter(active=True)  # Filter active comments
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', slug=post.slug)
    else:
        form = CommentForm()
    context = {'post':post,
               'comments': comments, 
               'form': form,
               'related_posts': related_posts
               
               
               
               
               }
    return render(request, 'main/post_detail.html',context)
   




def search_view(request):
    query = request.GET.get('search')
    if query:
        results = Post.objects.filter(
            Q(title__icontains=query) | 
            Q(content__icontains=query)
        )
    else:
        results = Post.objects.none()

    return render(request, 'main/results.html', {'results': results, 'query': query})

# def autocomplete_search(request):
#     if 'term' in request.GET:
#         query = request.GET.get('term')
#         search_results = Post.objects.filter(
#             Q(title__icontains=query) | 
#             Q(content__icontains=query)
#         )
#         suggestions = list(search_results.values('title'))
#         return JsonResponse(suggestions, safe=False)
#     return JsonResponse([], safe=False)


# def autocomplete_search(request):
#     if 'term' in request.GET:
#         query = request.GET.get('term')
#         search_results = Post.objects.filter(
#             Q(title__icontains=query) | 
#             Q(content__icontains=query)
#         )
#         suggestions = list(search_results.values('title', 'slug'))
#         return JsonResponse(suggestions, safe=False)
#     return JsonResponse([], safe=False)
def autocomplete_search(request):
    if 'term' in request.GET:
        query = request.GET.get('term')
        search_results = Post.objects.filter(
            Q(title__icontains=query) | 
            Q(content__icontains=query)
        )
        suggestions = list(search_results.values('title', 'slug'))
        return JsonResponse(suggestions, safe=False)
    return JsonResponse([], safe=False)





def BLOG(request):
    posts = Post.objects.all().order_by('-id')
    paginator = Paginator(posts, 6)
    print(request.GET)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    context = {'posts':posts,
              'all_post':posts,
              'paginator': paginator
               
               
               
               }
    return render(request, 'main/Blog.html', context)
    