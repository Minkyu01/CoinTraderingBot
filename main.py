import classes as cl
import pyupbit
import pandas as pd
import app
ticker_db = []
coins_db = []

app.main_site()


# test = app.appt 이거 일단 import까지는 됐는데 html input값은 안불러와져서 따로 알아봐야할듯 아마 내생각에 app.py에 class를 따로 만들거나
# 다른모듈에 클래스나 함수를 만들어서 app.py, main.py 두곳에 import 해야할거같음
# print(test)

def coin_export(num):
  #key = input.assetInfo(ticker_db)

  #a = key.info()
  ticker_db.append(a)

  chart = pyupbit.get_ohlcv(ticker=ticker_db[num]["Ticker"],
                            count=ticker_db[num]["Ticker_info"]["duration"],
                            to=20200201)

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
