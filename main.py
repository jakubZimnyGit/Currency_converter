import requests
from dotenv import load_dotenv
import os
from pprint import PrettyPrinter

load_dotenv()

printer = PrettyPrinter()

API_KEY = os.getenv('API_KEY')
URL = f'https://api.freecurrencyapi.com/v1/currencies?apikey={API_KEY}'

def get_currencies():

    response = requests.get(URL).json()['data']

    response = list(response.items())

    response.sort()
    return response

def display_currencies(data):

    for a in data:
        currency_data = a[1]
        short = a[0]
        symbol = currency_data['symbol']
        name = currency_data['name']
        print(f'{short} - {name} - {symbol}')

def convert_currencies(base_currnecy, currency, amount):
    convert_url = f'https://api.freecurrencyapi.com/v1/latest?apikey={API_KEY}&base_currency={base_currnecy}&currencies={currency}'
    response = requests.get(convert_url).json()
    printer.pprint(response)
    rate = response['data']['EUR']
    result: float = amount * rate
    print(f'{amount} {base_currnecy} ==> {round(result, 2)} {currency}')

def currency_converter():
    base_currency = input('enter base currency shortcut (E.g USD): ')
    amount = float(input('enter the amonut of money in that currency: '))
    currency_to_convert_to = input('enter the currency to convert to: ')
    return convert_currencies(base_currency, currency_to_convert_to, amount)

def main():
    currency_converter()


if __name__ == '__main__':
    main()

