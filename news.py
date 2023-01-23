import feedparser
from telegram.ext import Updater, JobQueue

# Inisialisasi bot Telegram
updater = Updater(5837266855:AAGIuaQqoLuNJh4f-H01mi9Pu4_MkmlqbLk, use_context=True)
job_queue = updater.job_queue

# Fungsi untuk mengambil berita terbaru
def get_latest_news():
    # Daftar situs berita yang ingin dimonitor
    news_sources = {
        'coindesk': 'https://www.coindesk.com/feed',
        'cointelegraph': 'https://cointelegraph.com/feed',
        'crypto news': 'https://www.cryptonews.com/rss/'
    }
    news_list = []
    for source, feed_url in news_sources.items():
        feed = feedparser.parse(feed_url)
        for entry in feed.entries:
            news_list.append((source, entry.title, entry.link))
    return news_list

# Fungsi yang akan dipanggil untuk mengirim notifikasi
def send_news(context):
    news_list = get_latest_news()
    for news in news_list:
        message = f"Sumber: {news[0]}\nJudul: {news[1]}\nLink: {news[2]}\n"
        context.bot.send_message(chat_id=SukamajuPetarunk, text=message)

# JobQueue untuk mengeksekusi send_news setiap 15 menit
job_queue.run_repeating(send_news, interval=900, first=0)

# Jalankan bot
updater.start_polling()
