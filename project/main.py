import backtesting as bt
import pyupbit
import input
import matplotlib.pyplot as plt
import pandas as pd 

ticker_db = []
coins_db = []

def sibal(num):
   key = input.assetInfo(ticker_db)
   a = key.info()
   ticker_db.append(a)

   coin = pyupbit.get_ohlcv(ticker = ticker_db[num]["Ticker"],
                        count = ticker_db[num]["Ticker_info"]["duration"],
                     to="20210410")

   backtest = bt.backTesting(coin , ticker_db[num]["Ticker_info"]["initial_amount"])
   coin_db = backtest.execute()
   # coins_db.append(coin_db)
   result = pd.DataFrame(coin_db)
   print(coin_db)
   result.plot.line()
   plt.show()
   print("=================================================")

sibal(0)
# print(coins_db)

# if (ticker_db[0]["next_asset"] == 1):
#    sibal(1)
   
