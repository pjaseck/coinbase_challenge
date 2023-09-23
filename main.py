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
        # Initialize Output class
        output = Output(request)
        # Clear console
        if system in ('Linux','Darwin'): 
            os.system('clear')
        else:
            os.system('cls')
        # Print information regarding best bid and ask and monitor biggest difference between their value
        biggest_diff = output.product_info(biggest_diff)
        # Metrics
        # Print best bid-ask mid-price for given timeslices
        output.mid_price_info(60,300,900)
        # Forecast
        #forecast_60 = Metrics(candles_response_300).forecast_av(60)
        #print('-----------------------')
        #print(f'Forecasted mid-price in 60 seconds: {forecast_60}')
        time.sleep(5.0 - ((time.time() - starttime) % 5.0))

if __name__ == "__main__":
    main()