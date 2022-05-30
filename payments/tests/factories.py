import datetime
import factory

from faker import Faker

from factory import SubFactory, LazyAttribute
from factory.django import DjangoModelFactory

from ..models import Rate

faker = Faker()


class RateFactory(DjangoModelFactory):
    group = factory.LazyAttribute(lambda _: faker.unique.name())
    rate = factory.LazyAttribute(lambda _: faker.unique.random_int())
    currency = factory.LazyAttribute(lambda _: faker.unique.currency())
    created_at = factory.LazyAttribute(lambda _: datetime.datetime.now(datetime.timezone.utc))

    class Meta:
        model = Rate
