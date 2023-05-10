from rest_framework.generics import ListAPIView,ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
from .models import Task
from .serializers import TaskSerializers
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime




# generics view

# class TaskallApiView(ListCreateAPIView):
#     queryset = Task.objects.all()
#     serializer_class = TaskSerializers



class TaskallApiView(APIView):
    def get(self, request):
        start_time_str = request.query_params.get('start_time')
        end_time_str = request.query_params.get('end_time')

        tasks = Task.objects.all()

        if start_time_str:
            try:
                start_time = datetime.fromisoformat(start_time_str)
                tasks = tasks.filter(start_time__gte=start_time)
            except ValueError:
                return Response("Invalid start_time format. Use ISO 8601 format.", status=status.HTTP_400_BAD_REQUEST)

        if end_time_str:
            try:
                end_time = datetime.fromisoformat(end_time_str)
                tasks = tasks.filter(start_time__lt=end_time)
            except ValueError:
                return Response("Invalid end_time format. Use ISO 8601 format.", status=status.HTTP_400_BAD_REQUEST)

        serializer = TaskSerializers(tasks, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TaskSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# generics view

# class TaskGrudApiView(RetrieveUpdateDestroyAPIView):
#     queryset = Task.objects.all()
#     serializer_class = TaskSerializers



class TaskCrudApiView(APIView):

    def get(self, request, pk):
        task = Task.objects.get(pk=pk)
        serializer = TaskSerializers(task)
        return Response(serializer.data)


    def put(self, request, pk):
        task = Task.objects.get(pk=pk)
        serializer = TaskSerializers(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        task = Task.objects.get(pk=pk)
        serializer = TaskSerializers(task, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        task = task = Task.objects.get(pk=pk)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class TaskStatusView(APIView):
    def get(self,request,pk):
        task = Task.objects.filter(status=pk)
        serializer = TaskSerializers(task,many=True)
        return Response(serializer.data)