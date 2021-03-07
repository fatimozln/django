from django.shortcuts import render, HttpResponse, redirect
from . import models
from django.contrib.auth.decorators import login_required
from . import forms
from articles import urls
# Create your views here.


@login_required(login_url="/accounts/login")
def add_post(request):
    if request.method == 'POST':
        form = forms.Create_post(request.POST)
        if form.is_valid():
            return redirect('articles:list')
    else:
        form = forms.Create_post()
    return render(request, 'post_visit/add_post.html', {'form': form})
