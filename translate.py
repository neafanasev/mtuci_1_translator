import requests
from header import headers

url = "https://google-translate1.p.rapidapi.com/language/translate/v2"


def get(text, lg):
    if lg == "en":
        payload = {'q': text, 'target': lg, 'source': 'ru'}
        response = requests.request("POST", url, data=payload, headers=headers)
    elif lg == "ru":
        payload = {'q': text, 'target': lg, 'source': 'en'}
        response = requests.request("POST", url, data=payload, headers=headers)
    response = response.text[44:-5]
    return response
