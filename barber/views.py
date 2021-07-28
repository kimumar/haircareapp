from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Setting, BookingMessage, BookingForm, CommentMessage, CommentForm, Post, PostForm

# Create your views here.
def index(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Thanks for booking with us.")
            return redirect('/')
    
    setting = Setting.objects.get(pk=1)
    form = BookingForm

    context = {
        'form': form,
        'setting': setting,
    }

    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html')



def blog(request):
    posts = Post.objects.all()
    setting = Setting.objects.get(pk=1)

    context = {
        'posts':posts,
        'setting': setting,
    }

    return render(request, 'blog.html', context)


def blogs(request, pk):
    post = Post.objects.get(id=pk)
    comments = CommentMessage.objects.all()
    setting = Setting.objects.get(pk=1)

    comment = CommentForm()
    if request.method == 'POST':
        comment = CommentForm(request.POST)
        if comment.is_valid():
            comment.save()
        
    


    context = {
        'post':post,
        'comments':comments,
        'comment':comment,
        'setting': setting,
    }

    return render(request, 'blog-single.html', context)


def create(request):
    post = PostForm()
    if request.method == 'POST':
        post = PostForm(request.POST)
        if post.is_valid():
            post.save()
        return redirect('/blog')

    context = {
        'post':post,
    }
    return render(request, 'create.html', context)



def update(request, pk):

    blog = Post.objects.get(id=pk)
    post = PostForm(instance=blog)

    if request.method == 'POST':
        post = PostForm(request.POST, instance=blog)
        if post.is_valid():
            post.save
        return redirect('/blog')


    

    context = {
        'post':post,
        
    }
    return render(request, 'create.html', context)

def updates(request, pk):
    
    blogs = CommentMessage.objects.get(id=pk)
    comment = CommentForm(instance=blogs)

    if request.method == 'POST':
        comment = CommentForm(request.POST, instance=blogs)
        if comment.is_valid():
           comment.save
        

    context = {
        'comment':comment,
        
    }
    return render(request, 'comment-update.html', context)

def deleteco(request, pk):
    comment = CommentMessage.objects.get(id=pk)

    if request.method == "POST":
        comment.delete()
        return redirect('/blog-single')

    context = {
        'comment':comment,
    }


    return render(request, 'comment-delete.html', context)


def delete(request, pk):
    post = Post.objects.get(id=pk)

    if request.method == "POST":
        post.delete()
        return redirect('/blog')


    context = {
        'post':post,
    }

    return render(request, 'confirm_delete.html', context)



def gallery(request):
    setting = Setting.objects.get(pk=1)

    context = {
        'setting':setting,
    }
    return render(request, 'gallery.html', context)

def services(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Thanks for booking with us.")
            return redirect('/services')
    
    form = BookingForm

    context = {
        'form': form,
    }
    return render(request, 'services.html', context)



