from django.shortcuts import render

def index(request):
    return render(request, 'tags/index.html',{'name':'Kim Gun Woo'})
    #BASE_DIR : project_name/templates
    #project_name/templates/tags/index.html