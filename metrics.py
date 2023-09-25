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

    Attributes
    ----------
    data : class or list of classes
        response from API as ProductBook object or list of Candle objects

    Methods
    -------
    product_details
        Returns best bid and ask information from the product book as a dictionary.
    mid_price
        Calculates average price of the highest bid and lowest ask from product candle data model.
    forecast
        Forecasts average price of the highest bid and lowest ask from product candle data model.

    """
    def __init__(self, data): # TODO: move data to each method and get rid of init?
        """
        Parameters
        ----------
        data : class or list of classes
            response from API as ProductBook object or list of Candle objects
        """
        self.data = data

    def product_details(self):
        """Returns best bid and ask information from the product book.

        Returns
        -------
        dict
            A dictionary containing 'book_time','best_bid_price', 'best_ask_price', 'best_bid_quant', 'best_ask_quant', 'bid_ask_diff' keys.
        """
        return {'book_time':self.data.time
                ,'best_bid_price':float(self.data.bids.price)
                ,'best_ask_price':float(self.data.asks.price)
                ,'best_bid_quant':self.data.bids.quantity
                ,'best_ask_quant':self.data.asks.quantity
                ,'bid_ask_diff':float(self.data.asks.price)-float(self.data.bids.price)}
    
    def mid_price(self, timeframe):
        """Calculates average price of the highest bid and lowest ask from a product candle.

        Parameters
        ----------
        timeframe : int
            last minutes from which the average price is supposed to be calculated

        Returns
        -------
        float
            Average price of best bid and best ask.
        """
        if timeframe == 1:
            last_candle = self.data[-1]
            candles_av = (last_candle.high + last_candle.low)/2
        else:
            past_time_point = time.time() - timeframe * 60
            candles_slice = Enumerable(self.data).where(lambda x: x.time >= past_time_point)
            candles_av = candles_slice.avg(lambda x: (x.low + x.high)/2)
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
        #  TODO: clean!

        # using df
        #df = pd.DataFrame(self.data, columns=['timestamp', 'low', 'high', 'open', 'close', 'volume'])
        #df['timestamp'] = pd.to_datetime(df['timestamp'], unit='s')
        #df['mid-price'] = (df['low'] + df['high'])/2
        #df = df.sort_values(by=['timestamp'], ascending=True)
        #df.index = pd.DatetimeIndex(df.index).to_period('M')
        # using candles
        # order the candlestick data in ascending order based on time
        candles_ascending = Enumerable(self.data).order_by(lambda x: x.time)
        # calculate the average best bid - best ask price for each candlestick data point
        av_list = [(candle.high + candle.low)/2 for candle in candles_ascending]
        # fit SARIMA model to the list of average prices
        fit = SARIMAX(av_list, order=(2, 1, 4),seasonal_order=(0,1,1,7)).fit(disp=0)
        #fit_df = SARIMAX(df['mid-price'], order=(2, 1, 4),seasonal_order=(0,1,1,7)).fit(disp=0)
        # generate a forecast for the mid-prices at the specified time in the future
        prediction = fit.forecast(steps=forecast_time)
        #prediction_df = fit_df.forecast(steps=forecast_time)
        #pred_array = prediction.to_numpy()
        return prediction[-1]


    def forescast_error(self):
        pass
