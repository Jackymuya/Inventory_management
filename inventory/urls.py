
from django.contrib.auth import views as auth_views
from django.urls import path
from django.shortcuts import redirect
from . import views

urlpatterns = [
    # Homepage: redirect visitors to login
    path('', lambda request: redirect('login'), name='home'),

    # Dashboard
    path('dashboard/', views.dashboard, name='dashboard'),

    # Categories
    path('category/', views.category, name='category'),
    path('category/add/', views.category_add, name='add_category'),

    # Products
    path('products/', views.products, name='products'),
    path('products/add/', views.product_add, name='add_product'),

    # Suppliers
    path('supplier/', views.supplier, name='supplier'),
    path('supplier/add/', views.supplier_add, name='add_supplier'),

    # Purchases
    path('purchase/', views.purchase, name='purchase'),
    path('purchase/add/', views.purchase_add, name='add_purchase'),

    # Sales
    path('sale/', views.sales, name='sales'),
    path('sale/add/', views.sale_add, name='add_sale'),

    # Stock
    path('stock/', views.stock, name='stock'),

    # Reports
    path('reports/', views.reports, name='reports'),

    # Users
    path('user/', views.users_list, name='user'),

    # Login
    path(
        'login/',
        auth_views.LoginView.as_view(
            template_name='inventory/login.html'
        ),
        name='login',
    ),

    # Logout
    path(
        'logout/',
        auth_views.LogoutView.as_view(),
        name='logout',
    ),
]

    