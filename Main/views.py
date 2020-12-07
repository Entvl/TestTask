import uuid

from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

# Create your views here.
from .forms import CourseForm
from .models import Course

# функция для проверки заполнености параметров фильтрации
def is_valid_queryparam(param):
    return param != '' and param is not None

def index(request):
    qs = Course.objects.all().order_by('start_date')
    name_query = request.GET.get('name_of_course')
    description_query = request.GET.get('description_of_course')
    start_date_min = request.GET.get('start_date_min')
    start_date_max = request.GET.get('start_date_max')


    if is_valid_queryparam(name_query):
        qs = qs.filter(name__icontains=name_query)

    elif is_valid_queryparam(description_query):
        qs = qs.filter(description__icontains=description_query)

    elif is_valid_queryparam(start_date_min):
        qs = qs.filter(start_date__gte=start_date_min)

    if is_valid_queryparam(start_date_max):
        qs = qs.filter(start_date__lte=start_date_max)

    data = {'data': qs}
    return render(request, "Main/index.html", data)


def my_courses(request):
    if not request.user.id:
        messages.info(request, "You need to login/register in the system")
        return redirect('home')
    qs = Course.objects.filter(user=request.user.id).order_by('start_date')
    data = {'data': qs}
    return render(request, "Main/my_courses.html", data)


def create(request):
    if request.method == "POST":
        form = CourseForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("home")
        else:
            messages.info(request, "Something was wrong, check your data and try again")

    else:
        if not request.user.id:
            messages.info(request, "You need to login/register in the system")
            return redirect("home")
        form = CourseForm()
        form.fields["user"].initial = request.user.id
    context = {
        'form': form
    }
    return render(request, "Main/add_form.html", context)


def read(request, id):
    try:
        course = Course.objects.get(id=id)
        return render(request, "Main/read_course.html", {"element":course})
    except Exception:
        return redirect("home")

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            messages.info(request, "You'r successfully logged in!")
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'Main/signup.html', {'form': form})

def delete(request, id):
    try:
        course = Course.objects.get(id=id)
        course.delete()
        return redirect("my_courses")
    except Exception:
        return redirect("my_courses")

def edit(request, id):
    course = Course.objects.get(id=id)
    if request.method == "POST":
        form = CourseForm(request.POST, request.FILES, instance=course)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect("home")
        else:
            messages.info(request, "Something was wrong, check your data and try again")

    else:
        if not request.user:
            messages.info(request, "You need to login/register in the system")
            return redirect("home")
        form = CourseForm(instance=course)
    context = {
        'form': form,
    }
    return render(request, "Main/add_form.html", context)