import os
from stop_words import get_stop_words
from nltk.stem import PorterStemmer
import re
def process(data_dir):
    emails = [os.path.join(data_dir, f) for f in os.listdir(data_dir)]
    stop_words = get_stop_words('english')
    for mail in emails:
        lines=[]
        with open(mail) as m:
            for line in m:
                lines.append(line.lower())
        with open(mail,'w') as m:
            m.writelines(lines)
        with open(mail) as m:
            lin=m.read()
            words=lin.split()
            i = 0
            while i < len(words):
                words[i] = re.sub('(http|https)://[^\s]*', 'httpaddr', words[i])
                words[i] = re.sub('[^\s]+@[^\s]+', 'emailaddr', words[i])
                words[i] = re.sub( '[$]+', 'dollar', words[i])
                words[i] = PorterStemmer().stem(words[i])
                if words[i] in stop_words:
                    del words[i]
                    i -= 1
                elif words[i].isdigit():
                    words[i] = 'number'
                elif words[i].isalpha() == False:
                    del words[i]
                    i -= 1
                if (len(words[i])==1):
                    del words[i]
                    i-=1
                i += 1
        with open(mail, 'w') as m:
            for w in words:
                m.write(" " + w)