import spacy

tipos = {
    'PRON': 'pronome',
    'VERB': 'verbo',
    'ADV': 'advérbio',
    'PART': 'particula',
    'NOUN': 'substantivo',
    'DET': 'artigo',
    'AUX': 'auxiliar',
    'ADP': 'adposição',
    'PROPN': 'nome próprio',
    'ADJ': 'adjetivo',
    'PUNCT': 'pontuação',
    'CCONJ': 'conjunção coordenativa',
    'CONJ': 'conjunção',
    'INTJ': 'interjeição',
    'NUM': 'numeral',
    'SCONJ': 'conjunção subordinativa',
    'SYM': 'símbolo',
    'X': 'outros',
    'SPACE': 'espaço'
}

# load the model in portuguese
nlp = spacy.load("pt_core_news_sm")

# input the phrase to the model
doc = nlp(input('Digite uma frase: '))

# read the results
for token in doc:
    print("TEXT={0} | LEMMA={1} | POS={2} | TAG={3} | DEP={4} | SHAPE={5} | ALPHA={6} | STOP={7}".format(token.text, token.lemma_, tipos[token.pos_], token.tag_, token.dep_, token.shape_, token.is_alpha, token.is_stop))