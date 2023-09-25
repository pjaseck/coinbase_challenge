import time
import warnings

from py_linq import Enumerable
from statsmodels.tools.sm_exceptions import ConvergenceWarning
from statsmodels.tsa.statespace.sarimax import SARIMAX

from coinbase.obj.candle import Candle

warnings.simplefilter('ignore', ConvergenceWarning)

class Metrics:
    """
    A class used to calculate metrics based API responses data models.

    Methods
    -------
    product_details
        Returns best bid and ask information from the product book as a dictionary.
    mid_price
        Calculates average price of the highest bid and lowest ask from product candle data model.
    forecast
        Forecasts average price of the highest bid and lowest ask from product candle data model.

    """

    def product_details(data):
        """Returns best bid and ask information from the product book.

        Parameters
        ----------
        data : class
            response from API as ProductBook object

        Returns
        -------
        dict
            A dictionary containing 'book_time','best_bid_price', 'best_ask_price', 'best_bid_quant', 'best_ask_quant', 'bid_ask_diff' keys.
        """
        return {'book_time':data.time
                ,'best_bid_price':float(data.bids.price)
                ,'best_ask_price':float(data.asks.price)
                ,'best_bid_quant':data.bids.quantity
                ,'best_ask_quant':data.asks.quantity
                ,'bid_ask_diff':float(data.asks.price)-float(data.bids.price)}
    
    def mid_price(data, timeframe):
        """Calculates average price of the highest bid and lowest ask from a product candle.

        Parameters
        ----------
        data : list
            response from API as list of Candle objects
        timeframe : int
            last minutes from which the average price is supposed to be calculated

        Returns
        -------
        float
            Average price of best bid and best ask.
        """
        if timeframe == 1:
            last_candle = data[-1]
            candles_av = (last_candle.high + last_candle.low)/2
        else:
            past_time_point = time.time() - timeframe * 60
            candles_slice = Enumerable(data).where(lambda x: x.time >= past_time_point)
            candles_av = candles_slice.avg(lambda x: (x.low + x.high)/2)
        return candles_av
    
    def forecast_av(data, forecast_time):
        """Forecasts average price of the highest bid and lowest ask from product candle response json file.

        Parameters
        ----------
        data : list
            response from API as list of Candle objects
        forecast_time : int
            seconds from now for which the mid-price is supposed to be forecasted
        
        Returns
        -------
        float
            forecasted value of the mid-price in forecast_time
        """

        candles_ascending = Enumerable(data).order_by(lambda x: x.time)
        av_list = [(candle.high + candle.low)/2 for candle in candles_ascending]
        fit = SARIMAX(av_list, order=(2, 1, 4),seasonal_order=(0,1,1,7)).fit(disp=0)
        prediction = fit.forecast(steps=forecast_time)
        return prediction[-1]

    def forescast_error():
        pass