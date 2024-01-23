from django.core.management.base import BaseCommand
from todoApp.factories import TodoFactory

class Command(BaseCommand):
     help = "Generates test data"

     def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Generating demo tasks...'))

        for _ in range(300):
            TodoFactory()

        self.stdout.write(self.style.SUCCESS('Demo tasks generated successfully.'))