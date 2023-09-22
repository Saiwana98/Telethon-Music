import os

class Config(object):
    API_ID = int(os.environ.get("API_ID", "6213538"))
    API_HASH = os.environ.get("API_HASH", "8ce3522bd21cc937eee4c68813d501d5")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", 6557573098:AAGn4IRHwKOF0VN18Hmoxy0T34gIR60J_d4)
    STRING_SESSION = os.environ.get("STRING_SESSION", BQA_cw7OUD4pYLDGSjIZa85QDFVYMEHjW3b3T5bkBaWELQsTt8ojxkdKNQj49YQYnUuMUrv0thtTVrBXWGbXOe_uNT7HjlNSm9d9iEgwC10JZ35CK1TG_1ZTO9ESDZ2OvAYh3-2xD01ft3sQ1s12gtVuTiutY5EQ3UCwuBiNap4UrHmXmRNJH0X2cpW4NCQPIfs_o3Rx0BtP4TZ2-bfJD_Yq50fZICN67b0G1LIHpKgfFB2a6SMZal4SqyBGGOZco43jjJOLQ1wTA2j8EQ0GsIGErj6YAfdk2LTjpSpnsCsLPtf5jgP46fRi7W_F9tPWD5HpRg6KBMnMHCNoJ0jxGsCvblvftwA)
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "")
    SUPPORT = os.environ.get("SUPPORT", "TheSupportChat") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "TheUpdatesChannel") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
