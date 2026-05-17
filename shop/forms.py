from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Category
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Submit


class ProductForm(forms.ModelForm):

    image = forms.ImageField(
        label='Image',
        required=False,
        widget=CustomClearableFileInput()
    )

    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_method = 'post'
        
        self.fields['category'].queryset = Category.objects.all()

        self.helper.layout = Layout(
            Field('name', css_class='form-control rounded-0'),
            Field('description', css_class='form-control rounded-0'),
            Field('price', css_class='form-control rounded-0'),
            Field('category', css_class='form-select rounded-0'),
            Field('image'),
        )
