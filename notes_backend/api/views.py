from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.permissions import AllowAny
from drf_yasg.utils import swagger_auto_schema

from .models import Note
from .serializers import NoteSerializer


@api_view(['GET'])
def health(request):
    """
    Health check endpoint.

    Returns:
        200 OK with {"message": "Server is up!"}
    """
    return Response({"message": "Server is up!"})


class NoteListCreateView(generics.ListCreateAPIView):
    """
    get:
    List all notes.

    post:
    Create a new note.
    """
    queryset = Note.objects.all().order_by("-created_at")
    serializer_class = NoteSerializer
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_id="listNotes",
        operation_summary="List notes",
        operation_description="Returns a paginated list of notes ordered by creation date descending.",
        responses={200: NoteSerializer(many=True)},
        tags=["notes"],
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_id="createNote",
        operation_summary="Create note",
        operation_description="Creates a new note with a non-empty title and optional content.",
        request_body=NoteSerializer,
        responses={201: NoteSerializer, 400: "Validation error"},
        tags=["notes"],
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class NoteRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    get:
    Retrieve a single note by ID.

    put:
    Replace an existing note.

    patch:
    Partially update a note.

    delete:
    Delete a note by ID.
    """
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = [AllowAny]
    lookup_url_kwarg = "id"
    lookup_field = "id"

    @swagger_auto_schema(
        operation_id="getNote",
        operation_summary="Get note",
        operation_description="Retrieve a single note by its ID.",
        responses={200: NoteSerializer, 404: "Not found"},
        tags=["notes"],
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_id="updateNote",
        operation_summary="Update note",
        operation_description="Update a note by replacing all fields.",
        request_body=NoteSerializer,
        responses={200: NoteSerializer, 400: "Validation error", 404: "Not found"},
        tags=["notes"],
    )
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_id="partialUpdateNote",
        operation_summary="Partial update note",
        operation_description="Partially update fields of a note.",
        request_body=NoteSerializer,
        responses={200: NoteSerializer, 400: "Validation error", 404: "Not found"},
        tags=["notes"],
    )
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_id="deleteNote",
        operation_summary="Delete note",
        operation_description="Delete an existing note.",
        responses={204: "Deleted", 404: "Not found"},
        tags=["notes"],
    )
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)
