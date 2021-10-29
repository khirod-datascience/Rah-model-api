# -*- coding: utf-8 -*-
"""
Created on Thu Sep 30 13:49:35 2021

@author: Devdarshan
"""

import pandas as pd
from nltk.corpus import stopwords
from fuzzywuzzy import fuzz

#import spacy
#nlp = spacy.load("en_core_sci_lg")


def search_by_definition_fuzzy_wuzzy(query):
    df = pd.read_csv("D:/COEAI/RAH/datasets/archive/mtsamples.csv")
    df = df.dropna()
    df=df.reset_index()
    
    descriptions = df["description"].tolist()
    
    
    #query = "laproscopy"
    
    
    filtered_query = [word for word in query.split() if word not in stopwords.words('english')]
    medical_specialty = []
    similar = []
    #sim = pd.DataFrame()
    #sim["medical_specialty"]=[]
    #sim["similarity"]=[]
    
    
    for item in range(len(descriptions)):
    
            similarity = fuzz.token_set_ratio(str(filtered_query).lower(),descriptions[item])
            #sim.append(similarity)
            medical_specialty.append(df["medical_specialty"][item])
            similar.append(similarity)
            #sim=sim.append({"medical_specialty":df["medical_specialty"][item], "similarity":similarity}, ignore_index=True)
            #sim=sim.append({"similarity":similarity}, ignore_index=True)
                #print(df["medical_specialty"][item])
    
    sim = pd.DataFrame(list(zip(medical_specialty, similar)), columns=["medical_specialty","similarity"])
    sim=sim.sort_values(by=['similarity'], ascending=False)
    sim.drop_duplicates(subset ="medical_specialty",
                         keep = "first", inplace = True)
    sim=sim.reset_index()
    results=[]
    for i in range(len(sim)):
        if sim["similarity"][i]==sim["similarity"][0]:
            results.append(sim["medical_specialty"][i])
        else:
            break
    return results


#search_by_definition_fuzzy_wuzzy("laproscopy")