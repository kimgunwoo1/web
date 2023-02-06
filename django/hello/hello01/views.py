from django.shortcuts import render
from django.http import HttpResponse

app_name='hello01'
def test(request):
    return HttpResponse('<h1>Hello, test2222222~!</h1>')

