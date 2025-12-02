from django.core.management.base import BaseCommand
from api.models import Note


class Command(BaseCommand):
    help = "Create a couple of sample notes for testing."

    def handle(self, *args, **options):
        samples = [
            {"title": "Welcome to Simple Notes", "content": "This is your first sample note."},
            {"title": "Second Note", "content": "Feel free to edit or delete me!"},
        ]
        created = 0
        for data in samples:
            obj, was_created = Note.objects.get_or_create(title=data["title"], defaults={"content": data["content"]})
            if was_created:
                created += 1
        self.stdout.write(self.style.SUCCESS(f"Seed complete. Created {created} new notes."))
