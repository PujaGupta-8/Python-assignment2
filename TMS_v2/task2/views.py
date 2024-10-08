from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import Task,TaskAssignment,Comment,Project
from django.contrib.auth.models import User
from .serializers import TaskSerializer,TaskAssignmentSerializer,CommentSerializer,ProjectSerializer,ProjectProgressSerializer
from datetime import datetime
import logging

logger = logging.getLogger(__name__)

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
        
class ProjectProgressViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectProgressSerializer
    
class TaskAssignmentViewSet(viewsets.ModelViewSet):
    queryset = TaskAssignment.objects.all()
    serializer_class = TaskAssignmentSerializer

    def create(self, request, *args, **kwargs):
        try:
            task_id = request.data.get('task')
            user_id = request.data.get('user')
            if task_id and user_id:
                task = Task.objects.get(id=task_id)
                user = User.objects.get(id=user_id)
                if task and user:
                    serializer = self.serializer_class(data=request.data)
                    serializer.is_valid(raise_exception=True)
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                else:
                    return Response({"error": "Invalid task or user ID."}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({"error": "Missing task or user ID."}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            logger.error(f"Error while creating task assignment: {str(e)}")
            return Response({"error": "An error occurred while creating the task assignment."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def destroy(self, request, *args, **kwargs):
        try:
            task_assignment_id = kwargs.get('pk')
            task_assignment = TaskAssignment.objects.get(id=task_assignment_id)

            if task_assignment:
                task_assignment.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            else:
                return Response({"error": "Task assignment not found."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            logger.error(f"Error while deleting task assignment: {str(e)}")
            return Response({"error": "An error occurred while deleting the task assignment."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def create(self, request, *args, **kwargs):
        try:
            task_id = request.data.get('task')
            user_id = request.data.get('user')

            if task_id and user_id:
                task = Task.objects.get(id=task_id)
                user = User.objects.get(id=user_id)

                if task and user:
                    serializer = self.serializer_class(data=request.data)
                    serializer.is_valid(raise_exception=True)
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                else:
                    return Response({"error": "Invalid task or user ID."}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({"error": "Missing task or user ID."}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            logger.error(f"Error while creating comment: {str(e)}")
            return Response({"error": "An error occurred while creating the comment."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def destroy(self, request, *args, **kwargs):
        try:
            comment_id = kwargs.get('pk')
            comment = Comment.objects.get(id=comment_id)

            if comment:
                comment.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            else:
                return Response({"error": "Comment not found."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            logger.error(f"Error while deleting comment: {str(e)}")
            return Response({"error": "An error occurred while deleting the comment."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
class TaskCompletionViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def complete(self, request, pk=None):
        try:
            task = self.get_object()
            print(f"Task: {task}")
            if task.status == "COMPLETED":
                return Response({"error": "Task is already completed."}, status=status.HTTP_400_BAD_REQUEST)
            
            if task.status != "IN_PROGRESS":
                return Response({"error": "Only tasks with a status of 'In Progress' can be marked as completed."}, status=status.HTTP_400_BAD_REQUEST)
            
            task.status = "COMPLETED"
            task.completion_time = datetime.now()
            task.save()
            
            serializer = self.serializer_class(task)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            logger.error(f"Error while completing task: {str(e)}", exc_info=True)
            return Response({"error": "An error occurred while completing the task."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
class OverdueTasksViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def list(self, request, *args, **kwargs):
        try:
            today = datetime.now().date()
            overdue_tasks = self.queryset.filter(due_date=today)
            serializer = self.serializer_class(overdue_tasks, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            logger.error(f"Error while retrieving overdue tasks: {str(e)}")
            return Response({"error": "An error occurred while retrieving overdue tasks."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)