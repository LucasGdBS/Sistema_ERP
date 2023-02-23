from django import forms

from erp.models import Funcionario

# class FuncionarioForm(forms.Form):
#     nome = forms.CharField(max_length=20, required=True)
#     sobrenome = forms.CharField(max_length=50, required=True)
#     cpf = forms.CharField(max_length=14, required=True)
#     email = forms.EmailField(max_length=100, required=True)
#     remuneracao = forms.DecimalField(max_digits=7, decimal_places=2, required=True)
# As 2 formas funcionam!

class FuncionarioForm(forms.ModelForm):
    class Meta:
        model = Funcionario
        fields = [
            'nome',
            'sobrenome',
            'cpf',
            'email',
            'remuneracao'
        ]
