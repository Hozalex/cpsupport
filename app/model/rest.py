from app.model.apiService import *
import json
import requests


class Rest(ApiService):
    url = 'https://sd.cpsupport.ru'
    issues = '/api/v1/issues/120/attachments/656945'
    company = '/api/v1/companies/'
    token = {'api_token': 'f51f7d713e28f37aecb37bfb99e600ce1448d2df'}

    def post(self):
        pass

    def get(self):
        response = requests.get(self.url + self.company, params=self.token)
        print(response)
        return response.json()
