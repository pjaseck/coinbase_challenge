from coinbase.obj.candle import Candle
from py_linq import Enumerable
from statsmodels.tsa.statespace.sarimax import SARIMAX
import pandas as pd
import warnings
from statsmodels.tools.sm_exceptions import ConvergenceWarning
warnings.simplefilter('ignore', ConvergenceWarning)

class Metrics:
    """
    A class used to calculate metrics for based on API responses.

    Attributes
    ----------
    data : json
        response from product candle API

    Methods
    -------
    mid_price
        Calculates average price of the highest bid and lowest ask from product candle response json file.
    forecast
        Forecasts average price of the highest bid and lowest ask from product candle response json file.

    """
    def __init__(self, data):
        """
        Parameters
        ----------
        data : json
            response from product candle API
        """
        self.data = data

    def mid_price(self):
        """Calculates average price of the highest bid and lowest ask from product candle response json file.

        Returns
        -------
        float
            Average price of best bid and best ask.
        """
        candles = [Candle.from_json(data) for data in self.data]
        candles_av = Enumerable(candles).avg(lambda x: (x.low + x.high)/2)
        return candles_av
    
    def forecast_av(self, forecast_time):
        """Forecasts average price of the highest bid and lowest ask from product candle response json file.

        Parameters
        ----------
        forecast_time : int
            seconds from now for which the mid-price is supposed to be forecasted
        
        Returns
        -------
        float
            forecasted value of the mid-price in forecast_time
        """
        df = pd.DataFrame(self.data, columns=['timestamp', 'low', 'high', 'open', 'close', 'volume'])
        df['timestamp'] = pd.to_datetime(df['timestamp'], unit='s')
        df['mid-price'] = (df['low'] + df['high'])/2
        df = df.sort_values(by=['timestamp'], ascending=True)
        df.index = pd.DatetimeIndex(df.index).to_period('M')
        fit = SARIMAX(df['mid-price'], order=(2, 1, 4),seasonal_order=(0,1,1,7)).fit(disp=0)
        prediction = fit.forecast(steps=forecast_time)
        pred_array = prediction.to_numpy()
        return pred_array[-1]

    def forescast_error(self):
        pass