import requests
from dotenv import load_dotenv
import os
from pprint import PrettyPrinter

load_dotenv()

printer = PrettyPrinter()

API_KEY = os.getenv('API_KEY')
URL = f'https://api.freecurrencyapi.com/v1/latest?apikey={API_KEY}'

def get_currencies():

    response = requests.get(URL).json()['data']

    response = list(response.items())

    response.sort()
    return response

def display_currencies(data):
    for a in data:
        print(a[0])


def main():
    data = get_currencies()
    display_currencies(data)

if __name__ == '__main__':
    main()

