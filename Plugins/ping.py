from pyrogram import Client, Filters
import datetime


@Client.on_message(Filters.me & Filters.command(['ping'], ['.', '/']))
def ping(client, message):
    start = datetime.datetime.now()
    message.edit('Pong!')
    end = datetime.datetime.now()
    ms = (end - start).microseconds / 1000
    message.edit('Pong!\n{}'.format(ms))