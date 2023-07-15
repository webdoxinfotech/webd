from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import get_object_or_404

# Create your views here.
from courses.models import *

def home(request):
    subjects = Subject.objects.all()
    courses = Course.objects.all()
    simple = map(lambda course: course.name.lower().replace("in jalandhar", "").title(), courses)
    reviews = Reviews.objects.filter(active=True)
    return render(request, "index.html", {'subjects': subjects, 'courses': courses, 'simple': simple, 'reviews': reviews})


def about(request):
    reviews = Reviews.objects.filter(active=True)
    return render(request, "about.html", {'reviews': reviews})


def course(request):
    courses = Course.objects.all()
    subjects = Subject.objects.all()
    return render(request, "course.html", {'courses': courses, 'subjects': subjects})


def blog(request):
    return render(request, "blog.html")


def contact(request):
    return render(request, "contact.html")


def single_course(request, slug):
    course = get_object_or_404(Course, slug=slug)
    subjects = Subject.objects.all()
    recent_courses = Course.objects.all().order_by('-published_date')[:5]
    return render(request, "single.html", {'course': course, 'subjects': subjects, 'recent_courses': recent_courses})

def search(request):
    st = request.GET.get('q', '')
    # print(st)
    courses = Course.objects.filter(name__icontains=st)
    return render(request, "course.html", {'courses': courses})