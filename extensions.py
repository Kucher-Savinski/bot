import requests

from config import keys

class ConvertException(Exception):
    pass

class CryptoConverter:
    @staticmethod
    def convert(base: str, quote: str, amount: str) -> object:

        if quote == base:
            raise ConvertException('Попытка конвертировать одинаковые валюту ' + base)

        try:
            tick = keys[base]
        except KeyError:
            raise ConvertException('Не удалось обработать валюту ' + base)

        try:
            tick = keys[quote]
        except KeyError:
            raise ConvertException('Не удалось обработать валюту ' + quote)

        try:
            amount = float(amount)
        except ValueError:
            raise ConvertException('Неправильно указано количество валюты')

class GetAPI():
    @staticmethod
    def get_price(base: str, quote: str, amount: str):
        r = requests.get('https://min-api.cryptocompare.com/data/price?fsym=' + keys[base] + '&tsyms=' + keys[quote])
        out = r.json()[keys[quote]] * float(amount)
        result = str(round(out, 3)) if out > 1 else str(out)
        return result