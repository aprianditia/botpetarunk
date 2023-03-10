import telegram
import requests
import json

bot = telegram.Bot(token="5837266855:AAGIuaQqoLuNJh4f-H01mi9Pu4_MkmlqbLk")

url = "https://indodax.com/api/summaries"
response = requests.get(url)
data = response.json()

for currency in data['tickers']:
    last_price = currency['last']
    change = currency['change']
    currency_name = currency['name']
    volume_buy = currency['buy']
    volume_sell = currency['sell']
    formatted_price = "Rp" + "{:,}".format(last_price).replace(",", ".")
    
    if abs(change) >= 5:
        if change > 0:
            message = f"Wow, terjadi kenaikan harga mata uang {currency_name} sebesar {change}%! Harga saat ini adalah Rp {formatted_price} dengan volume pembelian sebesar {volume_buy} dan volume penjualan sebesar {volume_sell}."
        elif change < 0:
            message = f"Oh tidak, terjadi penurunan harga mata uang {currency_name} sebesar {change}%! Harga saat ini adalah Rp {formatted_price} dengan volume pembelian sebesar {volume_buy} dan volume penjualan sebesar {volume_sell}."
        bot.send_message(chat_id="SukamajuPetarunk", text=message)
        
    if abs(change) >= 30 and currency['time'] <= 300:
        if change > 0:
            message = f"Perhatian! Terjadi lonjakan harga yang sangat besar pada mata uang {currency_name} sebesar {change}% dalam waktu kurang dari {currency['time']} detik! Harga saat ini adalah Rp {formatted_price} dengan volume pembelian sebesar {volume_buy} dan volume penjualan sebesar {volume_sell}. Segera lakukan tindakan sebelum harga semakin naik!"
        elif change < 0:
            message = f"Perhatian! Terjadi lonjakan harga yang sangat besar pada mata uang {currency_name} sebesar {change}% dalam waktu kurang dari {currency['time']} detik! Harga saat ini adalah Rp {formatted_price} dengan volume pembelian sebesar {volume_buy} dan volume penjualan sebesar {volume_sell}. Segera lakukan tindakan sebelum harga semakin turun!"
        bot.send_message(chat_id="SukamajuPetarunk", text=message)
