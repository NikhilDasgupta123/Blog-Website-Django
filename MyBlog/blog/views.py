from django.shortcuts import render
from blog.models import Post, Category
# Create your views here.
def home(request):
    posts=Post.objects.all()[:11]
    print(posts)
    
    cats=Category.objects.all()

    data={
        'posts':posts,
        'cats':cats
    }
    return render(request,'home.html',data)

def post(request,url):
    post=Post.objects.get(url=url)
    return render(request,'posts.html',{'post':post})
