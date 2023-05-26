from assymetric import Assymetric
from symmetric import Symmetric
import logging

def encrypt(decrypted_file, private_key, symmetric_key, encrypted_file, symmetric_key_decrypted, size):

    assym_SYM = Assymetric(
        private_k_file=private_key, decrypted_file=symmetric_key_decrypted, ciphed_file=symmetric_key)

    assym_SYM.decrypt()
    try:
        sym = Symmetric(size, symmetric_key_decrypted,
                           encrypted_file, decrypted_file)
        sym.encrytp()
    except:
        logging.error("Ошибка при создании ecryp")