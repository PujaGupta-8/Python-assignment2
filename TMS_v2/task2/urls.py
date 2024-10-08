
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import (
    TaskViewSet,
    TaskAssignmentViewSet,
    TaskCompletionViewSet,
    CommentViewSet,
    OverdueTasksViewSet,
    ProjectViewSet,
    ProjectProgressViewSet
)

router = DefaultRouter()
router.register(r'tasks', TaskViewSet, basename='task')
router.register(r'projects', ProjectViewSet, basename='project')
router.register(r'comments', CommentViewSet, basename='comments')
urlpatterns = [
    path('', include(router.urls)),
    path('tasks/<int:pk>/complete/', TaskCompletionViewSet.as_view({'put': 'complete', 'get': 'complete'}), name='task-complete'),
    path('tasks/<int:pk>/assign/', TaskAssignmentViewSet.as_view({'post': 'create', 'get': 'create'}), name='task-assign'),
    path('tasks/<int:pk>/unassign/', TaskAssignmentViewSet.as_view({'post': 'destroy', 'get': 'destroy'}), name='task-unassign'),
    path('tasks/<int:pk>/comments/', CommentViewSet.as_view({'post': 'create', 'get': 'list'}), name='task-comments'),
    path('tasks/<int:pk>/comments/<int:comment_id>/', CommentViewSet.as_view({'delete': 'destroy'}), name='task-comment-delete'),
    path('tasks/overdue/', OverdueTasksViewSet.as_view({'get': 'list'}), name='task-overdue'),
    path('projects/<int:pk>/progress/', ProjectProgressViewSet.as_view({'get': 'list'}), name='project-progress'),
]