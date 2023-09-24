import requests

class Request():
    """
    A class used to requests for API responses from Coinbase for a given product ID.

    Attributes
    ----------
    prod_id : str
        a product ID representing the trading pair (e.g., 'BTC-USD')
    granularity : int
        a value of a timeslice of historical rate data, the only accepted values: {60, 300, 900, 3600, 21600, 86400}

    Methods
    -------
    get_product_book
        Provides API response for a product book.
    
    get_product_candles
        Provides API response for product candles in a given timeslice.

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
        dict
            A dictionary containing the product book data in JSON format.
        
        """
        endpoint = f"https://api.pro.coinbase.com/products/{self.prod_id}/book"
        response = requests.get(endpoint).json()
        return response
    
    def get_product_candles(self, granularity):
        """This method sends an HTTP GET request to the Coinbase Pro API's product candles
        endpoint for the given trading pair and granularity, retrieves the candlestick data at level 1
        in JSON format, and returns the response.

        Parameters
        ----------
        granularity : int
            a value of a timeslice of historical rate data, the only accepted values: {60, 300, 900, 3600, 21600, 86400}
        
        Returns
        -------
        list
            A list containing the candlestick data in JSON format.
            Rates are returned in grouped buckets. Candle schema is of the form [timestamp, price_low, price_high, price_open, price_close].
        """
        endpoint = f"https://api.pro.coinbase.com/products/{self.prod_id}/candles?granularity={granularity}"
        response = requests.get(endpoint).json()
        return response