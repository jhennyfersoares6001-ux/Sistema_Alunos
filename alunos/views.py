from django.shortcuts import render

from django.shortcuts import render, redirect
from .models import Aluno, Curso
from .forms import AlunoForm, CursoForm

def listar_alunos(request):
    alunos = Aluno.objects.all()
    cursos = Curso.objects.all()

    return render(request, 'alunos/listar_alunos.html', {
        'alunos': alunos,
        'cursos': cursos
    })


def cadastrar_aluno(request):
    if request.method == 'POST':
        form = AlunoForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('listar_alunos')
    else:{
  "key": "ctrl+k s",
  "command": "saveAll"
}
    form = AlunoForm()

    return render(request, 'alunos/cadastrar_aluno.html', {
        'form': form
    })

def editar_aluno(request, id):
    aluno = Aluno.objects.get(id=id)

    if request.method == 'POST':
        form = AlunoForm(request.POST, instance=aluno)

        if form.is_valid():
            form.save()
            return redirect('listar_alunos')
    else:
        form = AlunoForm(instance=aluno)

    return render(
        request,
        'alunos/formulario.html',
        {'form': form}
    )

def excluir_aluno(request, id):
    aluno = Aluno.objects.get(id=id)

    if request.method == 'POST':
        aluno.delete()
        return redirect('listar_alunos')

    return render(
        request,
        'alunos/confirmar_exclusao.html',
        {'aluno': aluno}
    )

def cadastrar_curso(request):
    if request.method == 'POST':
        form = CursoForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('listar_cursos')
    else:
        form = CursoForm()

    return render(
        request,
        'alunos/formulario_curso.html',
        {'form': form}
    )


def listar_cursos(request):
    cursos = Curso.objects.all()

    return render(
        request,
        'alunos/listar_cursos.html',
        {'cursos': cursos}
    )

def editar_curso(request, id):
    curso = Curso.objects.get(id=id)

    if request.method == 'POST':
        form = CursoForm(request.POST, instance=curso)

        if form.is_valid():
            form.save()
            return redirect('listar_cursos')
    else:
        form = CursoForm(instance=curso)

    return render(
        request,
        'alunos/formulario_curso.html',
        {'form': form}
    )

def excluir_curso(request, id):
    curso = Curso.objects.get(id=id)

    if request.method == 'POST':
        curso.delete()
        return redirect('listar_cursos')

    return render(
        request,
        'alunos/confirmar_exclusao_curso.html',
        {'curso': curso}
    )

def pagina_inicial(request):
    return render(request, 'inicio/index.html')