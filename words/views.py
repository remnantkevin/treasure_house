from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from words.models import Word

#def index(request):
#  return HttpResponse("Hello, world!")

# index page of all words
def index(request):
  if len(request.GET) == 0:
    list_of_words = []
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for letter in alpha:
      letter_list = Word.objects.filter(word__istartswith=letter)
      if len(letter_list) > 0:
        list_of_words.append(letter_list)

    context = {"list_of_words": list_of_words}
    return render(request, "words/index.html", context)
  else:
    return render(request, "words/search.html", {"search": request.GET["search"]})
  

def definition(request, word_id):
  context = {"word": get_object_or_404(Word, id=word_id)}
  return render(request, "words/definition.html", context)