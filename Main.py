import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

TOKEN = "I_TOKEN_THAR_KHA_HETAH_DAH_RAW"

logging.basicConfig(level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👻 Hey! Ka ni Ghost Bot!\nEng pawh min zawt rawh, ka lo chhang ang che.\nMizo in pawh ka hrethiam e!")

async def help_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("/start - Bot tih nunna\n/help - Hei hi\nThu i ziah apiang ka lo chhang ang!")

async def chat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()
    name = update.message.from_user.first_name
    if "ka hming" in text or "i hming" in text:
        reply = "Ka hming chu Ghost a nia 👻 Nang chu " + name + " i ni tiraw?"
    elif "mizo" in text:
        reply = "Mizo tawng ka thiam ve deuh! Eng nge i hriat duh? Mizo tawngin min zawt rawh."
    elif "bialnu" in text:
        reply = "Bialnu chu muhil tir rawh, a mutui laiin bot kan siam a ni lawm 😂"
    elif "hello" in text or "hi" in text or "hey" in text:
        reply = f"Hey {name}! Eng nge i tih? Ka ngai che a!"
    elif "love" in text or "hmangaih" in text:
        reply = "Aww... ka lai deuh. Mahse ka ni Ghost, ka hmangaih che ❤️👻"
    elif "bye" in text or "mangtha" in text:
        reply = "Mangtha le! Mu tha rawh aw, naktuk ah kan inbe leh dawn nia."
    elif "?" in text:
        reply = f"Hmm... '{update.message.text}' tih kha chu... ka ngaihtuah mek."
    else:
        reply = f"Ka hrethiam e, '{update.message.text}' i ti a. Min hrilh belh teh!"
    await update.message.reply_text(reply)

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_cmd))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, chat))
    print("Ghost Bot a nung ta!")
    app.run_polling()
