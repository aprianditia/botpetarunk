import feedparser
import telegram
from telegram.ext import Updater, CommandHandler, JobQueue

# Inisialisasi bot Telegram
updater = Updater(token='YOUR_TELEGRAM_BOT_TOKEN', use_context=True)
dispatcher = updater.dispatcher

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

# Fungsi yang akan dipanggil ketika pengguna mengetik /news
def send_news(context):
    news_list = get_latest_news()
    for news in news_list:
        message = f"Sumber: {news[0]}\nJudul: {news[1]}\nLink: {news[2]}\n"
        context.bot.send_message(chat_id=update.message.chat_id, text=message)

# Tambahkan fungsi send_news sebagai handler untuk perintah /news
news_handler = CommandHandler('news', send_news)
dispatcher.add_handler(news_handler)

# Jalankan bot
updater.start_polling()

# set job queue
job_queue = updater.job_queue
job_queue.run_repeating(send_news, interval=900, first=0)
