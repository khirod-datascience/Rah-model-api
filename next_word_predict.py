#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 14 12:29:25 2021

@author: devdarshanmishra
"""

from keras.models import load_model
import numpy as np
import pickle
from keras.preprocessing.sequence import pad_sequences

# Load the model and tokenizer

model = load_model('nextword_pred.h5')
tokenizer = pickle.load(open('PickleFiles/tokenizer1.pkl', 'rb'))


def predict_next(query):
  input_text = query.strip().lower()

  encoded_text = tokenizer.texts_to_sequences([input_text])[0]
  pad_encoded = pad_sequences([encoded_text], maxlen=1, truncating='pre')
  #print(encoded_text, pad_encoded)
  for i in (model.predict(pad_encoded)[0]).argsort()[-3:][::-1]:
    pred_word = tokenizer.index_word[i]
    yield pred_word


