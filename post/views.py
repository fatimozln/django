from django.shortcuts import render, HttpResponse
from . import models
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required(login_url="/accounts/login")
def add_post(request):
    return render(request, 'post_visit/add_post.html', {'post': add_post})
