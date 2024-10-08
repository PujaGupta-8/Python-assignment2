from rest_framework import serializers
from .models import Task,Project,TaskAssignment,Comment

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'
class TaskAssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskAssignment
        fields = '__all__'
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
class ProjectProgressSerializer(serializers.ModelSerializer):
    progress = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = ('id', 'name', 'progress')

    def get_progress(self, obj):
        total_tasks = obj.tasks.count()
        completed_tasks = obj.tasks.filter(status="Completed").count()
        progress = (completed_tasks / total_tasks) * 100 if total_tasks > 0 else 0
        return progress