import requests
from pprint import pprint

#'key': '75426d6d32bb0fed982b76d2b36fb13278421fa1'

def client():
    
    token = 'Token 75426d6d32bb0fed982b76d2b36fb13278421fa1'
    
    headers = {
         'Authorization' : token,
    }
    
    credentials = {
        'username': 'arife',
        'password': 'musab2010',
    }

    response = requests.get(
        url='http://127.0.0.1:8000/api/kullanici-profilleri/',
        headers=headers,
    )

    print ('Status Code: ',response.status_code)
    response_data = response.json()

    pprint (response_data)
 
if __name__ == '__main__':
     client()