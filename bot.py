import os
from dotenv import load_dotenv
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update, WebAppInfo
from telegram.ext import Application, CommandHandler, ContextTypes

# بارگذاری توکن از فایل .env
load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

# هندلر /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton(
            "🛍️ ورود به سایت", 
            web_app=WebAppInfo(url="https://anahid-crafts.my.canva.site/")
        )]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("به فروشگاه آنلاین آناهید خوش آمدید:", reply_markup=reply_markup)

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()

if __name__ == "__main__":
    main()





# from telegram import Update, KeyboardButton, ReplyKeyboardMarkup, WebAppInfo
# from telegram.ext import Application, CommandHandler, ContextTypes

# TOKEN = os.getenv("BOT_TOKEN")

# async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     web_app = WebAppInfo(url="https://anahid-crafts.my.canva.site/")
#     keyboard = [[KeyboardButton(text="باز کردن سایت آناهید", web_app=web_app)]]
#     reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
#     await update.message.reply_text("سلام! برای باز کردن سایت روی دکمه زیر کلیک کن:", reply_markup=reply_markup)

# app = Application.builder().token(TOKEN).build()
# app.add_handler(CommandHandler("start", start))

# app.run_polling()
















# from telegram import Update
# from telegram.ext import Application, CommandHandler, ContextTypes
# from dotenv import load_dotenv
# import os

# # بارگذاری متغیرهای محیطی از فایل .env
# load_dotenv()

# TOKEN = os.getenv("BOT_TOKEN")

# async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     await update.message.reply_text("🎉 به ربات آناهید خوش آمدید!")

# async def shop(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     await update.message.reply_text(
#         "🛍️ برای مشاهده فروشگاه آنلاین، اینجا کلیک کنید:\nhttps://basalam.com/anahid-crafte"
#     )

# def main():
#     app = Application.builder().token(TOKEN).build()

#     app.add_handler(CommandHandler("start", start))
#     app.add_handler(CommandHandler("shop", shop))

#     print("🤖 ربات در حال اجراست...")
#     app.run_polling()

# if __name__ == "__main__":
#     main()
