from coinbaseAPI import Request
import time
import os
from datetime import datetime

# User input
prod_id = str(input('Provide product ID (e.g. BTC-USD): ')).upper()

biggest_diff = 0
starttime = time.time()
while True:
    handler = Request(prod_id)
    buy_price = handler.get_buy()
    sell_price = handler.get_sell()
    buy_sell_diff = float(buy_price) - float(sell_price)
    if buy_sell_diff > biggest_diff:
        biggest_diff = buy_sell_diff
    os.system('clear')
    print(datetime.now())
    print(f'{prod_id}\nHighest bid: {buy_price}\nLowest ask: {sell_price}\nBiggest diff: {biggest_diff}')
    time.sleep(5.0 - ((time.time() - starttime) % 5.0))
