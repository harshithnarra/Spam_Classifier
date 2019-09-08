from collections import Counter
def make_dict(train):
    all_words=[]
    for mail in train:
        with open(mail) as m:
            lin = m.read()
            words = lin.split()
            all_words+=words
    dict=Counter(all_words)
    dict=dict.most_common(2000)
    return dict
