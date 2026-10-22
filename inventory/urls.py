from django.contrib.auth import views as auth_views
from django.urls import path
from . import views


urlpatterns = [

    path(
        'dashboard/',
        views.dashboard,
        name='dashboard'
    ),

    path(
        'category/',
        views.category,
        name='category'
    ),

    path(
        'category/add/',
        views.category_add,
        name='add_category'
    ),

    path(
        'products/',
        views.products,
        name='products'
    ),

    path(
        'products/add/',
        views.product_add,
        name='add_product'
    ),

    path( 
        'supplier/',
        views.supplier,
        name = 'supplier'
    ),

    path(
        'supplier/add',
        views.supplier_add,
        name = 'add_supplier'
        
    ),

    path( 
        'purchase/',
        views.purchase,
        name = 'purchase'
    ),

    path(
        'purchase/add',
        views.purchase_add,
        name = 'add_purchase'
        
    ),

    path(
        'sale/',
        views.sales,
        name = 'sales'
    ),


    path(
        'sale/add/',
        views.sale_add,
        name = 'add_sale'
    ),

    path(
        'stock/',
        views.stock,
        name = 'stock'

    ),

    path('reports/',
    views.reports,
    name = 'reports'
    ),


    path('user/',
    views.users_list,
    name = 'user'

    ),

    path(
        'logout/',auth_views.LogoutView.as_view(), name='logout'
    ),

    path('reports/', views.reports, name='reports'),

    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    path(
    'login/',
    auth_views.LoginView.as_view(
        template_name='inventory/login.html'
    ),
    name='login',
),
]


    