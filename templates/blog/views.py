from django.shortcuts import render

# Create your views here.
from .models import Blog
def allblogs(request):
    Blog_var= Blog.ojects
    return render(request,'blog/allblogs.html',{'blog_html':blogs_var})
    def detail(request,blog_id):
        detailblog=get_object_or_404(Blog,pk=blog_id)
        return render(request,'blog/detail.html',{'blog_detail': detailblog})
