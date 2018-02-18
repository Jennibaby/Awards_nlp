#-*- coding: utf-8 -*-
import nltk
from nameparser.parser import HumanName

def get_product_names(text):
    tokens = nltk.tokenize.word_tokenize(text)
    pos = nltk.pos_tag(tokens)
    sentt = nltk.ne_chunk(pos, binary = False)
    person_list = []
    person = []
    name = ""
    for subtree in sentt.subtrees():
        print(subtree.label())
        print (subtree)
        for leaf in subtree.leaves():
            #print (leaf[0])
            person.append(leaf[0])
        if len(person) > 1: #avoid grabbing lone surnames
            for part in person:
                name += part + ' '
            if name[:-1] not in person_list:
                person_list.append(name[:-1])
            name = ''
        person = []

    return (person_list)

#['#', 'TheShapeofWater', 'wins', 'Best', 'Original', 'Score', 'Full', 'winners', 'list', ':', 'https', ':', '//t.co/IjwywdoJ4e', '#', 'GoldenGlobes', 'https', ':', '//t.co/AynkISUQzp']
text = """
The Handmaid's Tale won best Best Series of Drama. The Shape of Water wins Best Original Score.
Best Series of Drama is The Marvelous Mrs. Maisel.
"""
names = get_product_names(text)
print (names)

print ("\n\n\n")
sentences = nltk.sent_tokenize(text)
tokenized_sentences = [nltk.word_tokenize(sentence) for sentence in sentences]
tagged_sentences = [nltk.pos_tag(sentence) for sentence in tokenized_sentences]
chunked_sentences = nltk.ne_chunk_sents(tagged_sentences, binary=True)

def extract_entity_names(t):
    entity_names = []

    if hasattr(t, 'label') and t.label:
        if t.label() == 'NE':
            entity_names.append(' '.join([child[0] for child in t]))
        else:
            for child in t:
                entity_names.extend(extract_entity_names(child))

    return entity_names

entity_names = []
for tree in chunked_sentences:
    # Print results per sentence
    # print extract_entity_names(tree)

    entity_names.extend(extract_entity_names(tree))

# Print all entity names
#print entity_names

# Print unique entity names
print (set(entity_names))

# # Install: pip install spacy && python -m spacy download en
# import spacy

# # Load English tokenizer, tagger, parser, NER and word vectors
# nlp = spacy.load('en')

# # Process whole documents
# #text = open('customer_feedback_627.txt').read()
# doc = nlp(text)

# # Find named entities, phrases and concepts
# for entity in doc.ents:
#     print(entity.text, entity.label_)

# # Hook in your own deep learning models
# #nlp.add_pipe(load_my_model(), before='parser')

