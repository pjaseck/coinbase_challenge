import platform
import time

from cli.clear import clear_console
from cli.output import Output
from coinbase.coinbase_client import CoinbaseClient

# Checking operating system
system = platform.system()
# Time is sec to reload the data
interval = 5

def main():
    try:
        prod_id = str(input('Provide product ID (e.g. BTC-USD): ')).upper().strip() # could be as parameter in CLI input
        biggest_diff_so_far = 0
        starttime = time.time()
        while True:
            # Initialize CoinbaseClient class
            coinbase_client = CoinbaseClient(prod_id)
            # Initialize Output class
            output = Output(coinbase_client) # TODO: could split for Helper to get info from Metrics and Output to pring
            
            # ------- CONSOLE OUTPUT -------
            # Clear console
            clear_console(system)
            print(f'Selected product ID: {prod_id}. Press CTRL+C to change, CTRL+Z to stop the program.')
            # Print information regarding best bid and ask and monitor biggest difference between their value
            biggest_diff_so_far = output.product_info(biggest_diff_so_far)
            # METRICS
            # Print best bid-ask mid-price in last 1,5 and 15 minutes
            output.mid_price_info(intervals=[1,5,15])
            # Print forecast of the mid-price in next 60 seconds based on actual data with 60 seconds granularity
            output.forecast_info(granularity=60,ahead=60)

            time_elapsed = time.time() - starttime
            time_remaining = interval - time_elapsed % interval
            time.sleep(time_remaining)
    except KeyboardInterrupt:
        # Start again to change prod ID if interupted from console (CTRL+C)
        clear_console(system)
        main()

if __name__ == "__main__":
    main()