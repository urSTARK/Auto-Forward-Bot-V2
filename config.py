from os import environ 

class Config:
    API_ID = environ.get("API_ID", "577678")
    API_HASH = environ.get("API_HASH", "d2c6e01uuiuiouioiuiou0fc6d7a1be")
    BOT_TOKEN = environ.get("BOT_TOKEN", "7558935139:AAFZC7c1J_8IQ1mcR0VKyWAAH60LumA4KAM") 
    BOT_SESSION = environ.get("BOT_SESSION", "bot") 
    DATABASE_URI = environ.get("DATABASE", "mongodb+srv://sr7blackbirds:5mRE2CGlkCXmI5pL@cluster0.jsssmx8.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    DATABASE_NAME = environ.get("DATABASE_NAME", "fdxhsdtawesfbot")
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '8479858938').split()]

class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    
