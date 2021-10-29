# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 12:21:00 2021

@author: Devdarshan
"""

from flask import Flask, request
from flask_restful import Resource, Api
import search_by_definition
import fuzzy_wuzzy_Search_by_definition
import next_word_predict
app = Flask(__name__)
api = Api(app)

class predict(Resource):
    def get(self, query):
        return {'data': search_by_definition.manual_predict(query)}

class predict_fuzzywuzzy(Resource):
    def get(self, query):
        return {'data': fuzzy_wuzzy_Search_by_definition.search_by_definition_fuzzy_wuzzy(query)}

class predict_nextword(Resource):
    def get(self, query):
        return {'data': next_word_predict.predict_next(query)}


api.add_resource(predict, '/searchByDefinition/<query>')
api.add_resource(predict_fuzzywuzzy, '/fuzzyWuzzySearchByDefinition/<query>')
api.add_resource(predict_nextword, '/predictNextWord/<query>')

if __name__ == '__main__':
     app.run()