import requests

api = "https://api.coinbase.com/v2/prices/BTC-USD/spot"

bitcoin = requests.get(api)

data = bitcoin.json()
# print(data)

bitcoin_price = data["data"]["amount"]
print(bitcoin_price)