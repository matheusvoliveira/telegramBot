from telegram.ext import *
import keys

print('Starting up bot ...')

def start_command(update, context):
    update.message.reply_text('Hello there! I\'m a bot. Nice to meet you!')


def help_command(update, context):
    update.message.reply_text('Try typping anything and i will respond!')

def custom_command(update, context):
    update.message.reply_text('This is a custom command!')

def handle_response(text: str) -> str:
    if 'hello' in  text:
        return 'Hey there'
    if 'how are you' in text:
        return 'I am good, thanks'
    else:
        return 'Idk'
def handle_message(update, context):
    message_type = update.message.chat.type
    text = str(update.message.text).lower()
    response = ''

    if message_type == 'group':
        if '@mrxangbot' in text:
            new_text = text.replacec('@mrxangbot', '').strip()
            response = handle_response(new_text)
    else:
        response = handle_response(text)

    update.message.reply_text(response)

def error(update, context):
    print(f'Update {update} caused error: {context.error}')

if __name__ == '__main__':
    updater = Updater(keys.token, use_context=True)
    dp = updater.dispatcher

    #Commands
    dp.add_handler(CommandHandler('start', start_command))
    dp.add_handler(CommandHandler('help', help_command))
    dp.add_handler(CommandHandler('custom', custom_command))

    # o handler é um objeto que define como seu bot deve
    # responder uma mensagem especifica como por exemplo start_command

    #Messages
    dp.add_handler(MessageHandler(Filters.text,handle_message))

    #Errors
    dp.add_error_handler(error)

    #Run bot
    updater.start_polling(1.0)
    updater.idle()


