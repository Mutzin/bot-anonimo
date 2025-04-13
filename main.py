from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
import os
from keep_alive import keep_alive

TOKEN = '8090131009:AAHjp7wG2D4_BPSRoQa0F6QAPQUOcLxnhqk'
GROUP_ID = '-1002626451118'  # Seu ID do grupo

def start(update, context):
    update.message.reply_text("Bot está online!")

# Função principal para iniciar o bot
def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    # Outras configurações do bot

    keep_alive()  # Chama a função para manter o bot rodando
    app.run_polling()

if __name__ == '__main__':
    main()
