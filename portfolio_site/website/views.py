from django.shortcuts import render
from .models import *
# Create your views here.

def index(request):
    aboutMe = AboutMe.objects.all()
    context = {
        'aboutMe':aboutMe
    }
    return render(request, 'index.html')

def resume(request):
    experience = Experience.objects.all()
    certificate = Certificate.objects.all()
    designSkill = DesignSkill.objects.all()
    codingSkill = CodingSkill.objects.all()
    context = {
        'experience':experience,
        'certificate':certificate,
        'designSkill':designSkill,
        'codingSkill':codingSkill,
    }
    return render(request, 'resume.html')

def portfolio(request):
    portfolio = Portfolio.objects.all()
    context = {
        'portfolio':portfolio,
    }
    return render(request, 'portfolio.html')

def contact(request):
    contact = ContactForm.objects.all()
    context = {
        'contact':contact
    }
    return render(request, 'contact.html')

def blog(request):
    blog = Blog.objects.all()
    context = {
        'blog':blog
    }
    return render(request, 'blog.html')