from rest_framework import viewsets, generics
from escola.models import Aluno, Curso, Matricula
from escola.serializer import AlunoSerializer, CursoSerializer, MatriculaSerializer, ListaMatriculaSerializer, AlunoSerializerV2
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions

class AlunoViewSet(viewsets.ModelViewSet):
    """Exibindo todos os alunos e alunas"""
    queryset = Aluno.objects.all()
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated, DjangoModelPermissions]
    def get_serializer_class(self):
        return AlunoSerializerV2 if self.request.version == 'v2' else AlunoSerializer
    
class CursoViewSet(viewsets.ModelViewSet):
    """Exibindo todos os cursos"""
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
    authentication_classes = [BasicAuthentication, DjangoModelPermissions]
    permission_classes = [IsAuthenticated]
    
class MatriculaViewSet(viewsets.ModelViewSet):
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer
    authentication_classes = [BasicAuthentication, DjangoModelPermissions]
    permission_classes = [IsAuthenticated]
    
class ListaMatriculasAluno(generics.ListAPIView):
    def get_queryset(self):
        return Matricula.objects.filter(aluno_id=self.kwargs['pk'])
    serializer_class = ListaMatriculaSerializer
    authentication_classes = [BasicAuthentication, DjangoModelPermissions]
    permission_classes = [IsAuthenticated]