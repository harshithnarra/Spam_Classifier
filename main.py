import os
import numpy
from math import floor
from process_mail import process
from dictionary import make_dict
from extract_features import ext_featr
from pathlib import Path
from sklearn.svm import SVC
from random import shuffle
from sklearn.metrics import classification_report, confusion_matrix
data_dir = Path('/Users/harsh/PycharmProjects/spam_classifier/data')
check_dir=Path('/Users/harsh/PycharmProjects/spam_classifier/check')
process(data_dir)
process(check_dir)
emails = [os.path.join(data_dir, f) for f in os.listdir(data_dir)]
check=[os.path.join(check_dir, f) for f in os.listdir(check_dir)]
print(emails)
shuffle(emails)
print(emails)
split_index=floor(len(emails)*0.7)
train=emails[:split_index]
test=emails[split_index:]
print(train)
dict=make_dict(train)
print(dict)
train_featr=ext_featr(train,dict)
train_label=numpy.zeros(len(train))
i=0
for f in train:
    if "spmsg" in f:
        train_label[i]=1
    i+=1
test_featr=ext_featr(test,dict)
test_label=numpy.zeros(len(test))
i=0
j=0
for f in test:
    if "spmsg" in f:
        test_label[i]=1
        j+=1
    i+=1
print(i)
print(j)
model=SVC(kernel='linear')
model.fit(train_featr,train_label)
test_pred=model.predict(test_featr)
print(confusion_matrix(test_label,test_pred))
print(classification_report(test_label,test_pred))
check_featr=ext_featr(check,dict)
check_pred=model.predict(check_featr)
print(check_pred[:])