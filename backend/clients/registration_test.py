import requests
from pprint import pprint

#'key': 'e5b033af8d9daecec684076940af3865ed08b594'

def client():
    credentials = { #yeni user
        'username': 'metin',
        'email': 'metin@gmail.com', 
        'password1': 'bekir2015',
        'password2': 'bekir2015',
        'grup': 'Veli',
    }

    response = requests.post(
        url='http://127.0.0.1:8000/api/rest-auth/registration/',
        data= credentials,
    )

    print ('Status Code: ',response.status_code)
    response_data = response.json()

    pprint (response_data)
 
if __name__ == '__main__':
     client()