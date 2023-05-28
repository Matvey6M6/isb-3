import json 
import os
from encryption import encrypt
from decryption import decrypt
SETTINGS = os.path.join("setting.json")
with open(SETTINGS) as json_file:
    settings = json.load(json_file)
decrypt(settings['encrypted_file'], settings['private_key'],
                         settings['symmetric_key'], settings['decrypted_file'], settings["symmetric_key_decrypted"], 128)