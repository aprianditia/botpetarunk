import requests
from bs4 import BeautifulSoup

# Ambil halaman web akun Twitter yang ditentukan
twitter_handle = "tier10k"
url = f"https://twitter.com/{twitter_handle}"
response = requests.get(url)

# Parsing HTML
soup = BeautifulSoup(response.text, "html.parser")

# Cari tweet terbaru
tweet = soup.find("div", class_="js-tweet-text-container").text.strip()

# Kirim tweet ke grup Telegram
bot.send_message(chat_id=SukamajuPetarunk, text=tweet)
