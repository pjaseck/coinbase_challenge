from obj.candle import Candle
from py_linq import Enumerable

class Metrics:
    def __init__(self, data):
        self.data = data

    def forecast(data):
        pass

    def forecast_error(data):
        pass

    @staticmethod
    def mid_price(json_data):
        candles = [Candle.from_json(data) for data in json_data]
        candles_av = Enumerable(candles).avg(lambda x: (x.low + x.high)/2)
        return candles_av