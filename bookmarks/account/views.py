from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.contrib.auth import authenticate,login
from .forms import LoginForm,UserRegistrationForm,add_new_items
from django.contrib.auth.decorators import login_required
from .models import product
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
    productData = product.objects.all()
    data = {
        'productData': productData
    }
    return render(request, 'account/items.html', data)

def service_personnel(request):
    return render(request,'account/service_personnel.html')

def new_items(request):
    new_form = add_new_items()
    return render(request,'account/new_items.html', {'new_form':new_form})

def saveproduct(request):

    if request.method=="POST":
        item_name=request.POST.get('item_name')
        price=request.POST.get('price')
        brand=request.POST.get('brand')
        model=request.POST.get('model')
        type=request.POST.get('type')
        date=request.POST.get('date')
        invoice_image=request.POST.get('invoice_image')

        if request.POST.get('Warranty') =='on':
            Warranty = True
        else:
            Warranty =False

        duration_warranty=request.POST.get('duration_warranty')

        if request.POST.get('Is_Alert_Needed') == 'on':
            Is_Alert_Needed = True
        else:
            Is_Alert_Needed = False

        if request.POST.get('Insurance') == 'on':
            Insurance = True
        else:
            Insurance = False
        duration_insurance=request.POST.get('duration_insurance')
        en=product(item_name=item_name,price=price, brand=brand, model=model, type=type, date=date, invoice_image=invoice_image,
                   Warranty=Warranty, duration_warranty=duration_warranty, Is_Alert_Needed=Is_Alert_Needed,
                   Insurance=Insurance, duration_insurance=duration_insurance)
        en.save()
    return render(request, 'account/new_items.html')

