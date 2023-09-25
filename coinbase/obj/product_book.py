from coinbase.obj.order import Order

class ProductBook:
    """
    A class used to represent a product book.

    Attributes
    ----------
    bids : list
        a list containing best bid details (price, quantity and count)
    asks : list
        a list containing best bid details (price, quantity and count)
    sequence : str
        unique number for the order book response
    time : str
        product book time

    Methods
    -------
    from_json
        Converts response in json file into ProductBook object.

    """
    def __init__(self, bids, asks, sequence, time):
        """
        Parameters
        ----------
        bids : list
            a list containing best bid details
        asks : list
            a list containing best bid details
        sequence : int
            unique number for the order book response
        time : datetime
            product book time
        """
        self.bids = bids
        self.asks = asks
        self.sequence = sequence
        self.time = time
    
    @staticmethod
    def from_json(json_data):
        """Converts response in json file into callable ProductBook object.

        Parameters
        ----------
        json_data : dict
            A dictionary containing product book data in JSON format.

        Returns
        -------
        class
            ProductBook object
        """
        bids = Order.from_json(json_data['bids'])
        asks = Order.from_json(json_data['asks'])
        return ProductBook(
            bids,
            asks,
            json_data['sequence'],
            json_data['time']
        )
