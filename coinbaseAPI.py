import requests

class Request():
    def __init__(self, currency1, currency2):
        self.currency1 = currency1
        self.currency2 = currency2
    
    def get_buy(self):
        endpoint = f"https://api.coinbase.com/v2/prices/{self.currency1}-{self.currency2}/buy"
        response = requests.get(endpoint)
        buy_price = response.json()['data']['amount']
        return buy_price
    
    def get_sell(self):
        endpoint = f"https://api.coinbase.com/v2/prices/{self.currency1}-{self.currency2}/sell"
        response = requests.get(endpoint)
        sell_price = response.json()['data']['amount']
        return sell_price

