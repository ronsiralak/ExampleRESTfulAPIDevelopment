# In books/management/commands/create_example_data.py

from django.core.management.base import BaseCommand
from books.models import Book
from datetime import date

class Command(BaseCommand):
    help = 'Creates example book data'

    def handle(self, *args, **options):
        Book.objects.create(title="Example Book 1", author="Author 1", publication_date=date(2020, 1, 1), isbn="1234567890123")
        Book.objects.create(title="Example Book 2", author="Author 2", publication_date=date(2019, 5, 15), isbn="9876543210987")
        self.stdout.write(self.style.SUCCESS('Example data created successfully'))
