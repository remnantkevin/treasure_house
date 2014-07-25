from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from words.models import Word

def index(request):
  return HttpResponse("Hello, world!")

def definition(request, word_id):
  context = {"word": get_object_or_404(Word, id=word_id)}
  return render(request, "words/definition.html", context)