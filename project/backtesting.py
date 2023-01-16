class backTesting :
    def __init__(self, daily_data, coin_db) :
        self.daily_data = daily_data
    def execute(self):
        coin_db = self.daily_data["close"]
        return coin_db


# backtest = backTesting(df, 1000000)
# backtest.execute()
