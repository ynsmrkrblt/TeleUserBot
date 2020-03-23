from pyrogram import Client

api_id = 0
api_hash = ""
mongo_connect = "MONGO_CONNECT"

client = Client("session", api_id, api_hash)
client.start()
client.stop()
