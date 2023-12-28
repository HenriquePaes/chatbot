import spacy

type_entities = {
    'PER':       'Pessoas, inclusive fictícias.',
    'NORP':         'Nacionalidades ou grupos religiosos ou políticos.',
    'FAC':          'Prédios, aeroportos, estradas, pontes etc.',
    'ORG':          'Empresas, agências, instituições etc.',
    'LOC':          'Países, cidades, estados.',
    'MISC':          'Locais, sem classificação geopolítica (non-GPE locations), cordilheiras, cursos d''agua.',
    'PRODUCT':      'Objetos, veículos, alimentos etc. (serviços não).',
    'EVENT':        'Furacões noemados, batalhas, guerras, eventos esportivos etc.',
    'WORK_OF_ART':  'Títulos de livros, canções etc.',
    'LAW':          'Documentos nomeados que viraram leis.',
    'LANGUAGE':     'Qualquer idioma nomeado.',
    'DATE':         'Datas ou períodos absolutos ou relativos.',
    'TIME':         'Períodos de tempo menores que um dia.',
    'PERCENT':      'Percentual, incluindo "%".',
    'MONEY':        'Valores monetários, incluindo a unidade.',
    'QUANTITY':     'Medidas, como o peso ou a distância.',
    'ORDINAL':      '"primeiro", "segundo" etc.',
    'CARDINAL':     'Numerais que não se enquadram em outro tipo.'
}

nlp = spacy.load('pt_core_news_sm')
doc = nlp(input('Digite uma frase: '))

for ent in doc.ents:
    print("{0}: {1} = {2}".format(ent.text, ent.label_, type_entities[ent.label_]))