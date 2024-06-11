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

def display_currencies():
    data = get_currencies()
    print('\n\n')
    for a in data:
        currency_data = a[1]
        short = a[0]
        symbol = currency_data['symbol']
        name = currency_data['name']
        print(f'{short} - {name} - {symbol}')
    print('\n\n')
def get_user_currency_input():
    base_currency = input('enter base currency shortcut (E.g USD): ')
    currency_to_convert_to = input('enter the currency to convert to: ')
    return base_currency, currency_to_convert_to

def get_exchange_rate(base_currency, currency):
    convert_url = f'https://api.freecurrencyapi.com/v1/latest?apikey={API_KEY}&base_currency={base_currency}&currencies={currency}'
    response = requests.get(convert_url).json()
    rate = response['data'][currency]
    return rate
def convert_currencies(base_currency, currency, amount):
    rate = get_exchange_rate(base_currency=base_currency, currency=currency)
    result: float = amount * rate
    print(f'\n\n{amount} {base_currency} ==> {round(result, 2)} {currency}\n\n')


def currency_converter():
    base_currency, currency_to_convert_to = get_user_currency_input()
    amount = float(input('enter the amount of money in base currency: '))
    return convert_currencies(base_currency, currency_to_convert_to, amount)

def menu():
    while True:
        print('------Currency Converter--------')
        print('1. List of all currencies\n2. Convert currency\n3. currency exchange rate\nq - quit')
        option = input('Choose option (1-3): ')
        match option:
            case "q":
                break
            case "1":
                display_currencies()
                pass
            case "2":
                currency_converter()
                pass
            case "3":
                base_currency, currency = get_user_currency_input()
                rate = get_exchange_rate(base_currency, currency)
                print(f'\n\n{base_currency} ---> {currency} exchange rate: {rate}\n\n')
def main():
    menu()


if __name__ == '__main__':
    main()

