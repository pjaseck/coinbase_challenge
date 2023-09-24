from coinbase.api import Request
from cli.output import Output
from cli.clear import clear_console
import time
import platform

# TODO: PyInstaller to create executable?

# Checking operating system
system = platform.system()

def main():
    try:
        prod_id = str(input('Provide product ID (e.g. BTC-USD): ')).upper().strip()
        biggest_diff = 0
        starttime = time.time()
        while True:
            # Request book data from API
            request = Request(prod_id)
            # Initialize Output class
            output = Output(request)
            # Clear console
            clear_console(system)
            print(f'Selected product ID: {prod_id}. Press CTRL+C to change.')
            # Print information regarding best bid and ask and monitor biggest difference between their value
            biggest_diff = output.product_info(biggest_diff)
            # Metrics
            # Print best bid-ask mid-price for given timeslices
            output.mid_price_info(60,300,900)
            # Print forecast of the mid-price in next 60 seconds
            output.forecast_info(60,60)
            time.sleep(5.0 - ((time.time() - starttime) % 5.0))
    except KeyboardInterrupt:
        clear_console(system)
        main()

if __name__ == "__main__":
    main()