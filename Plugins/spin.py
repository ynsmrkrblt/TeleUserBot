from pyrogram import Client, Filters
from time import sleep

moon = "🌖🌕🌔🌓🌒🌑🌘🌗"
clock = "🕛🕑🕒🕓🕔🕕🕖🕗🕘🕙🕚"
run = "🏃‍⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀"
car = "🚗‍⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀"


@Client.on_message(Filters.me & Filters.command(['animation'], ['.', '/']))
def spin(app, message):
    if len(message.text.split()) > 1:
        text = " ".join(message.text.split()[1:]).replace(" ", "")
        if text in ("moon", "clock", "run", "car"):
            a = ""
            if text == "moon": a = moon
            elif text == "clock": a = clock
            elif text == "run": a = run
            elif text == "car": a = car
            for i in range(1, 4):
                for i in range(1, len(a)):
                    message.edit(a[i:] + a[:i])
                    sleep(0.4)
        else:
            for i in range(1,4):
                for i in range(1, len(text)):
                    message.edit(text[i:] + text[:i])
                    sleep(0.4)
