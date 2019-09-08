import os
import re
from stop_words import get_stop_words
from pathlib import Path
from nltk.stem import PorterStemmer
from urllib.parse import urlparse
stop_words = get_stop_words('english')
data_dir = Path('/Users/harsh/PycharmProjects/spam_classifier/data')
emails = [os.path.join(data_dir, f) for f in os.listdir(data_dir)]
print(emails[2892])
k=Path('/Users/harsh/PycharmProjects/spam_classifier/data/spmsgc147.txt')
with open(k) as m:
    lin = m.read()
    words = lin.split()
    i=0
    while i<len(words):
        words[i] = re.sub('(http|https)://[^\s]*', 'httpaddr', words[i])
        words[i]=PorterStemmer().stem(words[i])
        if words[i]  in stop_words:
            del words[i]
            i-=1
        elif words[i].isdigit():
            words[i]='number'
        elif words[i].isalnum()==False:
            del words[i]
            i-=1
        i+=1
print(words)
with open(k, 'w') as m:
    for w in words:
        m.write(" " + w)