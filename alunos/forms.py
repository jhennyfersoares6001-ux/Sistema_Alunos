from django import forms
from .models import Aluno, Curso


class AlunoForm(forms.ModelForm):
    curso = forms.ModelChoiceField(
        queryset=Curso.objects.all(),
        empty_label="Selecione uma opção"
    )

    class Meta:
        model = Aluno
        fields = ['nome', 'email', 'curso']


class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['nome', 'descricao']