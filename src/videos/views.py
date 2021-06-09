from django.core.exceptions import ViewDoesNotExist
from django.shortcuts import redirect, render
from gallary.decorators import allowed_user

from .models import Video
from .forms import Video_Model_From

# Create your views here.
def myvideo(request,pk,post_title):
    vdo = Video.objects.get(id =pk)
    vdos = Video.objects.all().exclude(id=pk)
    context = {
        'vdo':vdo,
        'vdos':vdos
    }
    return render(request,'myvideos.html',context)

def allVideos(request):
    vdos = Video.objects.all()
    vdoForm  = Video_Model_From()
    
    if request.method == 'POST':
        v_form =Video_Model_From(request.POST,request.FILES or None)
        if v_form.is_valid():
            instance = v_form.save(commit=False)
            instance.save()


    context = {
        'vdos':vdos,
        'vdoForm':vdoForm
    }
    return render(request,'allvideos.html',context)

@allowed_user(allowed_roles=['admin'])
def editVideo(request,pk):
    update_vdo  = Video.objects.get(id=pk)
    v_form = Video_Model_From(instance=update_vdo)
    if request.method == 'POST':
        form = Video_Model_From(request.POST,request.FILES,instance=update_vdo)
        form.save()
        return redirect('my-videos')
    context = {
        'v_form':v_form
    }
    return render(request,'updatevdo.html',context)

@allowed_user(allowed_roles=['admin'])
def deleteVdo(request,pk):
    deleted_vdo = Video.objects.get(id=pk)
    if 'confirm_delete_btn' in request.POST:
        deleted_vdo.delete()
        return redirect('my-videos')
    elif 'nokeepit' in request.POST:
        return redirect('my-videos')



    context = {
        'deleted_vdo':deleted_vdo
    }
    return render(request,'deletevdo.html',context)