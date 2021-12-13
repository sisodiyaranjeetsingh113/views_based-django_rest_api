from rest_framework.response import Response
from django.shortcuts import render
from django.http.response import JsonResponse
from .models import Task
from .serializers import TaskSerializer
from rest_framework.decorators import api_view
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
@api_view(['GET'])
def taskList(request):
    task=Task.objects.all()
    if task is None:
        JsonResponse("No records")
    else:
      serializer=TaskSerializer(task,many=True)
    return JsonResponse({'result':serializer.data},safe=False)
@api_view(['GET'])
def taskDetail(request,pk):
    task=Task.objects.get(id=pk)
    serializer=TaskSerializer(task,many=True)
    return JsonResponse(serializer.data,safe=False)
@api_view(['POST'])
def taskCreate(request):
    serializer=TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return JsonResponse(serializer.data,safe=False)
@api_view(['POST'])
def taskUpdate(request,pk):
    task=Task.objects.get(id=pk)
    serializer=TaskSerializer(instance=task,data=request.data)
    return JsonResponse(serializer.data,safe=False)
@api_view(['DELETE'])
def taskDelete(request,pk):
    task=Task.objects.get(id=pk)
    serializer=TaskSerializer(task,many=True)
    return JsonResponse("Deleted")