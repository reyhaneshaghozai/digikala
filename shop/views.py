from django.shortcuts import render,redirect
from.models import Product, Category
from django.contrib.auth import authenticate, login , logout
from django.contrib import messages 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms 
from.forms import SignUpForm
from django.shortcuts import get_object_or_404


def helloworld(request):
    all_products = Product.objects.all()
    return render (request , "index.html",{'Products': all_products})
def about(request):
    return render(request,'about.html')

#برای دکمه های ورود و خروج
def login_user(request):
    if request.method =="POST":
        username=request.POST['username']
        password=request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request,("با موفقیت وارد شدید"))
            return redirect("home")
        else:
            messages.success(request,("مشکلی در لاگین وجود دارد"))
            return redirect('login')
    else:
        return render(request,"login.html")

def logout_user(request):
    logout(request)
    messages.success(request,('با موفقیت خارج شدید!'))
    return redirect('home')

def signup_user(request):
    form=SignUpForm()
    # اگر فرمی به ویو ارسال شده باشه باید اونو بگیریم و سیوش بکنیم
    if request.method == "POST":
        form = SignUpForm(request.POST)    #این ریکوِئست . پست     یعنی هر چیزی که از کاربر گرفتی و بیا داخل ساین اپ فرم بریز
        if form.is_valid():

            #هر وقت کاربر بیاد ثبت نام کنه ما اونو لاگین بکنیم  
            username=form.cleaned_data['username']
            password1=form.cleaned_data['password1']
            user = authenticate(request, username=username,password=password1)
            login(request, user)
            form.save()       # اگر این فرم هیچ مشگلی نداشت بیا و سیوش کن
            messages.success(request,(" اکانت شما ساخته شد!"))
            return redirect('home')     #وقتی که کاربر اکانتش ساخته شد  دوباره بیاد به صفحه اصلی 
        else:
             messages.success(request,("مشکلی در ثبت نام شما وجود دارد"))
             return redirect('signup')    
    else:    
        return render(request,'signup.html',{'form':form})
    

def product(request,pk):
    product = Product.objects.get(id=pk)
    return render(request, "product.html", {'product': product})


def Category(request,cat):
    cat = cat.replace("-"," ")
    try:
        category = Category.abjects.get(name=cat)
        products = Product.abjects.filter(Category = Category) 
        return render(request,'category.html',{"products": products ,"category": category })
    except:
        messages.success(request, ('دسته بندی وجود ندارد '))
        print('sssss')
        return redirect('home')

 