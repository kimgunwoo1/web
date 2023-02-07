from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.core.paginator import Paginator
# Create your views here.

def todo_list(request):
    todos = Todo.objects.filter(complete=False)
    paginator = Paginator(todos,5) #5개씩
    page_num = request.GET.get('page','1') #page 값이 없으면 default 1

    #페이지에 맞는 모델
    page_obj = paginator.get_page(page_num)

    #총게시물 수
    print ('----------count----------')
    print(page_obj.count)

    print ('----------number - 현재 페이지번호 ---------')
    print(page_obj.number)

    print ('----------num_pages----------')
    print(page_obj.paginator.num_pages)

    #총 페이지 range객체
    print('----------총 페이지 range객체----------')
    print(page_obj.paginator.page_range)

    print('----------다음페이지, 이전페이지----------')
    print(page_obj.has_next())
    print(page_obj.has_previous())

    try :
        print('----------다음 페이지 숫자 없으면 에러----------')
        print(page_obj.next_page_number())

        print('----------이전 페이지 숫자 없으면 에러----------')
        print(page_obj.previous_page_number())
    except :
        pass

    print('----------start_index----------')
    print(page_obj.start_index())
    print('----------end_index----------')
    print(page_obj.end_index())

    return render(request, 'todo/todo_list.html', {'todos': page_obj})

# def todo_list(request):
#     todos = Todo.objects.filter(complete=False)
#     return render(request, 'todo/todo_list.html', {'todos': todos})

    


def todo_post(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.save()
            
            if 'imagefile' in request.FILES.key():
                upload_file = request.FILES['imagefile']
                upload = default_storage.save(upload_file.name, 
                ContentFile(upload_file.read()))
                # default_storage = /media, 화일 업로드 기능

                Todo.objects.filter(id=todo.id).update(imagefile=upload)
                #신규로 저장한 todo의 id를 참조해서 imagefile의 값을 update함
            # upload_file = request.FILES['imagefile']
            # upload = default_storage.save(upload_file.name, 
            # ContentFile(upload_file.read()))
            # # default_storage = /media, 화일 업로드 기능

            # Todo.objects.filter(id=todo.id).update(imagefile=upload)
            # #신규로 저장한 todo의 id를 참조해서 imagefile의 값을 update함
            return redirect('todo:todo_list')
    else:
        form = TodoForm()
    return render(request, 'todo/todo_post.html', {'form':form})

def todo_detail(request, pk):
    todo = Todo.objects.get(id=pk)
    return render(request, 'todo/todo_detail.html', {'todo':todo})

def todo_done(request, pk):
    todo = Todo.objects.get(id=pk)
    todo.complete = True
    todo.save()
    return redirect('todo:todo_list')

def todo_edit(request, pk):
    todo = Todo.objects.get(id=pk)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.save()
            return redirect('todo:todo_list')
    else:
        form = TodoForm(instance=todo)

    return render(request, 'todo/todo_post.html', {'form':form})


def done_list(request):
    todos = Todo.objects.filter(complete=True)
    return render(request, 'todo/done_list.html', {'todos': todos})


def todo_delete(request, pk):
    todo = Todo.objects.get(id=pk)
    todo.delete()

    return redirect('todo:todo_list')