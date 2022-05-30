import pytest
from datetime import datetime
from django.test import TestCase
from .factories import UserFactory


class UserModelTests(TestCase):
    def setUp(self):
        self.user = UserFactory()

    def test_user_fields(self):
        assert self.user.first_name is not None
        assert self.user.last_name is not None
        assert self.user.username is not None
        assert self.user.email is not None
        assert self.user.is_superuser is False
        assert self.user.is_staff is False
        assert isinstance(self.user.date_joined, datetime)

    def test_user__str__(self):
        repr_user = str(self.user)

        assert self.user.username in repr_user
