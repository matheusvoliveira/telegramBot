from telegram.ext import *
import keys

print('Starting up bot ...')

def start_command(update, context):
    update.message.reply_text('Hello there! I\'m a bot. Nice to meet you!')


def help_command(update, context):
    update.message.reply_text('Try typping anything and i will respond!')

def custom_command(update_context):
    update.message.reply_text('This is a custom command!')

def handle_response(text: str) -> str:
    if 'hello' in the text:
        return 'Hey there' \
    if 'how are you' in text:
        return 'I am good, thanks'
    else
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

    #teste
