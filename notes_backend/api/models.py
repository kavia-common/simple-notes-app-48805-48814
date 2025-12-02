from django.db import models


class Note(models.Model):
    """
    Represents a note with a title, content, and auto-managed timestamps.
    """
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True, default="")
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True, db_index=True)

    def __str__(self) -> str:
        return f"{self.title} ({self.pk})"
