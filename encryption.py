from assymetric import Assymetric
from symmetric import Symmetric
import logging

def encrypt(decrypted_file: str, private_key: str, symmetric_key:
             str, encrypted_file: str, symmetric_key_decrypted:str, size: int) -> None:
    """Функциия запускает режим шифровки данных

    Args:
        decrypted_file (str): текст
        private_key (str): приватный ключ
        symmetric_key (str): симметричный ключ
        encrypted_file (str): путь куда сохранить зашифрованный текст
        symmetric_key_decrypted (str): файл с симметричным расшифрованным ключем
        size (int): размер ключа
    """

    assym_SYM = Assymetric(
        private_k_file=private_key, decrypted_file=symmetric_key_decrypted, ciphed_file=symmetric_key)
    assym_SYM.decrypt()
    sym = Symmetric(size, symmetric_key_decrypted,
                           encrypted_file, decrypted_file)
    sym.encrytp()