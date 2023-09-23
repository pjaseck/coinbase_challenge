from obj.candle import Candle
from py_linq import Enumerable
from statsmodels.tsa.statespace.sarimax import SARIMAX
import pandas as pd

class Metrics:
    def __init__(self, data):
        self.data = data

    def mid_price(self):
        candles = [Candle.from_json(data) for data in self.data]
        candles_av = Enumerable(candles).avg(lambda x: (x.low + x.high)/2)
        return candles_av
    
    def forecast_av(self, forecast_time):
        df = pd.DataFrame(self.data, columns=['timestamp', 'low', 'high', 'open', 'close', 'volume'])
        df['timestamp'] = pd.to_datetime(df['timestamp'], unit='s')
        df['mid-price'] = (df['low'] + df['high'])/2
        df = df.sort_values(by=['timestamp'], ascending=True)
        fit1 = SARIMAX(df['mid-price'], order=(2, 1, 4),seasonal_order=(0,1,1,7)).fit(disp=0)
        df_pred = fit1.forecast(steps=forecast_time)
        array = df_pred.to_numpy()
        return array[-1]

    def forescast_error(self):
        pass
