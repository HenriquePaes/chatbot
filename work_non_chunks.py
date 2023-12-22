import spacy

nlp = spacy.load('pt_core_news_sm')
doc = nlp(u'O deep learning decifra o código de RNAs mensageiros e a potencial codificação de proteínas.')
print(doc)
print('')
for chunk in doc.noun_chunks:
    print("Text: {0} | Texto do noun chunk original.".format(chunk.text))
    print("Root text: {0} | Texto da palavra original que conecta o noun chunk ao resto do parsing.".format(chunk.root.text))
    print("Root dep: {0} | Relação de dependência que conecta a raiz ao head.".format(chunk.root.dep_))
    print("Root head text: {0} | Texto do head raiz do token.".format(chunk.root.head.text))
    print("--------------------------------------------------------------------------------------------------")