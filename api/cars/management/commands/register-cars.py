from django.core.management.base import BaseCommand
from cars.models import Car


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write('Creating cars...')

        cars = [{"name": "Audi A3", "plate": "AAA-111"}, {"name": "Chevrolet Cruze", "plate": "BBB-222"}, {"name": "Peugeot 208", "plate": "CCC-333"}, {"name": "Peugeot 308", "plate": "DDD-444"},  {"name": "Ford Mondeo", "plate": "EEE-555"},
                {"name": "Toyota Corolla", "plate": "FFF-666"}, {"name": "Toyota Etios", "plate": "GGG-777"}, {"name": "Toyota Rav4", "plate": "HHH-888"}, {"name": "Gol Trend", "plate": "III-999"}, {"name": "Toyota Hilux", "plate": "JJJ-000"}]

        Car.objects.bulk_create([Car(**car) for car in cars])
        self.stdout.write(self.style.SUCCESS('Cars created!'))
