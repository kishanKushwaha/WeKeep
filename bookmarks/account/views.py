from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.contrib.auth import authenticate,login
from .forms import LoginForm,UserRegistrationForm,add_new_items
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    return render(request,'account/dashboard.html',{'section':'dashboard'})

# Create your views here.
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,username=cd['username'],
                                      password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request,user)
                    return HttpResponse('Authenticated'' Successfully')
                else:
                    return HttpResponse('Disabled Account')
            else:
                return HttpResponse("Invalid login")
    else:
        form=LoginForm()
    return render(request,'account/login.html',{'form':form})

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            #Profile.objects.create(user=new_user)
            return render(request,'account/register_done.html',{'new_user': new_user})
    else:
        user_form=UserRegistrationForm()
    return render(request,'account/register.html',{'user_form': user_form})

def service(request):
    return render(request,'account/service.html')

def items(request):
    return render(request,'account/items.html')

def service_personnel(request):
    return render(request,'account/service_personnel.html')

def new_items(request):
    new_form = add_new_items()
    return render(request,'account/new_items.html', {'new_form':new_form})
