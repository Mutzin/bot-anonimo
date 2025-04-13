from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, CommandHandler, ContextTypes, filters
from keep_alive import manter_vivo  # Nome mais claro para função de manter o bot online

TOKEN = "8090131009:AAHjp7wG2D4_BPSRoQa0F6QAPQUOcLxnhqk"
GROUP_ID = -1001234567890  # Substitua pelo ID real do seu grupo

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Envie uma mensagem aqui e ela será enviada anonimamente para o grupo.")

async def receber_mensagem(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.chat.type == "private":
        mensagem = update.message.text
        await context.bot.send_message(chat_id=GROUP_ID, text=f"📩 {mensagem}")
        await update.message.reply_text("✅ Mensagem enviada anonimamente!")

if __name__ == "__main__":
    manter_vivo()  # Inicia o servidor Flask para manter o bot ativo (funciona no Koyeb)
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, receber_mensagem))

    print("Bot iniciado...")
    app.run_polling()
