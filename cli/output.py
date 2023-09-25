from tabulate import tabulate

from metrics import Metrics


# TODO: round results?, Metrics output as input?

class Output:
    """
    A class used to provide output to the console.

    Attributes
    ----------
    coinbase_client : class
        CoinbaseClient object
    
    Methods
    -------
    product_info
        Retrieves and displays product book information.  
    mid_price_info
        Retrieves and displays mid-price information.
    forecast_info
        Retrieves and displays forecasted mid-price information.
    """
    def __init__(self, coinbase_client):
        """
        Parameters
        ----------
        coinbase_client : class
            CoinbaseClient object
        """
        self.coinbase_client = coinbase_client

    def product_info(self, biggest_diff):
        """Retrieves and displays product book information.         
        This method fetches data from the product book API endpoint, retrieves processed data using Metrics method
        and prints relevant information to the console.

        Parameters
        ----------
        biggest_diff : float
            The biggest observed bid-ask difference.

        Returns
        -------
        float
            The updated biggest observed bid-ask difference.
        """
        product_data = self.coinbase_client.get_product_book()
        product_dict = Metrics(product_data).product_details()
        book_time = product_dict['book_time']
        best_bid_price = product_dict['best_bid_price']
        best_ask_price = product_dict['best_ask_price']
        best_bid_quant = product_dict['best_bid_quant']
        best_ask_quant = product_dict['best_ask_quant']
        bid_ask_diff = product_dict['bid_ask_diff']

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
    
    def mid_price_info(self, intervals):
        """Retrieve and display mid-price information.
        This method fetches data from the product candles API endpoint, retrieves mid-price using Metrics method
        and prints information to the console.

        Parameters
        ----------
        intervals : list
            a list of time intervals (in seconds) for which the mid-price is calculated
        """

        minutes = []
        mid_prices = []
        display_table = []

        # Get mid-price from each time interval
        for interval in intervals:
            candles_data = self.coinbase_client.get_product_candles(60) # granularity fixed for 60 seconds
            mid_price = Metrics(candles_data).mid_price(interval)
            mid_prices.append(mid_price)
            minutes.append(interval)

        # Transform the data into display_table used for printing
        for mid_price, minutes in zip(mid_prices, minutes):
            display_table.append([minutes, mid_price])

        print('-----------------------')
        print('Best bid and ask mid-price')
        print(tabulate(display_table, headers=['Minutes', 'Mid-price'], floatfmt=".5f"))

    def forecast_info(self, granularity, ahead):
        """Retrieve and display forecasted mid-price information.
        This method fetches data from the product candles API endpoint, retrieves forecasted mid-price using Metrics method
        and prints information to the console.

        Parameters
        ----------
        granularity : int
            an interval of historical candlestick data in seconds
        ahead : int
            the time interval (in seconds) ahead for the forecast
        """
        candles_response = self.coinbase_client.get_product_candles(granularity)
        forecast = Metrics(candles_response).forecast_av(ahead)

        print('-----------------------')
        print(f'Forecasted mid-price in {ahead} seconds: {forecast}')