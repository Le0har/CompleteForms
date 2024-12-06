from rest_framework.test import APITestCase
from forms.models import Form
from django.urls import reverse
from rest_framework import status


class FormTestCase(APITestCase):

    def setUp(self):
        forms = [
            {
                'name': 'ShortForm',
                'email': 'first@mail.hop',
                'phone': '+7 999 111 11 111'
            },
            {
                'name': 'MediumForm',
                'email': 'second@mail.hop',
                'phone': '+7 999 222 22 22',
                'data': '2022-02-02'
            },
            {
                'name': 'LongForm',
                'email': 'third@mail.hop',
                'phone': '+7 999 333 33 33',
                'data': '2023-03-03',
                'text': 'Простота — высшая степень искусства.'
            }
        ]
        for form in forms:
            Form.objects.create(**form)

    def test_ok_shot_form(self):
        res_short = self.client.post(reverse('form-get-form'), {'email': 'nikita@mail.hop', 
                                                                'phone': '+7 999 211 12 14'})
        self.assertEqual(res_short.status_code, status.HTTP_200_OK)
        self.assertEqual(res_short.data['form_name'], 'ShortForm')

    def test_ok_midium_form(self):
        res_midium = self.client.post(reverse('form-get-form'), {'email': 'valera@mail.hop', 
                                                                'phone': '+7 999 311 12 14',
                                                                'data': '2023-02-02'})
        self.assertEqual(res_midium.status_code, status.HTTP_200_OK)
        self.assertEqual(res_midium.data['form_name'], 'MediumForm')

    def test_ok_long_form(self):
        res_midium = self.client.post(reverse('form-get-form'), {'email': 'ищкшы@mail.hop', 
                                                                'phone': '+7 899 311 12 14',
                                                                'data': '2017-02-02',
                                                                'text': 'Движение - жизнь!'})
        self.assertEqual(res_midium.status_code, status.HTTP_200_OK)
        self.assertEqual(res_midium.data['form_name'], 'LongForm')

    def test_ok_unknown_form(self):
        res_short = self.client.post(reverse('form-get-form'), {'noemail': 'nikita@mail.hop', 
                                                                'phone': '+7 999 211 12 14'})
        self.assertEqual(res_short.status_code, status.HTTP_200_OK)
        self.assertEqual(res_short.data['form_name'], 'Unknown')