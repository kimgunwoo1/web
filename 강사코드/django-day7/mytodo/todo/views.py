from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.core.paginator import Paginator

# Create your views here.

def todo_list(request):
    todos = Todo.objects.filter(complete=False)

    paginator = Paginator(todos,5)
    page_num = request.GET.get('page','1') # default : 없으면 1
    page_obj = paginator.get_page(page_num)


    
    return render(request,'todo/todo_list.html',{'todos':page_obj})


def todo_post(request):
    if request.method == 'GET':
        form = TodoForm()
        return render(request,'todo/todo_post.html',{'form':form})
    else:  #post
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.save()

            if 'imagefile' in request.FILES.key() :
                upload_file = request.FILES['imagefile']
                upload = default_storage.save(upload_file.name,ContentFile(upload_file.read()))
                # default_storage = /media,  화일 업로드 기능
                Todo.objects.filter(id=todo.id).update(imagefile=upload)
            #신규로 저장한 todo의 id를 참조해서 imagefile의 값을 update함

            return redirect('todo:todo_list')

            # 또다른 방법 (photo table 기준)
            # new_photo = Photo.objects.create(
            #     title= form.cleaned_data['title'],
            #     author = form.cleaned_data['author'],
            #     imagefile = request.FILES['imagefile'],
            #     description = form.cleaned_data['description'],
            #     price = form.cleaned_data['price'],
            # )
            # return redirect('photo_detail', pk=new_photo.id)

def todo_detail(request,pk):
    todo = Todo.objects.get(id=pk)
    return render(request,'todo/todo_detail.html',{'todo':todo})

def todo_edit(request,pk):
    todo = Todo.objects.get(id=pk)
    if request.method == 'GET' :
        form = TodoForm(instance=todo)
    else:
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid() :
            todo = form.save(commit=False)
            todo.save()

            upload_file = request.FILES['imagefile']
            upload = default_storage.save(upload_file.name,ContentFile(upload_file.read()))
            Todo.objects.filter(id=todo.id).update(imagefile=upload)

            return redirect('todo:todo_list')

    return render(request,'todo/todo_post.html',{'form':form})


def done_list(request):
    todos = Todo.objects.filter(complete=True)
    return render(request,'todo/done_list.html',{'todos':todos})    


def todo_done(request,pk):
    todo = Todo.objects.get(id=pk)
    todo.complete = True
    todo.save()
    return redirect('todo:todo_list')

def todo_delete(request,pk):
    todo = Todo.objects.get(id=pk)
    todo.delete()

    return redirect('todo:todo_list')