from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
from keep_alive import keep_alive

TOKEN = '8090131009:AAHjp7wG2D4_BPSRoQa0F6QAPQUOcLxnhqk'
GROUP_ID = -1002626451118

# /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Olá! Envie sua mensagem aqui e ela será enviada anonimamente para o grupo.")

# Envia mensagens privadas para o grupo
async def handle_private_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.chat.type == "private":
        msg = update.message.text
        await context.bot.send_message(chat_id=GROUP_ID, text=msg)

keep_alive()

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_private_message))

app.run_polling()
