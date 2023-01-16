import backtesting as bt
import pyupbit

class assetInfo:
   def __init__(self, db):
      self.db = db
      self.duration = int(input("duration : ")) # 일단 month기간으로
      self.start_year = int(input("start_year :")) #8글자 형식으로
      self.end_year = int(input("end_year :")) # 8글자 형식으로 
      self.initial_amount = int(input("Initial_amount :")) # 초기 금액
      self.ticker = input("Ticker (KRW-BTC) : ") #종목명 KRW-BTC
      self.next_asset = int(input("자산 추가 1 아님 0 : ")) # 

   def info(self):
      self.db = {'Ticker' : self.ticker , 
          'Ticker_info' : {'duration' : self.duration,
                            'start_year' : self.start_year,
                            'end_year' : self.end_year,
                            'initial_amount' : self.initial_amount
                            },
          "next_asset" : self.next_asset
          }
         
      return self.db
# df = pyupbit.get_ohlcv(ticker= ticker,
#                        count = duration,
#                     to="20210410")

# backtest = bt.backTesting(df, initial_amount)
# backtest.execute()
