import numpy
def ext_featr(train,dict):
    featr_matrix=numpy.zeros((len(train),2000))
    mail_no=0
    for mail in train:
        with open(mail) as m:
            lin = m.read()
            words = lin.split()
            for word in words:
                word_no=-1
                for i,(key,value) in enumerate(dict):
                    if key==word:
                        word_no=i
                        featr_matrix[mail_no,word_no]=words.count(word)
            mail_no+=1
    return featr_matrix

