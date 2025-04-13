from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
import os
from keep_alive import keep_alive

TOKEN = '8090131009:AAHjp7wG2D4_BPSRoQa0F6QAPQUOcLxnhqk'
GROUP_ID = '-1002626451118'  # Seu ID do grupo

# Função para responder ao comando /start
def start(update, context):
    update.message.reply_text("Bot está online!")

# Função principal para iniciar o bot
def main():
    # Configura o aplicativo do Telegram
    app = ApplicationBuilder().token(TOKEN).build()

    # Adiciona o manipulador do comando /start
    app.add_handler(CommandHandler("start", start))

    # Outras configurações do bot podem ser adicionadas aqui

    # Mantém o bot rodando, chamando a função do Flask (para Koyeb)
    keep_alive()  # Chama a função para manter o bot rodando

    # Inicia o polling para o bot
    app.run_polling()

# Verifica se é o script principal para rodar a função main
if __name__ == '__main__':
    main()
