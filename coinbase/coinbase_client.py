import requests

from coinbase.obj.product_book import ProductBook
from coinbase.obj.candle import Candle

class CoinbaseClient:
    """
    A class used to requests for API responses from Coinbase for a given product ID and convert the response.

    Attributes
    ----------
    prod_id : str
        a product ID representing the trading pair (e.g., 'BTC-USD')
    granularity : int
        an interval of historical candlestick data in seconds, the only accepted values: {60, 300, 900, 3600, 21600, 86400}

    Methods
    -------
    get_product_book
        Provides data from API response for a product book.
    
    get_product_candles
        Provides data from API response for product candles with given granularity.

    """
    def __init__(self, prod_id):
        """
        Parameters
        ----------
        prod_id : str
            a str representing product ID (e.g. BTC-USD)
        """
        self.prod_id = prod_id

    def get_product_book(self):
        """This method sends an HTTP GET request to the Coinbase Pro API's product book
        endpoint for the given trading pair, retrieves the order book data in JSON format,
        and returns the response.

        Returns
        -------
        class
            ProductBook data model
        
        """
        endpoint = f"https://api.pro.coinbase.com/products/{self.prod_id}/book"
        response = requests.get(endpoint)
        if response.status_code == 200:
            product_book_data = ProductBook.from_json(response.json())
            return product_book_data
        else:
            raise Exception(f'Failed to retrieve data from the API. Status code: {response.status_code}')
    
    def get_product_candles(self, granularity):
        """This method sends an HTTP GET request to the Coinbase Pro API's product candles
        endpoint for the given trading pair and granularity, retrieves the candlestick data at level 1
        in JSON format, and returns the response.

        Parameters
        ----------
        granularity : int
            an interval of historical candlestick data in seconds, the only accepted values: {60, 300, 900, 3600, 21600, 86400}
        
        Returns
        -------
        class
            Candle data model
        """
        endpoint = f"https://api.pro.coinbase.com/products/{self.prod_id}/candles?granularity={granularity}"
        response = requests.get(endpoint)
        if response.status_code == 200:
            product_candles_data = [Candle.from_json(bucket) for bucket in response.json()]
            return product_candles_data
        else:
            raise Exception(f'Failed to retrieve data from the API. Status code: {response.status_code}')