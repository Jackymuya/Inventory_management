from django import forms
from django.contrib.auth.forms import UserCreationForm
from django .contrib.auth.models import User
from .models import Category,Product,Supplier,Purchase,Sale

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name','description']


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name','sku','category','description','price','quantity','minimum_stock']

        widgets = {
            
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter product name',
            }),

            'sku': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter SKU',
            }),

            'category': forms.Select(attrs={
                'class': 'form-select',
            }),

            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter product description',
                'rows': 4,
            }),

            'price': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': '0.00',
                'step': '0.01',
            }),

            'quantity': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter quantity',
                'min': '0',
            }),

            'minimum_stock': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter minimum stock level',
                'min': '0',
            }),
        }


class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = [
            'name',
            'contact_person',
            'phone',
            'email',
            'address',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

    
class PurchaseForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = [
            'product',
            'supplier',
            'quantity',
            'unit_cost',
        ]

        widgets = {
            'product': forms.Select(
                attrs={'class': 'form-select'}
            ),
            'supplier': forms.Select(
                attrs={'class': 'form-select'}
            ),
            'quantity': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'min': 1,
                    'placeholder': 'Enter quantity'
                }
            ),
            'unit_cost': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'min': 0,
                    'step': '0.01',
                    'placeholder': 'Enter unit cost'
                }
            ),
        }


class SaleForm(forms.ModelForm):
    class Meta:
        model = Sale
        fields = ['product', 'quantity', 'selling_price']
        widgets = {
            'product': forms.Select(
                attrs={'class': 'form-select'}
            ),
            'quantity': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'min': 1,
                    'placeholder': 'Enter quantity'
                }
            ),
            'selling_price': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'min': 0,
                    'step': '0.01',
                    'placeholder': 'Enter selling price'
                }
            ),
        }
    


            
        
        
        


