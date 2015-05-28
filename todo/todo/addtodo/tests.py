from rest_framework.test import APITestCase
from rest_framework import status

class AddTodo(APITestCase):

    def test_add_todo(self):
        response = self.client.post('/v1/todos/', {})

        self.assertEquals(status.HTTP_201_CREATED, response.status_code, response.data)
