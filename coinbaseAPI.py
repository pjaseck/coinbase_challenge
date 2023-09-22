import requests

class Request():
    def __init__(self, prod_id):
        self.prod_id = prod_id

    def get_book(self):
        endpoint = f"https://api.pro.coinbase.com/products/{self.prod_id}/book"
        response = requests.get(endpoint)
        best_bid_price = response.json()['bids'][0][0]
        best_bid_amount = response.json()['bids'][0][1]
        best_ask_price = response.json()['asks'][0][0]
        best_ask_amount = response.json()['asks'][0][1]
        book_time = response.json()['time']
        return best_bid_price, best_bid_amount, best_ask_price, best_ask_amount, book_time
    
    def get_buy(self):
        endpoint = f"https://api.coinbase.com/v2/prices/{self.prod_id}/buy"
        response = requests.get(endpoint)
        buy_price = response.json()['data']['amount']
        return buy_price
    
    def get_sell(self):
        endpoint = f"https://api.coinbase.com/v2/prices/{self.prod_id}/sell"
        response = requests.get(endpoint)
        sell_price = response.json()['data']['amount']
        return sell_price

