from API.coinbaseAPI import Request
from obj.product_book import ProductBook
from obj.candle import Candle
from metrics import Metrics
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
    prod_book_response = request.get_product_book()
    candles_response_60 = request.get_product_candles(60)
    candles_response_300 = request.get_product_candles(300)
    candles_response_900 = request.get_product_candles(900)
    # Read data from json
    product_data = ProductBook.from_json(prod_book_response)
    # Basic output
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
    # Metrics
    # Mid price
    mid_price_60 = Metrics(candles_response_60).mid_price()
    mid_price_300 = Metrics(candles_response_300).mid_price()
    mid_price_900 = Metrics(candles_response_900).mid_price()
    print('-----------------------')
    print(f'Mid price:\n Last 1 min: {mid_price_60} | last 5 min: {mid_price_300} | last 15 min: {mid_price_900}')
    # Forecast
    result = Metrics(candles_response_60).forecast_av(60)
    print(result)
    time.sleep(5.0 - ((time.time() - starttime) % 5.0))
