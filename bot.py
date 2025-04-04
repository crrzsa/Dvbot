import os
import logging
from pyrogram import Client, filters

# إعدادات تسجيل الدخول
API_ID = int(os.getenv("API_ID", "29289705"))  
API_HASH = os.getenv("API_HASH", "1bbd8f4dd2d25a03585e89b819cd03da")  
BOT_TOKEN = os.getenv("BOT_TOKEN", "8116550412:AAEXHaeGr7STYOyL4S-jSGO4ZbFd_atCNqPc")

# تهيئة البوت
bot = Client(
    "media_downloader_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

# إعداد سجل الأخطاء
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# أمر /start
@bot.on_message(filters.command("start"))
def start_command(client, message):
    message.reply_text("مرحبًا! أرسل لي رابط فيديو وسأقوم بتحميله لك.")

# استقبال الروابط وتحميل الوسائط
@bot.on_message(filters.text & filters.regex(r"https?://"))
def download_media(client, message):
    url = message.text
    message.reply_text(f"جاري تحميل الفيديو من: {url}")
    # (هنا يمكنك إضافة كود تحميل الفيديو باستخدام yt-dlp أو أي مكتبة أخرى)

# تشغيل البوت
if __name__ == "__main__":
    bot.run()