from django.shortcuts import render, redirect
from .models import Decade, Fad
from .forms import DecadeForm, FadForm
from django.contrib.auth.decorators import login_required

# Create your views here.
#Remember to import models
# index - decades
def decade_list(request):
    decades = Decade.objects.all()
    return render(request, 'nostaldja/decade_list.html', { 'decades': decades })

def decade_detail(request, pk):
    decade = Decade.objects.get(pk=pk)
    return render(request, 'nostaldja/decade_detail.html', { 'decade': decade })

@login_required
def decade_create(request):
    if request.method == 'POST':
        form = DecadeForm(request.POST)
        if form.is_valid():
            decade = form.save()
            return redirect('decade_detail', pk=decade.pk)
    else:
        form = DecadeForm()
    return render(request, 'nostaldja/decade_form.html', { 'form': form })

@login_required
def decade_delete(request, pk):
    Decade.objects.get(id=pk).delete()
    return redirect('decade_list')

def fads_list(request):
    fads = Fad.objects.all()
    return render(request, 'nostaldja/fad_list.html', { 'fads': fads })

def fads_detail(request, id):
    fad = Fad.objects.get(id=id)
    return render(request, 'nostaldja/fad_detail.html', { 'fad': fad })

@login_required
def fads_create(request):
    if request.method == 'POST':
        form = FadForm(request.POST)
        if form.is_valid():
            fad = form.save()
            return redirect('fads_detail', id=fad.id)
    else:
        form = FadForm()
    return render(request, 'nostaldja/decade_form.html', { 'form': form })

@login_required
def fads_delete(request, id):
    Fad.objects.get(id=id).delete()
    return redirect('fads_list')



#make a function that combines the data with our view template and renders it


#Don't forget to setup my URLS!