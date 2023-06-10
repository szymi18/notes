from django.shortcuts import render, redirect, get_object_or_404

from notesApp.models import Note
from .forms import NoteForm


def note_list(request):
    notes = Note.objects.all()
    return render(request, 'notes/note_list.html', {'notes' : notes})

def note_create(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.author = request.user
            note.save()
            return redirect('note_detail', pk=note.pk)
        else:
            form = NoteForm()
        return render(request, 'notes/note_form.html', {'form' : form})


def note_detail(request, pk):
    note = get_object_or_404(Note, pk=pk)
    return render(request, 'notes/note_detail.html', {'note': note})

def note_edit(request, pk):
    note = get_object_or_404(Note, pk=pk)
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            note = form.save(commit=False)
            note.author = request.user
            note.save()
            return redirect('note_detail', pk=note.pk)
    else:
        form = NoteForm(instance=note)
    return render(request, 'notes/note_form.html', {'form' : form})
