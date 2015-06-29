from django import forms
from .models import Product

class ProductAdminForm(forms.ModelForm):
    class Meta:
        model = Product
        '''
        fields = ('name', 'slug', 'price', 'old_price', 'brand', 'sku', 'image',
                'is_active', 'is_bestseller', 'is_featured', 'quantity', 
                'description', 'meta_keywords', 'meta_description',)
        '''
        exclude = ('created_at', 'updated_at',)

    def clean_price(self):
        if self.cleaned_data['price'] <= 0:
            raise forms.ValidationError('Price must be greater than zero')
        return self.cleaned_data['price']
