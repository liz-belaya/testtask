from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Qr
from .forms import QrForm
import qrcode

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

def qr_remove(request, pk):
    qr = get_object_or_404(Qr, pk=pk)
    qr.delete()
    return redirect('qr_list')

def qr_create(request,pk):
    qr = get_object_or_404(Qr, pk=pk)
    image = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    image.add_data(qr)
    image.make(fit=True)
    img = image.make_image()
    name = 'qr'+str(pk)+'.png'
    img.save("qr_images/"+str(name))
    qr.image = ("qr_images/"+str(name))
    qr.save()
    return redirect('qr_list')


def qr_transition(request,pk):
    qr = get_object_or_404(Qr, pk=pk)
    qr.number_of_transitions += 1
    qr.save()
    return render(request,'qr/qr_transition.html')



# Create your views here.
