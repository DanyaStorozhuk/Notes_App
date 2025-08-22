from django.urls import path
from notes.views import NoteListViews, NoteDetailView, add_note

urlpatterns = [
    path('', NoteListViews.as_view(), name="home"),  # тепер головна сторінка працює
    path('note-list/', NoteListViews.as_view(), name="note-list"),
    path('notes/<int:pk>/', NoteDetailView.as_view(), name="note-detail"),
    path('notes-add/', add_note, name="add-note"),
]