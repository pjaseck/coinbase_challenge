from coinbase.obj.product_book import ProductBook
from metrics import Metrics

# TODO: round results?

class Output:
    def __init__(self, request):
        self.request = request

    def product_info(self, biggest_diff):
        prod_book_response = self.request.get_product_book()
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
        print('-----------------------')
        print(f'Book time: {book_time}')
        print('-----------------------')
        print(f'Best bid\nPrice: {best_bid_price}\nAmount: {best_bid_quant}')
        print('-----------------------')
        print(f'Best ask\nPrice: {best_ask_price}\nAmount: {best_ask_quant}')
        print('-----------------------')
        print(f'Biggest observed bid-ask difference: {biggest_diff}')
        return biggest_diff
    
    def mid_price_info(self, *argv):
        print('-----------------------')
        print('Best bid and ask mid-price')
        for arg in argv:
            candles_response = self.request.get_product_candles(arg)
            mid_price = Metrics(candles_response).mid_price()
            minutes = int(arg/60)
            print(f'Last {minutes} min: {mid_price}')

    def forecast_info(self, based, ahead):
        candles_response = self.request.get_product_candles(based)
        forecast = Metrics(candles_response).forecast_av(ahead)
        print('-----------------------')
        print(f'Forecasted mid-price in {ahead} seconds: {forecast}')