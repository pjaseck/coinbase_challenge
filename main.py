from coinbase.api import Request
from cli.output import Output
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
        # Print forecast of the mid-price in next 60 seconds
        output.forecast_info(60,60)
        time.sleep(5.0 - ((time.time() - starttime) % 5.0))

if __name__ == "__main__":
    main()