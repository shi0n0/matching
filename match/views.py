from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'matchingapp/index.html', {})

def mypage(request):
    return render(request, 'matchingapp/mypage.html', {})