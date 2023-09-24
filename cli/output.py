from coinbase.obj.product_book import ProductBook
from metrics import Metrics

# TODO: round results?

class Output:
    """
    A class used to provide output to the console.

    Attributes
    ----------
    request : class
        Request object
    
    Methods
    -------
    product_info
        Retrieves and displays product book information.  
    mid_price_info
        Retrieve and display mid-price information.
    forecast_info
        Retrieve and display forecasted mid-price information.
    """
    def __init__(self, request):
        """
        Parameters
        ----------
        request : class
            Request object
        """
        self.request = request

    def product_info(self, biggest_diff):
        """Retrieves and displays product book information.         
        This method fetches data from the product book API endpoint, processes it, and prints relevant information to the console.

        Parameters
        ----------
        biggest_diff : float
            The biggest observed bid-ask difference.

        Returns
        -------
        float
            The updated biggest observed bid-ask difference.
        
        """
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
        """Retrieve and display mid-price information.
        This method fetches data from the product candles API endpoint, calculates the mid-price, and prints it for specified time intervals.

        Parameters
        ----------
        *argv : int
            Variable-length argument list of time intervals (in seconds).
        """
        print('-----------------------')
        print('Best bid and ask mid-price')
        for arg in argv:
            candles_response = self.request.get_product_candles(arg)
            mid_price = Metrics(candles_response).mid_price()
            minutes = int(arg/60)
            print(f'Last {minutes} min: {mid_price}')

    def forecast_info(self, based, ahead):
        """Retrieve and display forecasted mid-price information.
        This method fetches data from the product candles API endpoint, calculates a forecasted mid-price for a specified time ahead,
        and prints the ouput in console.

        Parameters
        ----------
        based : int
            The time interval (in seconds) based on which the forecast is made.
        ahead : int
            The time interval (in seconds) ahead for the forecast.
        """
        candles_response = self.request.get_product_candles(based)
        forecast = Metrics(candles_response).forecast_av(ahead)
        print('-----------------------')
        print(f'Forecasted mid-price in {ahead} seconds: {forecast}')