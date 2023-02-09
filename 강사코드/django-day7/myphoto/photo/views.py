from django.shortcuts import render, get_object_or_404, redirect
from .models import Photo
from .forms import PhotoForm
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.http import HttpResponse

# Create your views here.
def photo_list(request):
    photo = Photo.objects.all()
    return render(request,'photo/photo_list.html',{'photos':photo})

def photo_detail(request,pk):
    photo = get_object_or_404(Photo,pk=pk)
    return render(request,'photo/photo_detail.html',{'photo':photo})
    

def photo_post(request):
    if request.method == 'GET' :
        form = PhotoForm()
        return render(request,'photo/photo_post.html',{'form':form})
    elif request.method == 'POST' :
        form = PhotoForm(request.POST)
        if form.is_valid() :
            photo = form.save(commit=False)
            photo.save()
            upload_file = request.FILES['imagefile']
            default_storage.save(upload_file.name, ContentFile(upload_file.read()))
            Photo.objects.filter(id=photo.id).update(imagefile=upload_file)            
            return redirect('photo_detail', photo.id)

    return render(request,'photo/photo_post.html',{'form':form})

def photo_edit(request,pk):
    photo = get_object_or_404(Photo,pk=pk)

    if request.method=="GET":
        form = PhotoForm(instance=photo)
    elif request.method =='POST':
        form = PhotoForm(request.POST, instance=photo)
        if form.is_valid() :
            photo = form.save(commit=False)
            photo.save()

            upload_file = request.FILES['imagefile']
            default_storage.save(upload_file.name, ContentFile(upload_file.read()))
            Photo.objects.filter(id=pk).update(imagefile=upload_file)
            return redirect('photo_detail',pk=photo.id)

    return render(request,'photo/photo_post.html',{'form':form})

def photo_del(request,pk):
    Photo.objects.get(id=pk).delete()
    return redirect('photo_list')


def download_proc(reuqest,filename):
    pass