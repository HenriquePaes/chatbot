import spacy
from spacy import displacy

nlp = spacy.load('pt_core_news_sm')
doc = nlp(u'Reserve um voo de Bangalore à Goa')
blr, goa = doc[4], doc[6]
print(list(blr.ancestors))
print(list(goa.ancestors))

# check item is a ancestors another item
print("{0} é um item ancestral de {1}?: {2}".format(doc[2], doc[6], doc[2].is_ancestor(doc[6])))

doc = nlp(u'Reserve uma mesa no restaurante e o táxi para o hotel')
tasks = doc[2], doc[7] # (mesa, taxi)
tasks_target = doc[4], doc[10] # (restaurante, hotel)

for task in tasks_target:
    for tok in task.ancestors:
        if tok in tasks:
            print("A reserva da(o) {} pertence ao {}.".format(tok, task))

# visualization children
print("Filhos ancestrais de taxi: {0}".format(list(doc[7].children)))

# Using the 'dep' visualizer
displacy.serve(doc, style='dep')