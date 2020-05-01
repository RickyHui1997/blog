from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from webblog.models import Post
# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/user')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form}) 


def user_login(request):
    # error_message = ''
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/user')
            # else:
             #    error_message = 'invalid username or password'
        # else:
         #    error_message = 'form invalid'
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})
    # return render(request, 'login.html',{'form': form, 'error_message': error_message})


def user_logout(request):
    logout(request)
    return redirect('/')


def user(request):
    author = request.user
    if request.method == 'POST':
        title = request.POST['title']
        body = request.POST['body']
        post = Post(author=author, title=title, body=body)
        post.save()
        posts = Post.objects.filter(author=author)
    else:
        posts = Post.objects.filter(author=author) 
    return render(request, 'user.html', {'username': request.user.username, 'posts': posts})


def home(request):
    if request.user.is_authenticated:
        print(request.user.username)
    else:
        print("not")
    posts = Post.objects.all()
    return render(request, 'home.html', {'posts': posts, 'user': request.user})



