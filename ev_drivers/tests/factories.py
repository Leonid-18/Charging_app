import datetime
import factory

from faker import Faker

from factory import SubFactory, LazyAttribute
from factory.django import DjangoModelFactory

from django.contrib.auth import get_user_model

faker = Faker()


class UserFactory(DjangoModelFactory):
    first_name = factory.LazyAttribute(lambda _: faker.unique.first_name())
    last_name = factory.LazyAttribute(lambda _: faker.unique.last_name())
    username = factory.LazyAttribute(lambda _: faker.unique.name())
    email = factory.LazyAttribute(lambda _: faker.unique.email())
    password = factory.LazyAttribute(lambda _: faker.password())
    date_joined = LazyAttribute(lambda _: datetime.datetime.now(datetime.timezone.utc))

    class Meta:
        model = get_user_model()



class UserFactoryOnlyEmail(DjangoModelFactory):
    email = factory.Faker("email")

    class Meta:
        model = get_user_model()


class UserFactoryWithPassword(UserFactory):
    password = faker.password()


class UserFactoryVerified(UserFactoryWithPassword):
    email_verified = True
