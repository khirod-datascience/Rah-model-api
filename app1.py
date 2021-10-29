# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 12:21:00 2021

@author: Devdarshan
"""

from flask import Flask, request
from flask_restful import Resource, Api
import search_by_definition
app = Flask(__name__)
api = Api(app)

class predict(Resource):
    def get(self, query):
        return {'data': search_by_definition.manual_predict(query)}

api.add_resource(predict, '/<query>')

if __name__ == '__main__':
     app.run()