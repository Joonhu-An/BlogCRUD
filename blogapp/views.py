from django.shortcuts import render, get_object_or_404, redirect
from .models import Blogapp
from django.utils import timezone

def main(request):
    blog_all = Blogapp.objects.all().order_by('-id')
    return render(request, 'main.html', {'blogs':blog_all})

def detail(request, blog_id):
    blog = get_object_or_404(Blogapp, pk=blog_id)
    return render(request,'detail.html',{'blog':blog})

# new 화면 띄우기
def new(request):
    return render(request,'new.html')

def create(request):
    blog=Blogapp()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()
    return redirect('/detail/' + str(blog.id))

    # 앞에 / 는 절대 경로 기존에 있던 URL이 다 날아가고 가장 처음 아무것도 없는 URL로 돌아간다.

def renew(request, blog_id):
    blog_r = get_object_or_404(Blogapp, pk=blog_id)
    return render(request,'renew.html',{'blog':blog_r})

def update(request, blog_id):
    blog= get_object_or_404(Blogapp,pk=blog_id)
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()
    return redirect('/detail/' + str(blog.id))

def delete(request, blog_id):
    blog_d = get_object_or_404(Blogapp, pk=blog_id)
    blog_d.delete()
    return redirect('main')


