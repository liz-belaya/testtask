from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Qr
from .forms import QrForm

def qr_list(request):
    qrs = Qr.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'qr/qr_list.html', {'qrs':qrs})

def qr_detail(request, pk):
    qr = get_object_or_404(Qr, pk=pk)
    return render(request, 'qr/qr_detail.html', {'qr': qr})

def qr_new(request):
    if request.method == "POST":
        form = QrForm(request.POST)
        if form.is_valid():
            qr = form.save(commit=False)
            qr.number_of_transitions = 0
            qr.published_date = timezone.now()
            qr.save()
            return redirect('qr_list')
    else:
        form = QrForm()
    return render(request, 'qr/qr_edit.html', {'form': form})

def qr_edit(request, pk):
    qr = get_object_or_404(Qr, pk=pk)
    if request.method == "POST":
        form = QrForm(request.POST, instance=qr)
        if form.is_valid():
            qr = form.save(commit=False)
            qr.number_of_transitions = 0
            qr.published_date = timezone.now()
            qr.save()
            return redirect('qr_list')
    else:
        form = QrForm(instance=qr)
    return render(request, 'qr/qr_edit.html', {'form': form})
# Create your views here.
