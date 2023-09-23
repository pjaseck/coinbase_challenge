from obj.order import Order

class ProductBook:
    """
    A class used to represent a product book.

    Attributes
    ----------
    bids : array
        a list containing best bid details (price, quantity and count)
    asks : array
        a list containing best bid details (price, quantity and count)
    sequence : str
        unique number for the order book response
    time : str
        product book time

    Methods
    -------
    from_json
        Converts response in json file into callable ProductBook object.

    """
    def __init__(self, bids, asks, sequence, time):
        """
        Parameters
        ----------
        bids : array
            a list containing best bid details
        asks : array
            a list containing best bid details
        sequence : str
            unique number for the order book response
        time : str
            product book time
        """
        self.bids = bids
        self.asks = asks
        self.sequence = sequence
        self.time = time
    
    @staticmethod
    def from_json(json_data):
        """Converts response in json file into callable ProductBook object.

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
