from django.shortcuts import render
from django.views.generic import ListView
from .models import Textbook


# List all textbooks
class IndexView(ListView):

    model = Textbook
    template_name = 'books/index.html'
    context_object_name = 'books'
    ordering = ['-title']

    def get_queryset(self):

        return Textbook.objects.all()