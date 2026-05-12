from telegram.ext import ApplicationBuilder
from handlers import start, manus_cmd, tars_cmd, nubia_cmd

def create_bot(token):
    app = ApplicationBuilder().token(token).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("manus", manus_cmd))
    app.add_handler(CommandHandler("tars", tars_cmd))
    app.add_handler(CommandHandler("nubia", nubia_cmd))
    return app
