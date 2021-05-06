from .views import ProjectCreate, ProjectDelete, ProjectDetail, ProjectEdit, ProjectList
from rest_framework.routers import DefaultRouter
from django.urls import path, include


app_name = 'project'

# router = DefaultRouter()
# router.register('', ProjectList, basename='project')

urlpatterns = [
    path('', ProjectList.as_view(), name='listproject'),
    path('<str:pk>', ProjectDetail.as_view(), name='detailproject'),
    path('create/', ProjectCreate.as_view(), name='createproject'),
    path('edit/<int:pk>/', ProjectEdit.as_view(), name='editproject'),
    path('delete/<int:pk>/', ProjectDelete.as_view(), name='deleteproject'),
    # path('', include(router.urls)),
]