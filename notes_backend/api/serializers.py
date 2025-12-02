from rest_framework import serializers
from .models import Note


class NoteSerializer(serializers.ModelSerializer):
    """
    Serializer for Note model providing validation and serialization.
    """

    class Meta:
        model = Note
        fields = ["id", "title", "content", "created_at", "updated_at"]
        read_only_fields = ["id", "created_at", "updated_at"]

    def validate_title(self, value: str) -> str:
        """
        Ensure the title is not blank or only whitespace.
        """
        if not value or not value.strip():
            raise serializers.ValidationError("Title must not be empty.")
        return value.strip()
