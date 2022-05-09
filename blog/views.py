from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post, Category

class PostList(ListView):
    model = Post
    ordering = '-pk'

    def get_context_data(self, **kwargs):
        context = super(PostList, self).get_context_data()
        context['categories'] = Category.objects.all()
        context['no_categories_post_count'] = Post.objects.filter(category=None).count()
        return context

class PostDetail(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super(PostDetail, self).get_context_data()
        context['categories'] = Category.objects.all()
        context['no_categories_post_count'] = Post.objects.filter(category=None).count()
        return context



# 위의 Postlist 과 동일하다
def post_list(request):

    posts = Post.objects.all().order_by('-pk')
    categories = Category.objects.all()
    no_category_post_count = Post.objects.filter(category=None).count()

    return render(
        request,
        'blog/post_list.html',
        {
            'post_list': posts,
            'categories': categories,
            'no_category_post_count': no_category_post_count
        }
    )


# 위의 PostDetail 과 동일하다
def post_detail(request, pk):
   post = Post.objects.get(pk=pk)

   return render(
      request,
       'blog/post_detail.html',
       {
           'post': post,
      }
   )

