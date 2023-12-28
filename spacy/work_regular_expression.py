import spacy
import re

nlp = spacy.load('pt_core_news_sm')

sentence1 = "Compre uma passagem de metrô de estação Pinheiros para a estação Barra Funda."
sentence2 = "Chame um táxi de aeroporto de Congonhas para Cumbica."

from_to = re.compile('.* de (.*) para (.*)')
to_from = re.compile('.* para (.*) de (.*)')

from_to_match = from_to.match(sentence2)
to_from_match = to_from.match(sentence2)

if from_to_match and from_to_match.groups():
    _from = from_to_match.groups()[0]
    _to = from_to_match.groups()[1]
    print("O padrão de_para coincidiu corretamente. Exibindo valores\n")
    print("De: {}, Para: {}".format(_from, _to))