import os
import logging

from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

logging.basicConfig(level=logging.INFO)


class Symmetric:
    """Класс генерирует симметричные ключи шифрования использую алогритм Camellia"""

    def __init__(self, size: int, sym_key_file: str, encrypt_file: str = None, decrypt_file: str = None) -> None:
        """Функция инициализации"""
        self.size = size
        self.sym_key_file = sym_key_file
        self.decrypt_file = decrypt_file
        self.encrypt_file = encrypt_file

    def _padd_(self, data: str) -> bytes:
        """Делает длинну текста кратным размеру блока
        Args:
            data (str): текст 

        Returns:
            bytes: сформированный текст
        """

        padder = padding.ANSIX923(algorithms.Camellia.block_size).padder()
        text = bytes(data, 'UTF-8')
        padded_text = padder.update(text)+padder.finalize()
        return padded_text

    def de_padd(self, plaintext: str) -> bytes:
        """Делает текст нормальным после функции _padd

        Args:
            plaintext (_type_): padded text 
        """
        last_byte = plaintext[-1]
        if isinstance(last_byte, int):
            return last_byte
        else:
            return ord(last_byte)

    def decrypt(self) -> str:
        """Расшифровывает текст

        Returns:
            str: расшифрованный текст 
        """
        c_text = bytes()
        try:
            with open(self.encrypt_file, 'rb') as file:
                c_text = file.read()
            logging.info(f"Файл {self.encrypt_file} проситан")
        except:
            logging.error(f"Файл {self.encrypt_file} ошибка чтения")
            exit()

        iv = c_text[:16]
        c_text = c_text[16:]
        key = self.open_symkey()
        cipher = Cipher(algorithms.Camellia(key[:16]),
                        modes.CBC(iv), backend=default_backend())

        decryptor = cipher.decryptor()
        plaintext = decryptor.update(c_text) + decryptor.finalize()

        padding_size = self.de_padd(plaintext)

        plaintext = plaintext[:-padding_size]

        self.decode_to_file(plaintext)

        return plaintext

    def decode_to_file(self, text):
        """"""
        try:
            with open(self.decrypt_file, "wb") as file:
                file.write(text)
            logging.info(f"Файл {self.decrypt_file}: запись прошла идеально")
        except:
            logging.error(f"Файл {self.decrypt_file}: ошибка при записи")

    def write_encrytext(self, c_text: bytes):
        """Срелизациия зашифрованного текста

        Args:
            c_text (bytes): 
        """
        try:
            with open(self.encrypt_file, "wb") as file:
                file.write(c_text)
            logging.info(f"Файл {self.encrypt_file}: запись прошла идеально")
        except:
            logging.error(f"Файл {self.encrypt_file}: ошибка при записи ")

    def encrytp(self) -> None:
        """Шифрует заданные данные и записывает их в зашифрованный файл
        """
        try:
            with open(self.decrypt_file, 'r') as file:
                data = file.read()
        except:
            logging.error(f"Файл {self.decrypt_file} не прочитан")

        iv = os.urandom(16)

        key = self.open_symkey()

        cipher = Cipher(algorithms.Camellia(key[:16]), modes.CBC(iv))

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
        """Генерация ключей"""
        key = os.urandom(self.size//8)
        self.write_sym(key)
