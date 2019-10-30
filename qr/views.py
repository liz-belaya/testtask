from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Qr

def qr_list(request):
    qrs = Qr.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'qr/qr_list.html', {'qrs':qrs})

def qr_detail(request, pk):
    qr = get_object_or_404(Qr, pk=pk)
    return render(request, 'qr/qr_detail.html', {'qr': qr})
# Create your views here.
