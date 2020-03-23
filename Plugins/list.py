from pyrogram import Client, Filters
from time import sleep, time


@Client.on_message(Filters.me & Filters.command(['userlist'], ['.', '/']))
def user_list(app, message):
    sleep(0.2)
    chat_type = message.chat.type
    if chat_type != "private":
        creator = ""
        admins = ""
        for i in app.get_chat_members(message.chat.id, filter="administrators"):
            if i.status == "creator":
                creator += "👑 -> @{}\n\n".format(i.user.username) if i.user.username \
                    else "👑 -> [{}](tg://user?id={})\n\n".format(
                        i.user.first_name, i.user.id
                    )
            if i.status == "administrator":
                admins += " ⛑ -> @{}\n".format(i.user.username) if i.user.username \
                    else " ⛑ -> [{}](tg://user?id={})\n".format(
                        i.user.first_name, i.user.id
                    )
        message.edit(f'Admin list:\n{creator}{admins}', parse_mode="Markdown", disable_web_page_preview=True)


@Client.on_message(Filters.me & Filters.command(['botlist'], ['.', '/']))
def bot_list(app, message):
    sleep(0.2)
    chat_type = message.chat.type
    if chat_type != "private":
        bots = ""
        for i in app.get_chat_members(message.chat.id, filter="bots"):
            bots += " 🤖 -> @{}\n".format(i.user.username)
        message.edit(f'Bot list:\n{bots}', parse_mode="Markdown", disable_web_page_preview=True)


@Client.on_message(Filters.me & Filters.command(['ghostlist'], ['.', '/']))
def ghost_list(app, message):
    sleep(0.2)
    message.edit('Wait...')
    chat_type = message.chat.type
    if chat_type != "private":
        num = 0
        for i in app.iter_chat_members(message.chat.id):
            if i.user.is_deleted:
                num += 1
        message.edit(f'Deleted account number : {num}', disable_web_page_preview=True)


@Client.on_message(Filters.me & Filters.command(['zombielist'], ['.', '/']))
def zombie_list(app, message):
    sleep(0.2)
    message.edit('Wait...')
    chat_type = message.chat.type
    if chat_type != "private":
        num = 0
        for i in app.iter_chat_members(message.chat.id):
            if i.user.status in ("long_time_ago", "within_month"):
                num += 1
        message.edit(f'Zombie account number : {num}', disable_web_page_preview=True)


@Client.on_message(Filters.me & Filters.command(['ghostkick'], ['.', '/']))
def ban_ghosts(app, message):
    sleep(0.2)
    message.edit('Wait...')
    chat_type = message.chat.type
    if app.get_chat_member(message.chat.id, app.get_me().id).status == "creator" or "administrator":
        if chat_type != "private":
            num = 0
            for i in app.iter_chat_members(message.chat.id):
                if i.user.is_deleted:
                    app.kick_chat_member(message.chat.id, i.user.id, time() + 60)
                    num += 1
                    sleep(0.5)
            message.edit(f'{num} deleted account is kicked')


@Client.on_message(Filters.me & Filters.command(['zombiekick'], ['.', '/']))
def ban_zombies(app, message):
    sleep(0.2)
    message.edit('Wait...')
    chat_type = message.chat.type
    if app.get_chat_member(message.chat.id, app.get_me().id).status == "creator" or "administrator":
        if chat_type != "private":
            num = 0
            for i in app.iter_chat_members(message.chat.id):
                if i.user.status in ("long_time_ago", "within_month"):
                    app.kick_chat_member(message.chat.id, i.user.id, time() + 60)
                    num += 1
                    sleep(0.5)
            message.edit(f'{num} zombie account is kicked')
