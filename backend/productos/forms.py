from django import forms
from .models import Producto


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'precio', 'descripcion', 'imagen', 'disponible']
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'w-full border rounded-lg px-4 py-2'
            }),
            'precio': forms.NumberInput(attrs={
                'class': 'w-full border rounded-lg px-4 py-2'
            }),
            'descripcion': forms.Textarea(attrs={
                'class': 'w-full border rounded-lg px-4 py-2',
                'rows': 4
            }),
            'imagen': forms.ClearableFileInput(attrs={
                'class': 'w-full'
            }),
        }
