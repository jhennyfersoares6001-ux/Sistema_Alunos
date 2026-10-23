from django.urls import path
from . import views

urlpatterns = [
    path('', views.pagina_inicial, name='pagina_inicial'),
    path('alunos/', views.listar_alunos, name='listar_alunos'),
    path('alunos/cadastrar/', views.cadastrar_aluno, name='cadastrar_aluno'),
    path('alunos/editar/<int:id>/', views.editar_aluno, name='editar_aluno'),
    path('alunos/excluir/<int:id>/', views.excluir_aluno, name='excluir_aluno'),
    path('cursos/', views.listar_cursos, name='listar_cursos'),
    path('cursos/cadastrar/', views.cadastrar_curso, name='cadastrar_curso'),
    path('cursos/editar/<int:id>/', views.editar_curso, name='editar_curso'),
    path('cursos/excluir/<int:id>/', views.excluir_curso, name='excluir_curso'),
]