import time
import requests

token = '5837266855:AAGIuaQqoLuNJh4f-H01mi9Pu4_MkmlqbLk'

while True:
    # Ambil data harga kripto top gainer dari Indodax
    # (Anda perlu menggunakan API atau scraping untuk melakukan ini)
    top_gainers = get_top_gainers_from_indodax()

    # Kirim notifikasi harga kripto top gainer ke channel atau grup Telegram
    for coin in top_gainers:
        message = f'{coin["name"]} - Rp {coin["price"]}, {coin["change"]}%'
        data = {'chat_id': 'SukamajuPetarunk', 'text': message}
        requests.post(f'https://api.telegram.org/bot{token}/sendMessage', data=data)

    # Tunggu selama 5 menit sebelum mengirim notifikasi lagi
    time.sleep(300)
