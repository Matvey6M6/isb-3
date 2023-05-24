import os
import logging

from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

logging.basicConfig(level=logging.INFO)
class Symmetric:
    def __init__(self, size, sym_key_file, encrypt_file, decrypt_file):

        self.size = size
        self.sym_key_file = sym_key_file
        self.decrypt_file = decrypt_file
        self.encrypt_file = encrypt_file

    def _padd_(self, data):
        padder = padding.ANSIX923(algorithms.Camellia.block_size).padder()
        text = bytes(data, 'UTF-8')
        padded_text = padder.update(text)+padder.finalize()

        return padded_text

    def de_padd(self, plaintext):
        last_byte = plaintext[-1]
        if isinstance(last_byte, int):
            return last_byte
        else:
            return ord(last_byte)

    def decrypt(self):
        c_text = bytes()
        try:
            with open(self.encrypt_file, 'rb') as file:
                c_text = file.read()
            logging.info(f"Файл {self.encrypt_file} проситан")
        except:
            logging.error(f"Файл {self.encrypt_file} ошибка чтения")
            exit()

        iv = c_text[:8]
        c_text = c_text[8:]

        cipher = Cipher(algorithms.Camellia(self.open_symkey()),
                        modes.CBC(iv), backend=default_backend())

        decryptor = cipher.decryptor()
        plaintext = decryptor.update(c_text) + decryptor.finalize()

        padding_size = self.de_padd(plaintext)

        plaintext = plaintext[:-padding_size]

        self.decode_to_file(plaintext)

        return plaintext

    def decode_to_file(self, text):
        try:
            with open(self.decrypt_file, "wb") as file:
                file.write(text)
            logging.info(f"Файл {self.decrypt_file}: запись прошла идеально")
        except:
            logging.error(f"Файл {self.decrypt_file}: ошибка при записи")

    def write_encrytext(self, c_text: bytes):
        try:
            with open(self.encrypt_file, "wb") as file:
                file.write(c_text)
            logging.info(f"Файл {self.encrypt_file}: запись прошла идеально")
        except:
            logging.error(f"Файл {self.encrypt_file}: ошибка при записи ")

    def encrytp(self):

        data = str()

        with open(self.decrypt_file, 'r') as file:
            data = file.read()

        iv = os.urandom(8)

        key = self.open_symkey()

        cipher = Cipher(algorithms.Blowfish(
            key), modes.CBC(iv), backend=default_backend())

        data = self._padd_(data)

        encryptor = cipher.encryptor()
        c_text = iv + encryptor.update(data) + encryptor.finalize()

        self.write_encrytext(c_text)

    def open_symkey(self):
        try:
            with open(self.sym_key_file, mode='rb') as key_file:
                content = key_file.read()
            logging.info(f"Файл {self.sym_key_file}: прочитан ")
            return content
        except:
            logging.error(f"Фейл {self.sym_key_file}: ошибка при чтении")

    def write_sym(self, c_key):

        try:
            with open(self.sym_key_file, 'wb') as key_file:
                key_file.write(c_key)
            logging.info(f"Файл {self.sym_key_file}: записан")
        except:
            logging.error(f"Фейл {self.sym_key_file}: ошибка при записи")

    def gernerate(self):


        key = os.urandom(self.size)
        self.write_sym(key)