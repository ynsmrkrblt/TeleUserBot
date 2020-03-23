from pyrogram import Client, Filters
from time import sleep
from os import remove, listdir
from requests import post


@Client.on_message(Filters.me & Filters.command("paste", prefixes=".") & Filters.reply)
def del_dog(app, message):
    message.edit('Wait...')
    if message.reply_to_message:
        if message.reply_to_message.document:
            file_name = message.reply_to_message.document.file_name
            for i in listdir("./Downloads/"):
                if i == file_name:
                    remove(f"./Downloads/{i}")
            app.download_media(message.reply_to_message, file_name="./Downloads/{}".format(file_name))
            sleep(0.4)
            with open("./Downloads/{}".format(file_name), "r") as file:
                code = ""
                for i in file.readlines():
                    code += f"{i}\r\n"
                file.close()
                remove("./Downloads/{}".format(file_name))
                r = post("https://del.dog/documents", data=code).json()
                paste_url = f"https://del.dog/{r['key']}"
                message.edit(paste_url, disable_web_page_preview=True)
        else:
            message.edit('Reply message type must be document')
    else:
        message.edit('You must reply message')
