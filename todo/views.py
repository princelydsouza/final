from django.shortcuts import render

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from todo.models import Todo
from todo.serializers import TodoSerializer

# Create your views here.

@csrf_exempt
def todo_list(request):

	if request.method =='GET':
		todo = Todo.objects.all()
		serializers = TodoSerializer(todo, many=True)
		return JsonResponse(serializers.data, safe=False)

	elif request.method == 'POST':
		data = JSONParser().parse(request)
		serializer = TodoSerializer(data=data)
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data, status=201)
		return JsonResponse(serializer.errors, status=404) 