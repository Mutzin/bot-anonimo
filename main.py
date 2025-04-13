from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
from keep_alive import manter_vivo

TOKEN = "8090131009:AAHjp7wG2D4_BPSRoQa0F6QAPQUOcLxnhqk"
GROUP_ID = -1002626451118  # Substitua pelo ID real do seu grupo

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Envie sua mensagem aqui. Ela será enviada anonimamente para o grupo.")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.chat.type == "private":
        mensagem = update.message.text
        await context.bot.send_message(chat_id=GROUP_ID, text=f"📩 {mensagem}")
        await update.message.reply_text("✅ Mensagem enviada anonimamente!")

if __name__ == '__main__':
    manter_vivo()  # inicia o servidor Flask para o Koyeb

    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("Bot iniciado com sucesso.")
    app.run_polling()
