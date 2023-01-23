import time
import requests
from bs4 import BeautifulSoup

def get_top_gainers_from_indodax():
    url = 'https://indodax.com/id/market'
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    table = soup.find_all('table')[0]
    rows = table.find_all('tr')

    coins = []
    for row in rows[1:]:
        cols = row.find_all('td')
        coin = {}
        coin['name'] = cols[1].find_all('a')[0].text.strip()
        coin['price'] = cols[2].text.strip()
        coin['change'] = cols[5].text.strip()
        coins.append(coin)

    # Sort list of coins by change in descending order
    coins = sorted(coins, key=lambda x: float(x['change'][:-1]), reverse=True)

    # Return top 5 gainers
    return coins[:5]

token = 'YOUR_BOT_TOKEN'

while True:
    # Ambil data top 5 kripto berdasarkan perubahan harga tertinggi dalam persen dalam waktu 24 jam
    top_gainers = get_top_gainers_from_indodax()

    # Kirim notifikasi harga kripto top gainer ke channel atau grup Telegram
    for coin in top_gainers:
        message = f'{coin["name"]} - Rp {coin["price"]}, {coin["change"]}'
        data = {'chat_id': '@your_channel_username', 'text': message}
        requests.post(f'https://api.telegram.org/bot{token}/sendMessage', data=data)

    # Tunggu selama 5 menit sebelum mengirim notifikasi lagi
    time.sleep(300)
