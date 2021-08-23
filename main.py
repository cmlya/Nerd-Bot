from random import random
from uuid import uuid4
from telegram import Update, InlineQueryResultArticle, InputTextMessageContent
import Constants as Keys
from telegram.ext import *
import Responses as Response

print("Bot started")


def start_command(update, context):
    update.message.reply_text('Welcome to SagzanBot coded in Python! u can find my code in my developer\'s GitHub!')


def help_command(update, context):
    update.message.reply_text('no help')


def handle_message(update, context):
    text = str(update.message.text)
    response = Response.response(text)
    update.message.reply_text(response)


def inline_query(update: Update, context: CallbackContext) -> None:
    query = update.inline_query.query
    results = [
        InlineQueryResultArticle(
            id=str(uuid4()),
            title="How sagzan are you? 📚",
            input_message_content=InputTextMessageContent("I am " + str(round(random() * 100)) +
                                                          "% sagzan!" + Response.double_emoji()),
        ),
        InlineQueryResultArticle(
            id=str(uuid4()),
            title="How sagzan is " + query + "? 🤨",
            input_message_content=InputTextMessageContent(query + " is " + str(round(random() * 100)) +
                                                          "% sagzan!" + Response.double_emoji()),
        ),
    ]
    update.inline_query.answer(results)


def error(update, context):
    print(f"Update {update} caused error {context.error}")


def main():
    updater = Updater(Keys.APIkey, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(InlineQueryHandler(inline_query))  # inline
    dp.add_handler(MessageHandler(Filters.text, handle_message))
    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()


main()
