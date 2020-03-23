from pyrogram import Client, Filters, ChatPermissions
from time import time
from datetime import datetime

def user_mention(text):
    for i in text.split():
        if i.startswith("@"):
            return i[1:]


def mute_time(text):
    days = hours = minutes = 0
    for i in text.split():
        if i.endswith("d") and i[:-1].isdigit():
            days = int(i[:-1]) * 24 * 60 * 60
        elif i.endswith("h") and i[:-1].isdigit():
            hours = int(i[:-1]) * 60 * 60
        elif i.endswith("m") and i[:-1].isdigit():
            minutes = int(i[:-1]) * 60
    return int(days + hours + minutes)


@Client.on_message(Filters.me & Filters.command(['mute'], ['.', '/']))
def mute_user(app, message):
    chat_type = message.chat.type
    stats = ("creator", "administrator")
    if chat_type != "private":
        if app.get_chat_member(message.chat.id, app.get_me().id).status in stats:
            if message.reply_to_message:
                if app.get_chat_member(message.chat.id, message.reply_to_message.from_user.id).status not in stats:
                    app.restrict_chat_member(message.chat.id, message.reply_to_message.from_user.id,
                                             ChatPermissions(), 0)
                    if message.reply_to_message.from_user.username:
                        message.edit(f'@{message.reply_to_message.from_user.username} is muted')
                        return
                    else:
                        message.edit('[{}](tg://user?id={}) is muted'.format(
                            message.reply_to_message.from_user.first_name, message.reply_to_message.from_user.id
                        ), parse_mode="Markdown", disable_web_page_preview=True)
                        return
                else:
                    message.edit('You can\'t mute admin')
                    return
            if message.entities:
                if message.entities[0].type == 'mention':
                    if len(message.text.split()) == 2:
                        if app.get_chat_member(message.chat.id, user_mention(message.text)).status not in stats \
                                if user_mention(message.text) in\
                                   [i.user.username for i in app.iter_chat_members(message.chat.id)] else True:
                            app.restrict_chat_member(message.chat.id, message.reply_to_message.from_user.id,
                                                     ChatPermissions(), 0)
                            message.edit(f'@{user_mention(message.text)} is muted')
                            return
                    else:
                        message.edit('You should use like this ".mute @username"')
                        return
                elif message.entities[0].type == 'text_mention':
                    if len(message.text.split()) == 2:
                        if app.get_chat_member(message.chat.id, message.entities[0].user.id).status not in stats:
                            app.restrict_chat_member(message.chat.id, message.reply_to_message.from_user.id,
                                                     ChatPermissions(), 0)
                            message.edit('[{}](tg://user?id={}) is muted'.format(
                                message.entities[0].user.first_name, message.entities[0].user.id
                            ))
                            return
                        else:
                            message.edit('Yout can\'t mute admin')
                            return
                    else:
                        message.edit('You should use like this ".mute @username"')
                        return


@Client.on_message(Filters.me & Filters.command(['unmute'], ['.', '/']))
def unmute_user(app, message):
    chat_type = message.chat.type
    stats = ("creator", "administrator")
    if chat_type != "private":
        if app.get_chat_member(message.chat.id, app.get_me().id).status in stats:
            if message.reply_to_message:
                if app.get_chat_member(message.chat.id, message.reply_to_message.from_user.id).status not in stats:
                    app.restrict_chat_member(message.chat.id, message.reply_to_message.from_user.id,
                                             ChatPermissions(can_send_messages=True,
                                                             can_send_media_messages=True,
                                                             can_invite_users=True,
                                                             can_add_web_page_previews=True,
                                                             can_send_polls=True,
                                                             can_send_other_messages=True), 0)
                    if message.reply_to_message.from_user.username:
                        message.edit(f'@{message.reply_to_message.from_user.username} is unmuted')
                        return
                    else:
                        message.edit('[{}](tg://user?id={}) is unmuted'.format(
                            message.reply_to_message.from_user.first_name, message.reply_to_message.from_user.id
                        ), parse_mode="Markdown", disable_web_page_preview=True)
                        return
                else:
                    message.edit('You can\'t unmute admin')
                    return
            if message.entities:
                if message.entities[0].type == 'mention':
                    if len(message.text.split()) == 2:
                        if app.get_chat_member(message.chat.id, user_mention(message.text)).status not in stats \
                                if user_mention(message.text) in\
                                   [i.user.username for i in app.iter_chat_members(message.chat.id)] else True:
                            app.restrict_chat_member(message.chat.id, message.reply_to_message.from_user.id,
                                                     ChatPermissions(can_send_messages=True,
                                                                     can_send_media_messages=True,
                                                                     can_invite_users=True,
                                                                     can_add_web_page_previews=True,
                                                                     can_send_polls=True,
                                                                     can_send_other_messages=True), 0)
                            message.edit(f'@{user_mention(message.text)} is muted')
                            return
                    else:
                        message.edit('You should use like this ".unmute @username"')
                        return
                elif message.entities[0].type == 'text_mention':
                    if len(message.text.split()) == 2:
                        if app.get_chat_member(message.chat.id, message.entities[0].user.id).status not in stats:
                            app.restrict_chat_member(message.chat.id, message.reply_to_message.from_user.id,
                                                     ChatPermissions(can_send_messages=True,
                                                                     can_send_media_messages=True,
                                                                     can_invite_users=True,
                                                                     can_add_web_page_previews=True,
                                                                     can_send_polls=True,
                                                                     can_send_other_messages=True), 0)
                            message.edit('[{}](tg://user?id={}) is unmuted'.format(
                                message.entities[0].user.first_name, message.entities[0].user.id
                            ))
                            return
                        else:
                            message.edit('Yout can\'t unmute admin')
                            return
                    else:
                        message.edit('You should use like this ".unmute @username"')
                        return


