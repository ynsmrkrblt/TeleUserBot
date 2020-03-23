from pyrogram import Client, Filters
from pymongo import MongoClient
from threading import Thread
import config
from time import sleep
from os import listdir

app = Client("session", config.api_id, config.api_hash, plugins=dict(root="Plugins"))

mclient = MongoClient(config.mongo_connect)
database = mclient["Telegram"]
collection = database["userbot"]

if collection.find_one({}):
    data = collection.find_one({})
else:
    collection.insert_one({"github": "https://github.com/ynsmrkrblt/TeleUserBot"})
    data = collection.find_one({})


@app.on_message(Filters.me & Filters.command(['helpme'], ['.', '/']))
def help_message(client, message):
    sleep(0.2)
    message.edit('Commands -> [telegra.ph](https://telegra.ph/TeleUserBot-Commands-03-21)\n'
                 'Plugins & News -> @teleuserbotnews\n'
                 'Github Source -> [Github](https://github.com/ynsmrkrblt/TeleUserBot)\n',
                 parse_mode="Markdown", disable_web_page_preview=True)


@app.on_message(Filters.me & Filters.command(['send plugin'], ['.', '/']))
def send_plugin(client, message):
    sleep(0.2)
    text = message.text
    if len(text.split()) == 3:
        if f"{text.split()[2]}.py" in listdir("Plugins"):
            app.delete_messages(message.chat.id, message.message_id)
            app.send_document(message.chat.id, "./Plugins/{}.py".format(text.split()[2]))
        else:
            message.edit('File is not found')
    elif len(text.split()) == 2:
        message.edit('You must input file name')


def database():
    sleep(10)
    while 1:
        for i in list(data.keys()):
            if i == "_id":
                data.pop("_id")
        collection.insert_one(data)
        collection.delete_one({})
        sleep(60)


Thread(target=database).start()
Thread(target=app.run()).run()