from django.urls import path
from .views import health, NoteListCreateView, NoteRetrieveUpdateDestroyView

urlpatterns = [
    path('health/', health, name='Health'),
    path('notes/', NoteListCreateView.as_view(), name='notes-list-create'),
    path('notes/<int:id>/', NoteRetrieveUpdateDestroyView.as_view(), name='notes-detail'),
]
