
# model.py
import os, requests

class CurrencyModel:
    API_KEY = "SEQVX6VQdMZc1S3OGKuw67iynLkLlB0y"
    API_URL = "https://api.apilayer.com/exchangerates_data/convert"

    @staticmethod
    def convert_currency(amount: float, from_c: str, to_currencies):
        """

        :param amount: amount to convert e.g. 12.5
        :param from_c: my current currency e.g. EUR
        :param to_currencies: target currency e.g. USD
        :return: array of errors
        """
        headers = {"apikey": CurrencyModel.API_KEY}
        out = []
        for to_currency in to_currencies:
            try:
                resp = requests.get(
                    CurrencyModel.API_URL,
                    headers=headers,
                    params={"to": to_currency, "from": from_c, "amount": amount},
                    timeout=10,
                )
                resp.raise_for_status()
                data = resp.json()
                result = data.get("result", None)
                rate = (data.get("info", {}) or {}).get("rate", None)
                if result is None or rate is None:
                    out.append({"error": f"Error: invalid API response for {to_currency}"})
                else:
                    out.append({"target": to_currency, "result": float(result), "rate": float(rate)})
            except requests.exceptions.RequestException as e:
                out.append({"error": f"Error: request failed for {to_currency}: {e}"})
        return out

