import requests
from pprint import pprint

#'key': '75426d6d32bb0fed982b76d2b36fb13278421fa1'

def client():
    credentials = {
        'username': 'arife',
        'password': 'musab2010',
    }

    response = requests.post(
        url='http://127.0.0.1:8000/api/rest-auth/login/',
        data= credentials,
    )

    print ('Status Code: ',response.status_code)
    response_data = response.json()

    pprint (response_data)
 
if __name__ == '__main__':
     client()