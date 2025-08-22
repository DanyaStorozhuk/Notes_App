from django.shortcuts import render,redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Note
from .forms import NoteForm
# Create your views here.


def add_note(request):
    # Перевіряємо, чи запит прийшов методом POST (користувач натиснув "Зберегти")
    if request.method == "POST":
        # якщо прийшли дані з форми (користувач натиснув "Зберегти")
        form = NoteForm(request.POST)
        # Перевіряємо, чи форма валідна (користувач правильно заповнив поля)
        if form.is_vaild():
            # Якщо форма правильна, зберігаємо об’єкт у базу даних
            form.save()
            # Після збереження перенаправляємо користувача на список нотаток
            return redirect('note-list')
    else:
        # Якщо запит НЕ POST (наприклад, просто відкрили сторінку),
        # створюємо порожню форму для відображення в шаблоні
        form = NoteForm()
    return render(request, 'notes/add_note.html', {'form': form})


class NoteListViews(ListView):
    model = Note
    template_name = "note_list.html"

class NoteDetailView(DeleteView):
    model = Note
    template_name = "note_detail.html"