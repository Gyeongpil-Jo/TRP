from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseNotAllowed
from .models import Inform
from .forms import InformForm
from django.utils import timezone
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def home(request):
    context = {'name': request.user}
    return render(request, 'TRP/home.html', context)


@login_required(login_url='common:login')
def start_date(request):
    if Inform.objects.filter(name=request.user):
        return redirect('TRP:calculate')

    if request.method == 'POST':
        form = InformForm(request.POST)
        if form.is_valid():
            inform = form.save(commit=False)
            inform.name = request.user
            inform.save()
            return redirect('TRP:calculate')
    else:
        form = InformForm()
    context = {'form': form}
    return render(request, 'TRP/start_date.html', context)


@login_required(login_url='common:login')
def calculate(request):
    inform = Inform.objects.get(name=request.user)
    context = {'inform': inform}
    return render(request, 'TRP/calculate.html', context)


@login_required(login_url='common:login')
def file_upload(request):
    inform = Inform.objects.get(name=request.user)
    if request.method == 'POST':
        form = InformForm(request.POST, request.FILES, instance=inform)
        if form.is_valid():
            inform = form.save(commit=False)
            inform.save()
            return redirect('TRP:calculate')
    else:
        form = InformForm(instance=inform)
    context = {'form': form}
    return render(request, 'TRP/file_upload.html', context)