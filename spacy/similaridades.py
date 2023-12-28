import spacy

nlp = spacy.load('pt_core_news_sm')
doc = nlp(u'carro caminhão google')

for t1 in doc:
    for t2 in doc:
        similarity_perc = int(t1.similarity(t2) * 100)
        print("A palavra {} é {}% semelhante à palavra {}".format(t1.text, similarity_perc, t2.text))