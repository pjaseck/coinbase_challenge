import requests

class Request():
    """
    A class used to requests for API responses from Coinbase for a given product ID.

    Attributes
    ----------
    prod_id : str
        a str representing product ID (e.g. BTC-USD)
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
        """Provides API response for a product book at level 1 for a given product ID.

        Returns
        -------
        json
            Json file with the best bid, ask and auction information.
        """
        endpoint = f"https://api.pro.coinbase.com/products/{self.prod_id}/book"
        response = requests.get(endpoint).json()
        return response
    
    def get_product_candles(self, granularity):
        """Provides API response for a product book at level 1 for a given product ID.

        Parameters
        ----------
        granularity : int
            a value of a timeslice of historical rate data, the only accepted values: {60, 300, 900, 3600, 21600, 86400}
        
        Returns
        -------
        json
            Json file with historic rates for a product. 
            Rates are returned in grouped buckets. Candle schema is of the form [timestamp, price_low, price_high, price_open, price_close].
        """
        endpoint = f"https://api.pro.coinbase.com/products/{self.prod_id}/candles?granularity={granularity}"
        response = requests.get(endpoint).json()
        return response