import factory                         #for generating demo data
from .models import Todo

class TodoFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Todo

    title = factory.Faker('sentence', nb_words=4)
    details = factory.Faker('paragraph', nb_sentences=3)
    completed = factory.Faker('boolean')
