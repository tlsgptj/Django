from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'myapp/index.html')
# http 객체 리턴
# MVT 구조 
# model -> M 
# template -> 웹의 화면 구성을 담당
# view -> Model과 Template 사이를 연결함 