from API.coinbaseAPI import Request
from obj.product_book import ProductBook
import time
import os
from datetime import datetime

# User input
# prod_id = str(input('Provide product ID (e.g. BTC-USD): ')).upper()
prod_id = 'BTC-USD'

biggest_diff = 0
starttime = time.time()
while True:
    # Request book data from API
    request = Request(prod_id)
    response = request.get_book()
    # Read data from json
    product_data = ProductBook.from_json(response)
    # Output
    best_bid_price = float(product_data.bids.price)
    best_ask_price = float(product_data.asks.price)
    best_bid_quant = product_data.bids.quantity
    best_ask_quant = product_data.asks.quantity
    book_time = product_data.time
    bid_ask_diff =  best_ask_price - best_bid_price
    if bid_ask_diff > biggest_diff:
        biggest_diff = bid_ask_diff
    os.system('clear')
    print(f'Book time: {book_time}')
    print('-----------------------')
    print(f'Best bid\nPrice: {best_bid_price}\nAmount: {best_bid_quant}')
    print('-----------------------')
    print(f'Best ask\nPrice: {best_ask_price}\nAmount: {best_ask_quant}')
    print('-----------------------')
    print(f'Biggest observed bid-ask difference: {biggest_diff}')
    time.sleep(5.0 - ((time.time() - starttime) % 5.0))
