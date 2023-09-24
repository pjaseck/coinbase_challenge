class Candle:
    """
    A class used to represent historic rates for a product.

    Attributes
    ----------
    time : str
        time bucket start time
    low : str
        low lowest price during the bucket interval
    high : str
        high highest price during the bucket interval
    open : str
        open opening price (first trade) in the bucket interval
    close : str
        close closing price (last trade) in the bucket interval
    volume : str
        volume volume of trading activity during the bucket interval

    Methods
    -------
    from_json
        Converts response in json file into Candle object.

    """
    def __init__(self, time, low, high, open, close, volume):
        """
        Parameters
        ----------
        time : str
            time bucket start time
        low : str
            low lowest price during the bucket interval
        high : str
            high highest price during the bucket interval
        open : str
            open opening price (first trade) in the bucket interval
        close : str
            close closing price (last trade) in the bucket interval
        volume : str
            volume volume of trading activity during the bucket interval
        """
        self.time = time
        self.low = low
        self.high = high
        self.open = open
        self.close = close
        self.volume = volume
    
    @staticmethod
    def from_json(json_data):
        """Converts response in json file into Candle object.

        Parameters
        ----------
        json_data : list
            A list containing candlestick data in JSON format.

        Returns
        -------
        class
            Candle object
        """
        return Candle(
            json_data[0],
            json_data[1],
            json_data[2],
            json_data[3],
            json_data[4],
            json_data[5]
        )