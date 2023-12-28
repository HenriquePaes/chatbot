from spacy.lang.pt.stop_words import STOP_WORDS
import spacy

print(STOP_WORDS)
print('Qtd. de palavras: {0}'.format(len(STOP_WORDS)))

# check the word is a stop word
nlp = spacy.load('pt_core_news_sm')
print('A palavra "é" é uma stopword?: {0}'.format(nlp.vocab[u'é'].is_stop))
print('A palavra "oi" é uma stopword?: {0}'.format(nlp.vocab[u'oi'].is_stop))
