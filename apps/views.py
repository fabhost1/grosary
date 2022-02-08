from django.shortcuts import render
from django.contrib.auth.models import User
# Create your views here.
def home(request):
    return render(request,'first.html')

def register(request):
    return render (request,'register.html')
def login1(request):
    return render(request,'login.html')
def logout(request):
    return render(request,'index.html')

def register1(request):

    data=User()
    data.username=request.POST.get('username')
    data.first_name=request.POST.get('firstname')
    data.last_name=request.POST.get('lastname')
    data.email=request.POST.get('email')
    data.password=request.POST.get('password1')

    data.save()
    return render(request,'login.html')
def login(request):

    if request.method == 'POST':

        username=request.POST.get('username')
        password=request.POST.get('password')

        try: 
            User.objects.get(username=username,password=password)
            return render(request,'index.html')
        except:
            return render(request,'login.html')
    else:
        return render(request,'register.html')
def cart(request):
    return render(request,'cart.html')
def shop(request):
    return render(request,'shop.html')
def slide(request):
    return render(request,'index_2.html')


     


