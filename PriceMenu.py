import rumps
import requests

class CryptoTickerApp(rumps.App):
    def __init__(self):
        super(CryptoTickerApp, self).__init__("PriceTicker", title="Loading...")
        self.timer = rumps.Timer(self.update_prices, 15)  # 更新频率
        self.timer.start()

    def update_prices(self, _):
        prices = self.get_prices()
        self.title = f"₿{prices['BTC']}|Ξ{prices['ETH']}"
        print(f"title is :{self.title}")

    def get_prices(self):
        symbols = ['BTCUSDT','ETHUSDT','BNBUSDT']

        prices = {}
        for symbol in symbols:
            response = requests.get(f'https://api.binance.com/api/v3/ticker/price?symbol={symbol}')
            data = response.json()
            prices[symbol[:-4]] = round(float(data['price']))
        return prices

if __name__ == "__main__":
    CryptoTickerApp().run()
