from rest_framework.test import APIClient
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework_simplejwt.tokens import RefreshToken
from payments.tests.factories import RateFactory
from ..constants import STANDARD_USER


class LoginViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.credentials = {
            'username': 'test',
            'password': 'test_password'
        }
        cls.client = APIClient()
        cls.rate = RateFactory()
        User.objects.create_user(**cls.credentials)

    @property
    def bearer_token(self):
        # assuming there is a user in User model
        user = User.objects.get(username=self.credentials['username'])
        refresh = RefreshToken.for_user(user)
        return {"HTTP_AUTHORIZATION": f'Bearer {refresh.access_token}'}

    def test_login(self):
        self.user.groups.add(STANDARD_USER)
        response = self.client.post("/user/login", self.credentials, follow=True)
        self.assertEqual(response.status_code, 200)

    # def test_client_authentication(self):
    #     self.client.login(username=self.credentials['login'], password=self.credentials['password'])
    #     user = auth.get_user(self.client)
    #     assert user.is_authenticated
    #
    def test_me(self):
        response = self.client.get("/user/me", **self.bearer_token)
        self.assertEqual(response.status_code, 200)

    # def test_view_uses_correct_template(self):
    #     response = self.client.get(reverse('students'))
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'testing/student_list.html')
    #
    # def test_pagination_is_correct(self):
    #     response = self.client.get(reverse('students'))
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTrue('is_paginated' in response.context)
    #     self.assertTrue(response.context['is_paginated'] is True)
    #     self.assertEqual(len(response.context['student_list']), 10)
