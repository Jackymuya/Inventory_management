from django.shortcuts import render,redirect
from .models import Category,Product,Supplier,Purchase,Sale
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import CategoryForm
from .forms import ProductForm
from .forms import SupplierForm
from .forms import PurchaseForm
from .forms import SaleForm
from django.db import models
from django.db.models import Sum
from django.contrib.auth.forms import UserCreationForm




@login_required
def dashboard(request):

    return render(
        request,
        'inventory/dashboard.html'
    )


@login_required
def category(request):
    categories = Category.objects.all()
    return render(
        request,
        'inventory/category/category.html',
        { 
            'categories' :categories
        }
    )
@login_required
def category_add(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category')

    

    else:
        form = CategoryForm()
    
    return render(
        request,
        'inventory/category/add_category.html',
        {
            'form':form
        }
    )

@login_required
def products(request):
    products = Product.objects.all()

    return render(
        request,
        'inventory/product/product.html',
        {
            'products':products
        }
    )
@login_required    
def product_add(request):
    if request.method == 'POST':
         form = ProductForm(request.POST)
         if form .is_valid():

            form.save()
            return redirect('products')
   
        
        

    else:

        form = ProductForm()

    return render(
            request,
            'inventory/product/add_product.html',
            {
                'form':form
            }
        )    
@login_required
def supplier(request):
    supplier = Supplier.objects.all()

    return render(
        request, 
        'inventory/supplier/supplier.html',

        {
            'supplier':supplier
        }
    )
@login_required
def supplier_add(request):
    if request.method =='POST':
        form = SupplierForm(request.POST)
        if form .is_valid():
            form.save()

            return redirect(supplier)

    else:

        form = SupplierForm()

        return render(
            request,
            'inventory/supplier/add_supplier.html',

            {
                'form' :form
            }
        )


def purchase(request):
    purchase = Purchase.objects.all()
    return render(
        request,
        'inventory/purchase/purchase.html',
        {
            'purchase':purchase
        }
    )
@login_required
def purchase_add(request):
    if request. method == 'POST':
        form = PurchaseForm(request.POST)
        if form .is_valid():
            form.save()
            return redirect (purchase
            
            )


    else:
        form  = PurchaseForm()
        return render(
            request,
            'inventory/purchase/add_purchase.html',

            {
                'purchase':purchase
            }
        )
        
def sales(request):
    sales_list = Sale.objects.all()
    return render(
        request,
        'inventory/sale/sales.html',
        {
            'sales':sales_list
        }
    )

@login_required
def sale_add(request):
    if request.method == 'POST':
         form = SaleForm(request.POST)
         if form .is_valid():
            form.save()
            return redirect('sales'
        
   
    )


    else:

        form = SaleForm()
        return render(
            request,
            'inventory/sale/add_sale.html',
            {
                'form':form
            }
        )

@login_required
def stock(request):
    products = Product.objects.all()

    low_stock_count = Product.objects.filter(
        quantity__lte=models.F('minimum_stock')
    ).count()

    context = {
        'products': products,
        'low_stock_count': low_stock_count,
    }

    return render(
        request,
        'inventory/stock/stock.html',
        context
    )
@login_required
def reports(request):
    total_products = Product.objects.count()

    total_stock = Product.objects.aggregate(
        total=Sum('quantity')
    )['total'] or 0

    low_stock_count = Product.objects.filter(
        quantity__lte=models.F('minimum_stock')
    ).count()

    context = {
        'total_products': total_products,
        'total_stock': total_stock,
        'low_stock_count': low_stock_count,
    }

    return render(
        request,
        'inventory/reports/reports.html',
        context
    )




@login_required
@user_passes_test(lambda user: user.is_staff)
def users_list(request):
    users = User.objects.all().order_by('username')

    context = {
        'users': users,
    }

    return render(
        request,
        'inventory/users/users.html',
        context
    )
@login_required   
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = UserCreationForm()

    # Style the form fields here, after creating the form
    for field in form.fields.values():
        field.widget.attrs.update({
            'class': 'form-control'
        })
       
    return render(
        request,
        'inventory/register.html',
        {'form': form}
    )






