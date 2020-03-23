from pyrogram import Filters, Client
from time import time, sleep
from google_search_client.search_client import GoogleSearchClient
import ast


@Client.on_message(Filters.me & Filters.command(['google'], ['.', '/']))
def google_search(client, message):
    sleep(0.2)
    text = message.text
    if len(text.split()) == 1:
        message.edit("You must input word for search")
        return
    message.edit("Searching...")
    start = time()
    query = " ".join(text.split()[1:])
    msg = "Searched word : {}\n\n".format(query)
    res = GoogleSearchClient()
    results = res.search(query).to_json()
    if results:
        i = 1
        for result in ast.literal_eval(results):
            msg += f"🔍 [{result['title']}]({result['url']})\n\n"
            i += 1
            if i == 6:
                break
        end = time()
        elapsed = end - start
        msg += f"Elapsed time : {str(elapsed)[:4]}"
        try:
            message.edit(msg, disable_web_page_preview=True, parse_mode="Markdown")
        except Exception as e:
            print(e)
