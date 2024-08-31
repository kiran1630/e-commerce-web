from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.
from .models import *
from django.contrib import messages
from .form import CustomerUserForm
def home(request):
    product= product_table.objects.filter(trending=1)
    return render(request,'shopapp/index.html',{'product' :product})

def login(request):
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


