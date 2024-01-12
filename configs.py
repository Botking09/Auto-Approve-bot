from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "27514811"))
    API_HASH = getenv("API_HASH", "88b650f1272ab3d38474b18d3bcc66a8")
    BOT_TOKEN = getenv("BOT_TOKEN", "1234567891:AdDfgFRFVVfDEhdhyjjvjjftSEW")
    FSUB = getenv("FSUB", "https://thanosXbotz")
    CHID = int(getenv("CHID", "-1001991743829"))
    SUDO = list(map(int, getenv("SUDO").split()))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://Ankitking:Ankitking@cluster0.oyrtdsm.mongodb.net/?retryWrites=true&w=majority")
    
cfg = Config()
