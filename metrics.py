from obj.candle import Candle
from py_linq import Enumerable
import pandas as pd

class Metrics:
    def __init__(self, data):
        self.data = data

    def mid_price(self):
        candles = [Candle.from_json(data) for data in self.data]
        candles_av = Enumerable(candles).avg(lambda x: (x.low + x.high)/2)
        return candles_av
    
    def forecast(self):
        pass

    def forescast_error(self):
        pass