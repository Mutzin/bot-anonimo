from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
import logging
from keep_alive import keep_alive  # Caso esteja usando Flask para manter o bot online

# Token do seu bot
TOKEN = '8090131009:AAHjp7wG2D4_BPSRoQa0F6QAPQUOcLxnhqk'
GROUP_ID = '-1002626451118'  # Seu ID do grupo

# Habilitar logs
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

# Função para lidar com o comando /start
async def start(update: Update, context):
    await update.message.reply_text('Olá! Envie suas mensagens e eu as repassarei anonimamente para o grupo.')

# Função para lidar com mensagens de texto
async def handle_message(update: Update, context):
    text = update.message.text  # A mensagem enviada
    if '@' in text:  # Se houver um @, trata como menção
        await context.bot.send_message(chat_id=GROUP_ID, text=f"Mensagem direcionada: {text}")
    else:
        await context.bot.send_message(chat_id=GROUP_ID, text=f"Mensagem anônima: {text}")

# Função principal para configurar o bot
async def main():
    # Criar o objeto Application
    application = ApplicationBuilder().token(TOKEN).build()

    # Adicionar handlers para o bot
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Iniciar o bot
    await application.run_polling()

# Rodar o Flask app para manter o bot online
if __name__ == "__main__":
    keep_alive()  # Função para manter o bot online, caso você esteja usando Flask
    import asyncio
    asyncio.run(main())
