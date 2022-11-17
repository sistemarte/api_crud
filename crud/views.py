from rest_framework.response import Response
from rest_framework.decorators import api_view
from crud import serializers
##My imports
from .models import Task
from .serializers import TaskSerializer

@api_view(['GET'])
def getTask(request):
    task = Task.objects.all()
    serializer = TaskSerializer(task, many=True)
    return Response(serializer.data)

    
@api_view(['POST'])
def postTask(request):
    data = request.data
    task = Task.objects.create(
        description = data['description'],
        date_limited = data['date_limited'],
        asignado_a = data['asignado_a'],
        prioridad = data['prioridad']
    )
    serializer = TaskSerializer(task, many=False)
    return Response(serializer.data)

@api_view(['PUT'])
def putTask(request, pk):
    data= request.data
    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(instance=task, data=data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteTask(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()
    return Response('Task eliminated')