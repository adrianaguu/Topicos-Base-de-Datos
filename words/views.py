from django.shortcuts import render
from .forms import PhraseForm
from nltk.stem import SnowballStemmer
from es_lemmatizer import lemmatize
import spacy


def index(request):
	if request.method == 'POST':
		form = PhraseForm(request.POST)
		print(request.POST)
		if form.is_valid():

			if 'lemas' in request.POST:
				nlp = spacy.load("es")
				nlp.add_pipe(lemmatize, after="tagger")
				phrase = form.cleaned_data['phrase']
				words = ""
				for token in nlp(phrase):
					words += token.lemma_ + " "
				form.cleaned_data['convertedphrase']=words
				new_form = PhraseForm(form.cleaned_data)
				return render(request, 'index.html', {'form': new_form})

			else:
				spanish_stemmer = SnowballStemmer('spanish')
				list_words = form.cleaned_data['phrase'].split(' ')
				phrase=""
				for word in list_words:
					phrase += spanish_stemmer.stem(word) + ' '

				form.cleaned_data['convertedphrase']= phrase
				new_form = PhraseForm(form.cleaned_data)
				return render(request, 'index.html', {'form': new_form})

	else:
		form = PhraseForm()

	return render(request, 'index.html', {'form': form})