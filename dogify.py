#by sghose ~ github.com/RONNCC
import nltk as nk
from random import choice
from numpy import unique

def get_prefix():
    return choice(['so','such','much'])

with open('article.txt','r') as f:
    text = nk.word_tokenize(f.read())

tagged_adjs = unique([' '.join([get_prefix(),x]) for
                (x,y) in nk.pos_tag(text) if y == 'NN'])
print tagged_adjs
