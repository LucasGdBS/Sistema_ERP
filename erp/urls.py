from django.urls import path
from erp.views import atualiza_funcionario, busca_funcionario_por_id, home, cria_funcionario, lista_funcionarios

app_name = 'erp'

urlpatterns = [
    path('', home),
    path('funcionarios/', lista_funcionarios),
    path('funcionarios/novo', cria_funcionario),
    path('funcionarios/detalhe/<pk>', busca_funcionario_por_id),
    path('funcionarios/atualiza/<pk>/', atualiza_funcionario, name='atualiza_funcionario'),
    #path('funcionarios/atualiza/<pk>', atualiza_funcionario)
]
