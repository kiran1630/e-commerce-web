from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.
from .models import *
from django.contrib import messages
from .form import CustomerUserForm
from django.contrib.auth import authenticate ,login,logout
from django.http import JsonResponse
import json 
def home(request):
    product= product_table.objects.filter(trending=1)
    return render(request,'shopapp/index.html',{'product' :product})

def  logout_page(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request,"Logged out Successfully")
    return redirect('/')

def add_to_cart(request):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        if request.user.is_authenticated:
            data = json.load(request)
            product_qty = data['product_qty']
            product_id = data['pid']
            print(request.user.id,'qty',product_qty,'pid',product_id)
            product_status = product_table.objects.get(id=product_id)
            if product_status:
                if Cart.objects.filter(user = request.user.id,product_id =product_id):
                    return JsonResponse({'status':'Product Already in Cart'},status=200)
                else:
                    if product_status.quantity>=product_qty:
                        Cart.objects.create(user = request.user,product_id =product_id,product_qty = product_qty)
                        print('product added')
                        return JsonResponse({'status':'Product Added to Cart'},status=200)
                        
                    else:
                        print('stock not available')
                        return JsonResponse({'status':'Product Stock not Available'},status =200)
                    return JsonResponse({'status':'Product Stock Not Available'},status=200)
        else:
            print('first login to add')
            return JsonResponse({'status':'Login to cart'},status =200)
    else:
            print('second login to add')
            return JsonResponse({'status':'Login to cart'},status =200)


def login_page(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:

        if request.method == 'POST':
                name = request.POST.get('username')
                passkey = request.POST.get('password')
                user = authenticate(request,username = name, password = passkey)
                if user is not None:
                    login(request,user)
                    messages.success(request,"Logged in Successfully")
                    return redirect('/')
                else:
                    messages.error(request,"Invalid User Name or Password")
                    return redirect('/login')
    return render(request,'shopapp/login.html')

def register(request):
    form = CustomerUserForm()
    if request.method == 'POST':
      form = CustomerUserForm(request.POST)
      if form.is_valid():
          form.save()
          messages.success(request,'Registration Success You can Login Now...')
          return redirect('/login')
    print('not done')
    return render(request,'shopapp/register.html',{'form':form})

def collections(request):
    category =  Category_table.objects.filter(status=0)
    return render(request,'shopapp/layout/collections.html',{'category':category})

def collection_view(request,name):
    if (Category_table.objects.filter(name=name,status=0)):
        product = product_table.objects.filter(categoty__name=name)
        print(product)
        return render(request,'shopapp/products/index.html',{'product':product,'category_name':name})
    else:
        messages.warning(request,'NO SUCH PRODUCT')
        return redirect('collections')

def product_detail(request,cname,pname):
    if (Category_table.objects.filter(name=cname,status=0)):
        if (product_table.objects.filter(name=pname,status=0)):
            product =  (product_table.objects.filter(name=pname,status=0)).first()
            return render(request,'shopapp/products/product_detail.html',{'product':product})
        else:
            messages.warning(request,'NO SUCH PRODUCT')
            redirect('collections')
    else:
        messages.warning(request,'NO SUCH CATEGORY')
        redirect('collections')


