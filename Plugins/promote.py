from pyrogram import Client, Filters


def username(text):
    for i in text.split():
        if i.startswith("@"):
            return i[1:]


@Client.on_message(Filters.me & Filters.group & Filters.command(['promote'], ['.', '/']))
def promote_user(client, m):
    if client.get_chat_member(m.chat.id, client.get_me().id).status == 'creator' or 'administrator':
        if m.reply_to_message:
            if client.get_chat_member(m.chat.id, m.reply_to_message.from_user.id).status != 'creator' or 'administrator':
                client.promote_chat_member(m.chat.id, m.reply_to_message.from_user.id,
                                           can_change_info=1,
                                           can_delete_messages=1,
                                           can_invite_users=1,
                                           can_pin_messages=1,
                                           can_promote_members=False,
                                           can_restrict_members=1)
                if m.reply_to_message.from_user.username:
                    m.edit('@{} is promoted'.format(m.reply_to_message.from_user.username), parse_mode='Markdown')
                    if len(m.text.split())>2 and client.get_chat_member(m.chat.id, client.get_me().id).status == 'creator':
                        client.set_administrator_title(m.chat.id, m.reply_to_message.from_user.id,
                                                       " ".join(m.text.split()[2:][:16]))
                else:
                    m.edit('[{}](tg://user?id={}) is promoted'.format(
                        m.reply_to_message.from_user.first_name, m.reply_to_message.from_user.id
                    ), parse_mode='Markdown', disable_web_page_preview=0)
                    if len(m.text.split())>2:
                        client.set_administrator_title(m.chat.id, m.reply_to_message.from_user.id,
                                                       " ".join(m.text.split()[2:][:16]))
            return
        if m.entities[0].type == 'mention':
            if client.get_chat_member(m.chat.id, username(m.text)).status != 'creator' or 'administrator':
                client.promote_chat_member(m.chat.id, username(m.text),
                                           can_change_info=1,
                                           can_delete_messages=1,
                                           can_invite_users=1,
                                           can_pin_messages=1,
                                           can_promote_members=False,
                                           can_restrict_members=1)
                m.edit('@{} is promoted'.format(username(m.text)), parse_mode='Markdown')
                if len(m.text.split())>2 and client.get_chat_member(m.chat.id, client.get_me().id).status == 'creator':
                    client.set_administrator_title(m.chat.id, username(m.text),
                                                   " ".join(m.text.split()[2:][:16]))
            return
        if m.entities[0].type == 'text_mention':
            if client.get_chat_member(m.chat.id, m.entities[0].from_user.id).status != 'creator' or 'administrator':
                client.promote_chat_member(m.chat.id, username(m.text),
                                           can_change_info=1,
                                           can_delete_messages=1,
                                           can_invite_users=1,
                                           can_pin_messages=1,
                                           can_promote_members=False,
                                           can_restrict_members=1)
                m.edit('[{}](tg://user?id={}) is promoted'.format(
                    m.entities[0].from_user.first_name, m.entities[0].from_user.id
                ), parse_mode='Markdown', disable_web_page_preview=0)
                if len(m.text.split())>2 and client.get_chat_member(m.chat.id, client.get_me().id).status == 'creator':
                    client.set_administrator_title(m.chat.id, m.entities[0].from_user.id,
                                                   " ".join(m.text.split()[2:][:16]))
            return


@Client.on_message(Filters.me & Filters.group & Filters.command(['demote'], ['.', '/']))
def demote_user(client, m):
    if client.get_chat_member(m.chat.id, client.get_me().id).status == 'creator' or 'administrator':
        if m.reply_to_message:
            if client.get_chat_member(m.chat.id, m.reply_to_message.from_user.id).status == 'creator' or 'administrator':
                client.promote_chat_member(m.chat.id, m.reply_to_message.from_user.id,
                                           can_change_info=0,
                                           can_delete_messages=0,
                                           can_invite_users=0,
                                           can_post_messages=0,
                                           can_promote_members=0,
                                           can_restrict_members=0)
                if m.reply_to_message.from_user.username:
                    m.edit('@{} is demoted'.format(m.reply_to_message.from_user.username), parse_mode='Markdown')
                else:
                    m.edit('[{}](tg://user?id={}) is demoted'.format(
                        m.reply_to_message.from_user.first_name, m.reply_to_message.from_user.id
                    ), parse_mode='Markdown', disable_web_page_preview=0)
            return
        if m.entities[0].type == 'mention':
            if client.get_chat_member(m.chat.id, username(m.text)).status == 'creator' or 'administrator':
                client.promote_chat_member(m.chat.id, username(m.text),
                                           can_change_info=0,
                                           can_delete_messages=0,
                                           can_invite_users=0,
                                           can_promote_members=0,
                                           can_restrict_members=0)
                m.edit('@{} is demoted'.format(username(m.text)), parse_mode='Markdown')
            return
        if m.entities[0].type == 'text_mention':
            if client.get_chat_member(m.chat.id, m.entities[0].from_user.id).status == 'creator' or 'administrator':
                client.promote_chat_member(m.chat.id, username(m.text),
                                           can_change_info=0,
                                           can_delete_messages=0,
                                           can_invite_users=0,
                                           can_pin_messages=0,
                                           can_promote_members=0,
                                           can_restrict_members=0)
                m.edit('[{}](tg://user?id={}) is demoted'.format(
                    m.entities[0].from_user.first_name, m.entities[0].from_user.id
                ), parse_mode='Markdown', disable_web_page_preview=0)
            return
