# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 12:11:29 2021

@author: Devdarshan
"""

import re

import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
import pandas as pd
import re
from nltk.tokenize import word_tokenize
import pandas as pd

from sklearn.preprocessing import LabelEncoder

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import model_selection, naive_bayes, svm
from sklearn.metrics import accuracy_score
import pickle
from sklearn.svm import LinearSVC


with open('D:/COEAI/RAH/model.pkl', 'rb') as handle:
    model_svc = pickle.load(handle)  

with open('D:/COEAI/RAH/vectorisation.pkl', 'rb') as handle:
    Tfidf_vect = pickle.load(handle)  
with open('D:/COEAI/RAH/label_encoder.pkl', 'rb') as handle:
    Encoder = pickle.load(handle)  


REPLACE_BY_SPACE_RE = re.compile('[/(){}\[\]\|@,;]') 
BAD_SYMBOLS_RE = re.compile('[^0-9a-z #+_]') # take all words that contain characters other than 0-9,a-z,#,+
STOPWORDS = set(stopwords.words('english'))


def text_prepare(text):

    #text = # lowercase text
    text =text.lower()
    #text = # replace REPLACE_BY_SPACE_RE symbols by space in text
    text = re.sub(REPLACE_BY_SPACE_RE, ' ', text)
    #text = # delete symbols which are in BAD_SYMBOLS_RE from text
    text =  re.sub(BAD_SYMBOLS_RE, '', text)
    #text = # delete stopwords from text
    token_word=word_tokenize(text)
    filtered_sentence = [w for w in token_word if not w in STOPWORDS] # filtered_sentence contain all words that are not in stopwords dictionary
    lenght_of_string=len(filtered_sentence)
    text_new=""
    for w in filtered_sentence:
        if w!=filtered_sentence[lenght_of_string-1]:
             text_new=text_new+w+" " # when w is not the last word so separate by whitespace
        else:
            text_new=text_new+w
            
    text = text_new
    return text
def manual_predict(query):
    #query = input("enter query: ")
    Test_X = []
    Test_X.insert(0,query)
    Test_X = [text_prepare(x) for x in Test_X]
    Test_X_Tfidf = Tfidf_vect.transform(Test_X)
    y_val_predicted_labels_tfidf = model_svc.predict(Test_X_Tfidf)
    y_val_pred_inversed = Encoder.inverse_transform(y_val_predicted_labels_tfidf)
    return y_val_pred_inversed[0]


