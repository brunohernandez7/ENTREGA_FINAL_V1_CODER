from django import forms

class BlogFormulario(forms.Form):

    titulo = forms.CharField()
    resumen = forms.CharField()
    texto = forms.CharField()
    
