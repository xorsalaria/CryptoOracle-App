import requests
import json

import os
os.system('cls')
###########################################

api_request = requests.get("https://api.coinmarketcap.com/v1/ticker/")
api = json.loads(api_request.content)

currencies = ["BTC", "XRP", "EOS", "STEEM"]

# My Portfolio
my_portfoloio = [
	{
		"sym": "STEEM",
		"amount_owned": 4000,
		"price_paid_per": .80
	},
	{
		"sym": "XRP",
		"amount_owned": 6000,
		"price_paid_per": .20
	},
	{
		"sym": "XLM",
		"amount_owned": 2000,
		"price_paid_per": .10
	},
	{
		"sym": "EOS",
		"amount_owned": 1000,
		"price_paid_per": 2.00
	}

]

portfolio_profit_loss = 0

print("-----------------------------")
for x in api:
	for coin in my_portfoloio:
		if coin["sym"] == x["symbol"]:

			#Let's do some Maths
			total_paid = float(coin["amount_owned"]) * float(coin["price_paid_per"])
			current_value = float(coin["amount_owned"]) * float(x["price_usd"])
			profit_loss = current_value - total_paid
			portfolio_profit_loss += profit_loss 



			print(x["name"])
			print("USD: ${0:.2f}".format(float(x["price_usd"])))
			print(x["rank"])
			print("Total Paid: ${0:.2f}".format(total_paid))
			print("Current Values: ${0:.2f}".format(current_value))
			print("Profit/Loss: ${0:.2f}".format(profit_loss))
			print("-----------------------------")

print("Portfolio Profit/Loss:",portfolio_profit_loss)




