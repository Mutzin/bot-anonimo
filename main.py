import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters

# Defina o token do bot
TOKEN = "8090131009:AAHjp7wG2D4_BPSRoQa0F6QAPQUOcLxnhqk"

# Configurações de log para depuração
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

# Função para o comando /start
async def start(update: Update, context):
    await update.message.reply("Olá! Eu sou seu bot anônimo. Envie sua mensagem!")

# Função para mensagens privadas
async def handle_private_messages(update: Update, context):
    if update.message.chat.type == "private":
        text = update.message.text
        # Enviar para o grupo específico
        group_id = -1002626451118  # Substitua com o ID correto do grupo
        await context.bot.send_message(group_id, f"Mensagem Anônima: {text}")

# Função para erros
async def error(update: Update, context):
    logger.warning(f'Update "{update}" causou o erro "{context.error}"')

def main():
    # Criação do aplicativo com o token
    app = Application.builder().token(TOKEN).build()

    # Adicionando os handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_private_messages))

    # Tratamento de erros
    app.add_error_handler(error)

    # Iniciar o bot
    app.run_polling()

if __name__ == '__main__':
    main()
