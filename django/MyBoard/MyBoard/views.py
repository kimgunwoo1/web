from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Myboard
from .models import MyMember
from django.core.paginator import Paginator

def index(request):
    myboard_all = Myboard.objects.all().order_by('-id')

    paginator = Paginator(myboard_all,5) #5개씩
    page_num = request.GET.get('page','3') #page 값이 없으면 default 1

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



    return render(request, 'index.html', {'board_all':page_obj})

def insert_form(request):
    return render(request, 'insert_form.html')

def insert_proc(request):
    myname = request.POST['myname']
    mytitle = request.POST['mytitle']
    mycontent = request.POST['mycontent']

    result = Myboard.objects.create(myname=myname, mytitle=mytitle,
            mycontent=mycontent, mydate=timezone.now())

    if result:
        return redirect('index1')
    else:
        return redirect('forminsert')

def detail(request, id):
    dto = Myboard.objects.get(id=id)
    return render(request, 'detail.html', {'dto': dto})

def delete_proc(request, id):
    result = Myboard.objects.get(id=id).delete()

    print('=======================')
    print(result)
    print('=======================')

    if result[0]:
        return redirect('index1')
    else:
        return redirect('/detail/'+id)

def update_form(request, id):
    post = Myboard.objects.get(id=id)
    return render(request, 'update.html', {'dto':post})

def update_res(request, id):
    id = request.POST['id']
    mytitle = request.POST['mytitle']
    mycontent = request.POST['mycontent']

    myboard = Myboard.objects.filter(id=id)
    result_title = myboard.update(mytitle=mytitle)
    result_content = myboard.update(mycontent=mycontent)

    if result_title + result_content == 2:
        return redirect('detail', id=id)
    else:
        return redirect('/update_form'+id)

def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    elif request.method == 'POST':
        myname = request.POST['myname']
        mypassword = request.POST['mypassword']
        myemail = request.POST['myemail']

        result = MyMember.objects.create(myname=myname, mypassword=mypassword,
            myemail=myemail)

    if result:
        return redirect('index1')
    else:
        return redirect('register')

def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        myname = request.POST['myname']
        mypassword = request.POST['mypassword']

        mymember = MyMember.objects.get(myname=myname)

        if mypassword == mymember.mypassword:
            #성공했으니 로그인이 된 페이지
            request.session['myname'] = mymember.myname
            return redirect('index1')
        else:
            #다시 로그인 페이지
            return redirect('login')


def logout(request):
    del request.session['myname']
    return redirect('index1')