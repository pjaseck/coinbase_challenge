from coinbase.api import Request
from cli.output import Output
from metrics import Metrics
import time
import os
import platform

# TODO: PyInstaller to create executable?

system = platform.system()
# User input
# prod_id = str(input('Provide product ID (e.g. BTC-USD): ')).upper()
prod_id = 'BTC-USD'

def main():
    biggest_diff = 0
    starttime = time.time()
    while True:
        # Request book data from API
        request = Request(prod_id)
        candles_response_60 = request.get_product_candles(60)
        candles_response_300 = request.get_product_candles(300)
        candles_response_900 = request.get_product_candles(900)
        # Clear console
        if system in ('Linux','Darwin'): 
            os.system('clear')
        else:
            os.system('cls')
        # Print information regarding best bid and ask and monitor biggest difference between their value
        biggest_diff = Output(request).product_info(biggest_diff)
        # Metrics
        # Mid price
        mid_price_60 = Metrics(candles_response_60).mid_price()
        mid_price_300 = Metrics(candles_response_300).mid_price()
        mid_price_900 = Metrics(candles_response_900).mid_price()
        print('-----------------------')
        print(f'Mid price:\n Last 1 min: {mid_price_60} | last 5 min: {mid_price_300} | last 15 min: {mid_price_900}')
        # Forecast
        forecast_60 = Metrics(candles_response_300).forecast_av(60)
        print('-----------------------')
        print(f'Forecasted mid-price in 60 seconds: {forecast_60}')
        time.sleep(5.0 - ((time.time() - starttime) % 5.0))

if __name__ == "__main__":
    main()