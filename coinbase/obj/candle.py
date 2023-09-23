class Candle:
    def __init__(self, time, low, high, open, close, volume):
        self.time = time
        self.low = low
        self.high = high
        self.open = open
        self.close = close
        self.volume = volume
    
    @staticmethod
    def from_json(json_data):
        return Candle(
            json_data[0],
            json_data[1],
            json_data[2],
            json_data[3],
            json_data[4],
            json_data[5]
        )