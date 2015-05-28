from todo.addtodo.serializer import TodoSerializer
from rest_framework.generics import ListCreateAPIView


class TodoView(ListCreateAPIView):
    serializer_class = TodoSerializer


