import re
from collections import Counter

MALE_REFERENCES = ['him', 'his', 'he']

FEMALE_REFERENCES = ['her', 'she']

def get_input():
    no_char = int(raw_input())

    characters = [raw_input() for i in xrange(no_char)]
    
    return characters

def get_corpus():
     return open('corpus.txt')

characters = get_input()
corpus = get_corpus().readlines()

store = {k:[] for k in characters}
for line in corpus:
    for char in characters:
        if char in line:
            store[char].append(line.strip())


for k, v in store.items():
    line_split = " ".join(v).split(" ")
    counts = Counter(line_split)
    male_score = sum(map(lambda _ : counts.get(_,0), MALE_REFERENCES))
    female_score = sum(map(lambda _ : counts.get(_,0), FEMALE_REFERENCES))
    if male_score > female_score:
        print "Male"
    else:
        print "Female"
