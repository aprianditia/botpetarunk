import telegram
import requests

bot = telegram.Bot(token="5837266855:AAGIuaQqoLuNJh4f-H01mi9Pu4_MkmlqbLk")

url = "https://indodax.com/api/summaries"
response = requests.get(url)
data = response.json()

for currency in data:
    last_price = currency['last']
    change = currency.get('change',0) #default value 0
    currency_name = currency['name']
    volume_buy = currency['buy']
    volume_sell = currency['sell']
    formatted_price = "Rp" + "{:,}".format(last_price).replace(",", ".")
    
    if abs(change) >= 5:
        if change > 0:
            message = f"Wow, terjadi kenaikan harga mata uang {currency_name} sebesar {change}%! Harga saat ini adalah Rp {formatted_price} dengan volume pembelian sebesar {volume_buy} dan volume penjualan sebesar {volume_sell}."
        elif change < 0:
            message = f"Oh tidak, terjadi penurunan harga mata uang {currency_name} sebesar {change}%! Harga saat ini adalah Rp {formatted_price} dengan volume pembelian sebesar {volume_buy} dan volume penjualan sebesar {volume_sell}."
        bot.send_message(chat_id="SukamajuPetarunk", text
