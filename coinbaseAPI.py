import requests

class Request():
    def __init__(self, prod_id):
        self.prod_id = prod_id

    def get_book(self):
        endpoint = f"https://api.pro.coinbase.com/products/{self.prod_id}/book"
        response = requests.get(endpoint).json()
        return response
    
    def get_buy(self):
        endpoint = f"https://api.coinbase.com/v2/prices/{self.prod_id}/buy"
        response = requests.get(endpoint).json()
        return response
    
    def get_sell(self):
        endpoint = f"https://api.coinbase.com/v2/prices/{self.prod_id}/sell"
        response = requests.get(endpoint).json()
        return response

