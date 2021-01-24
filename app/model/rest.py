from app.model.apiService import *
import json
import requests


class Rest:
    url = 'https://sd.cpsupport.ru'
    issues = '/api/v1/issues/120/attachments/656945'
    company = '/api/v1/companies/'
    id = '44'
    token = {'api_token': ''}
    company_json = None

    def post(self):
        response_post = requests.patch(
            'https://sd.cpsupport.ru/api/v1/companies/44?api_token=',
            data=json.dumps(self.company_json), headers={'Content-Type': 'application/json'})

        print('response post', response_post)

    def get(self):
        response = requests.get(self.url + self.company,
                                params={'api_token': '', 'name': 'Алтекс Софт'})
        self.company_json = response.json()
        self.company_json['additional_name'] = 'Altx-Soft'
        print(response)
        return self.company_json
