from telegram.ext import *
import keys
import requests
import json

# info api IMDB
url = "https://online-movie-database.p.rapidapi.com/auto-complete"


searchTerm = ''

print('Starting up bot ...')

def start_command(update, context):
    update.message.reply_text('Hello there! I\'m a bot. Nice to meet you!')


def help_command(update, context):
    update.message.reply_text('Try typping anything and i will respond!')

def custom_command(update, context):
    update.message.reply_text('This is a custom command!')

def handle_response(text: str) -> str:
    split = text.split()
    searchTerm = split[1]
    if split[0] == 'search' \
            and len(searchTerm) > 2:
        response = requests.get(url, headers=keys.headers, params={"q": searchTerm})
        data = json.loads(response.text)
        formattedData = json.dumps(data, indent=4)
        dataDict = json.loads(formattedData)
        responses = dataDict["d"]
        # return 'searching for ' + split[1] + ' ...'
        movies_info = []
        for movie in responses:
            try:
                if movie["qid"] == 'tvSeries':
                    info = "Título: " + movie["l"] + "\n" + "Imagem: " + movie["i"]["imageUrl"] + "\n" + "Kind: " + \
                           movie["qid"]
                else:
                    info = "Título: " + movie["l"] + "\n" + "Imagem: " + movie["i"]["imageUrl"] + "\n" + "Kind: " + \
                           movie["qid"]
                movies_info.append(info)
            except:
                pass

        if movies_info:
            return '\n\n'.join(movies_info)
        else:
            return 'No movies found.'

        # for movie in responses:
        #     print("Título: " + movie["l"])
        #     print("Imagem: " + movie["i"]["imageUrl"])
        #     print("Tipo: " + movie["qid"])
        #     print("Ano: " + movie["y"])
        #     print("Elenco: " + movie["s"])



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
