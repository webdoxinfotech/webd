from django.http import HttpResponse, FileResponse, Http404
from django.shortcuts import render
from django.shortcuts import get_object_or_404
import re
# Create your views here.
from courses.forms import CertificateForm
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

def insert_hyphen_before_first_digit(input_string):
    if (input_string.find("-") == -1):
        result = ""
        digit_found = False

        for char in input_string:
            if char.isdigit() and not digit_found:
                result += '-' + char
                digit_found = True
            else:
                result += char

        return result
    return input_string

def getCertificate(request):
    form = CertificateForm()
    if request.method == "POST":
        form = CertificateForm(request.POST or None)
        if form.is_valid():
            data = insert_hyphen_before_first_digit(form.cleaned_data['ref_id'].replace(' ', ''))
            print(data)
            try:
                # uploaded_file = get_object_or_404(Certificate, ref_id__iexact=data)
                uploaded_file = Certificate.objects.get(ref_id__iexact=data)
                return render(request, 'certificate.html', {'form': form, 'uploaded_file': uploaded_file})
            except Certificate.DoesNotExist as e:
                # uploaded_file = False
                return render(request, "certificate.html", {'form': form, 'err': e})
                # print(e)
    return render(request, "certificate.html", {'form': form})
