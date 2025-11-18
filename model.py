# api key: SEQVX6VQdMZc1S3OGKuw67iynLkLlB0y
# model.py
import requests

# model.py
# NOTE: move your API key to an environment variable APILAYER_KEY

import os
import requests
from typing import Iterable, List

class CurrencyModel:
    API_KEY = "SEQVX6VQdMZc1S3OGKuw67iynLkLlB0y"
    API_URL = "https://api.apilayer.com/exchangerates_data/convert"

    @staticmethod
    def convert_currency(amount: float, from_c: str, to_currencies: Iterable[str]) -> List[str]:
        if not CurrencyModel.API_KEY:
            return ["Error: Missing APILAYER_KEY environment variable"]

        headers = {"apikey": CurrencyModel.API_KEY}
        msgs: List[str] = []

        for to_currency in to_currencies:
            try:
                params = {"to": to_currency, "from": from_c, "amount": amount}
                resp = requests.get(CurrencyModel.API_URL, headers=headers, params=params, timeout=10)
                resp.raise_for_status()
                data = resp.json()
                result = data.get("result")
                if result is None:
                    msgs.append(f"Error: Invalid API response for {to_currency}")
                else:
                    msgs.append(f"{amount} {from_c} = {result} {to_currency}")
            except requests.exceptions.RequestException as e:
                msgs.append(f"Error: request failed for {to_currency}: {e}")

        return msgs
