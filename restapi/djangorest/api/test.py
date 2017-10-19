# /api/tests.py

from django.test import TestCase
from .models import Personas
from rest_framework.test import APIClient
from rest_framework import status
from django.core.urlresolvers import reverse

class ModelTestCase(TestCase):
    """Esta clase define el grupo de pruebas para el modelo personas"""


    def setUp(self):
        self.personas_name = "prueba"
        self.personas_edad = "20"
        self.personas = Personas(name=self.personas_name, edad= self.personas_edad)


    def test_model_can_create_a_personas(self):
        """prueba que el modelo pueda crear personas"""
        old_count= Personas.objects.count()
        self.personas.save()
        new_count = Personas.objects.count()
        self.assertNotEquals(old_count, new_count)


class ViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.personas_data = {'name': 'pruebas', 'edad':20}
        self.response = self.client.post(
            reverse('create'),
            self.personas_data,
            format="json")

    def test_api_can_create_a_personas(self):
        """Test the api has bucket creation capability."""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_api_can_get_a_personas(self):
        personas = Personas.objects.get()
        response = self.client.get(
            reverse('details',
            kwargs={'pk': personas.id}), format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, personas)


    def test_api_can_update_a_personas(self):
        change_personas = {'name': 'testing', 'edad':99}
        personas= Personas.objects.get()
        res = self.client.put(
            reverse('details', kwargs={'pk': personas.id}),
            change_personas, format='json'
        )
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_api_can_delete_a_personas(self):
        personas = Personas.objects.get()
        response = self.client.delete(
            reverse('details', kwargs={'pk': personas.id}),
            format='json',
            follow=True)

        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)

#    def test_api_can_get_all_personas(self):
#        personas = Personas.objects.all()
#        response = self.client.get(
#            reverse('personas_all',))
            #serializer = PersonasSerializer(personas, many=True)
#        self.assertEqual(response.status_code, status.HTTP_200_OK)
#        self.assertContains(response, personas)
