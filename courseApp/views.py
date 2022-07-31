from django.shortcuts import render, redirect, get_object_or_404
from .models import Category, Course, Theme
from .forms import NewUserForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.db.models import Q

def home(request):
    return render(request, "site/home.html")

def courseList(request, slug=None):
    searchCourse = request.GET.get('search')
    if searchCourse:
        cc = Course.objects.filter(Q(courseName__icontains=searchCourse) & Q(courseDescription__icontains=searchCourse))
    else:
        cc = Course.objects.all().order_by("-postDate")

    category = None
    categories = Category.objects.all()
    courses = Course.objects.all().order_by('-postDate')
    if slug:
        category = get_object_or_404(Category, slug=slug)
        courses = courses.filter(category=category)
    return render(request, "site/course-list.html", {
        'cc': cc,
        'category': category,
        'categories': categories,
        'courses': courses
    })

def themeList(request, slug=None):
    course = None
    courses = Course.objects.all()
    themes = Theme.objects.all()
    if slug:
        course = get_object_or_404(Course, slug=slug)
        themes = themes.filter(course=course)
    return render(request, "site/theme-list.html", {
        'course': course,
        'courses': courses,
        'themes': themes,
    })

def themeDetail(request, slug, pk):
    course = get_object_or_404(Course, slug=slug)
    theme = get_object_or_404(Theme, pk=pk)
    themes = Theme.objects.all()
    if slug:
        themes = themes.filter(course=course)
    return render(request, "site/theme-detail.html", {
        'course': course,
        'theme': theme,
        'themes': themes
    })

def signUp(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("home")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    else:
        form = NewUserForm()
    return render(request, "site/sign-up.html", {
        'form': form
    })

def logIn(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("home")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request, "site/log-in.html", {
        'form': form
    })

def logoutUser(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect("home")