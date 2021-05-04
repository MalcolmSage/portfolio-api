from rest_framework import viewsets, filters, generics, permissions
from rest_framework.views import APIView
from .models import Project
from .serializers import ProjectSerializer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

# Create your views here.
class ProjectList(generics.ListAPIView):

    serializer_class = ProjectSerializer
    queryset = Project.objects.all()

class ProjectDetail(generics.RetrieveAPIView):

    serializer_class = ProjectSerializer

    def get_object(self, queryset=None, **kwargs):
        item = self.kwargs.get('pk')
        return get_object_or_404(Project, slug=item)


class ProjectCreate(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class ProjectEdit(generics.UpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()

class ProjectDelete(generics.RetrieveDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()