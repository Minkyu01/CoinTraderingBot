import bback.classes as cl
import pyupbit
import pandas as pd
import app
ticker_db = []
coins_db = []


def coin_export(num):
  key = input.assetInfo(ticker_db) # 이거오류

  a = key.info()
  ticker_db.append(a)

  chart = pyupbit.get_ohlcv(ticker=ticker_db[num]["Ticker"],
                            count=ticker_db[num]["Ticker_info"]["duration"],
                            to="20200125")

  backtest = cl.backtesting(chart,
                            ticker_db[num]["Ticker_info"]["initial_amount"])
  coin_db = backtest.execute()
  # coins_db.append(coin_db)
  result = pd.DataFrame(coin_db)
  print(coin_db)
  result.plot.line()

# coin_export(0)
# print(coins_db)

# if (ticker_db[0]["next_asset"] == 1):
#    sibal(1)
