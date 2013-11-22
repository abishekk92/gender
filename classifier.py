import re
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
            store[char].append(line)

print store
#for char in characters:
#    occurences = re.findall(char+".*$", corpus, re.MULTILINE)
#    print len(occurences)
