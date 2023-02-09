from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'var/index.html')


def variable01(request):
    my_list = ['python','django','template']
    return render(request,'var/variable01.html',{'lst':my_list})

def variable02(request):    
    my_dict={'name':'seo', 'class':'AI 취업'}
    return render(request,'var/variable02.html',{'nme':my_dict})

def testfor(request):
    return render(request,'var/testfor.html',{'number':range(1,11)})
    # templates/var/testfor.html

def if01(request):
    return render(request,'var/if01.html',{'user':{'id':'hong-gd'}})

def if02(request):
    member = {'id':'multi', 'class':'ai', 'role':'manager'}
    return render(request,'var/if02.html',{'member':member})

def get_post(request):
    if request.method == 'GET':
        q = request.GET['q']
        return render(request,'var/get.html',{'q':q})
    elif request.method == 'POST':
        id = request.POST['id']
        return render(request,'var/post.html',{'id1':id})
def staticTest(request):
    return render(request,'var/staticTest.html')