@Client.on_message(Filters.me & Filters.command(['tmute'], ['.', '/']))
def tmute_user(app, message):
    chat_type = message.chat.type
    stats = ("creator", "administrator")
    if chat_type != "private":
        if app.get_chat_member(message.chat.id, app.get_me().id).status in stats:
            if message.reply_to_message:
                if app.get_chat_member(message.chat.id, message.reply_to_message.from_user.id).status not in stats:
                    if mute_time(message.text):
                        app.restrict_chat_member(message.chat.id, message.reply_to_message.from_user.id,
                                                 ChatPermissions(), time() + mute_time(message.text))
                        if message.reply_to_message.from_user.username:
                            message.edit(f'@{message.reply_to_message.from_user.username} is muted'
                                         f' for {datetime.utcfromtimestamp(mute_time(message.text)).strftime("%d days %H hours %M minutes")}')
                            return
                        else:
                            message.edit('[{}](tg://user?id={}) is muted for {}'.format(
                                message.reply_to_message.from_user.first_name, message.reply_to_message.from_user.id,
                                datetime.utcfromtimestamp(mute_time(message.text)).strftime(
                                    "%d days %H hours %M minutes")
                            ), parse_mode="Markdown", disable_web_page_preview=True)
                            return
                else:
                    message.edit('You can\'t mute admin')
                    return
            if message.entities:
                if message.entities[0].type == 'mention':
                    if len(message.text.split()) >= 2:
                        if app.get_chat_member(message.chat.id, user_mention(message.text)).status not in stats \
                                if user_mention(message.text) in\
                                   [i.user.username for i in app.iter_chat_members(message.chat.id)] else True:
                            if mute_time(message.text):
                                app.restrict_chat_member(message.chat.id, message.reply_to_message.from_user.id,
                                                         ChatPermissions(), time() + mute_time(message.text))
                                message.edit(f'@{user_mention(message.text)} is muted '
                                             f'for {datetime.utcfromtimestamp(mute_time(message.text)).strftime("%d days %H hours %M minutes")}')
                                return
                    else:
                        message.edit('You should use like this ".tmute @username 1d 1h 1m"')
                        return
                elif message.entities[0].type == 'text_mention':
                    if len(message.text.split()) >= 2:
                        if app.get_chat_member(message.chat.id, message.entities[0].user.id).status not in stats:
                            if mute_time(message.text):
                                app.restrict_chat_member(message.chat.id, message.reply_to_message.from_user.id,
                                                         ChatPermissions(), time() + mute_time(message.text))
                                message.edit('[{}](tg://user?id={}) is muted for {}'.format(
                                    message.entities[0].user.first_name, message.entities[0].user.id,
                                    datetime.utcfromtimestamp(mute_time(message.text)).strftime(
                                        "%d days %H hours %M minutes")
                                ))
                                return
                        else:
                            message.edit('Yout can\'t mute admin')
                            return
                    else:
                        message.edit('You should use like this ".tmute @username 1d 1h 1m"')
                        return


@Client.on_message(Filters.me & Filters.command(['kick'], ['.', '/']))
def kick_user(app, message):
    chat_type = message.chat.type
    stats = ("creator", "administrator")
    if chat_type != "private":
        if app.get_chat_member(message.chat.id, app.get_me().id).status in stats:
            if message.reply_to_message:
                if app.get_chat_member(message.chat.id, message.reply_to_message.from_user.id).status not in stats:
                    app.kick_chat_member(message.chat.id, message.reply_to_message.from_user.id, time() + 60)
                    if message.reply_to_message.from_user.username:
                        message.edit(f'@{message.reply_to_message.from_user.username} is kicked')
                        return
                    else:
                        message.edit('[{}](tg://user?id={}) is kicked'.format(
                            message.reply_to_message.from_user.first_name, message.reply_to_message.from_user.id
                        ), parse_mode="Markdown", disable_web_page_preview=True)
                        return
                else:
                    message.edit('You can\'t kick admin')
                    return
            if message.entities:
                if message.entities[0].type == 'mention':
                    if len(message.text.split()) == 2:
                        if app.get_chat_member(message.chat.id, user_mention(message.text)).status not in stats \
                                if user_mention(message.text) in\
                                   [i.user.username for i in app.iter_chat_members(message.chat.id)] else True:
                            app.kick_chat_member(message.chat.id, user_mention(message.text), time() + 60)
                            message.edit(f'@{user_mention(message.text)} is kicked')
                            return
                    else:
                        message.edit('You should use like this ".kick @username"')
                        return
                elif message.entities[0].type == 'text_mention':
                    if len(message.text.split()) == 2:
                        if app.get_chat_member(message.chat.id, message.entities[0].user.id).status not in stats:
                            app.kick_chat_member(message.chat.id, user_mention(message.text), time() + 60)
                            message.edit('[{}](tg://user?id={}) is kicked'.format(
                                message.entities[0].user.first_name, message.entities[0].user.id
                            ))
                            return
                        else:
                            message.edit('Yout can\'t kick admin')
                            return
                    else:
                        message.edit('You should use like this ".kick @username"')
                        return
