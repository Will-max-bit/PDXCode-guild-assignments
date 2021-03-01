import requests
import json
from datetime import datetime

response = requests.get('http://www.codewars.com/api/v1/users/Will-max-bit/code-challenges/completed?page=0', headers={'Authorization': 'Token token="-"'})
response_data = response.json()





data = response_data['data']
def code_wars(api):
    for datum in data:
        chal_name = datum['name']
        lan_name = datum['completedLanguages']
        language = "".join(lan_name)
        date = datum['completedAt'][:10]    
        day = datetime.strptime(date, '%Y-%m-%d')
        print(f'{chal_name} written in {language} on {day}')
    
#print(data)

print(code_wars(data))