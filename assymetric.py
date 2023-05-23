import logging

from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.serialization import load_pem_public_key, load_pem_private_key


class assymetric:

    def __init__(self, public_k_file, private_k_file, decrypted_file, ciphed_file):
        self.public_pem = public_k_file
        self.private_pem = private_k_file
        self.ciphed_file = ciphed_file
        self.decrypted_file = decrypted_file

    def public_key_to_file(self, key):
        try:
            with open(self.public_pem, 'wb') as file_out:
                file_out.write(key.public_bytes(encoding=serialization.Encoding.PEM,
                                                format=serialization.PublicFormat.SubjectPublicKeyInfo))
            logging.info(f"Файл {self.public_pem}: успешно записан")
        except:
            logging.error(f"Файл {self.public_pem}: ошибка открытия")

    def private_key_to_file(self, key):

        try:
            with open(self.private_pem, 'wb') as file_out:
                file_out.write(key.private_bytes(encoding=serialization.Encoding.PEM,
                                                 format=serialization.PrivateFormat.TraditionalOpenSSL,
                                                 encryption_algorithm=serialization.NoEncryption()))
            logging.info(f"Файл {self.public_pem}  записан")
        except:
            logging.error(f"файл {self.public_pem}: ошибка при открытии")

    def generate_pair(self):

        keys = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048
        )
        private_key = keys
        public_key = keys.public_key()

        self.public_key_to_file(public_key)
        self.private_key_to_file(private_key)

    def read_public_key(self):
        try:
            with open(self.public_pem, 'rb') as pem_in:
                public_bytes = pem_in.read()
            d_public_key = load_pem_public_key(public_bytes)
            logging.info(f"Файл {self.public_pem} прочитан")
            return d_public_key
        except:
            logging.error(f"Файл {self.public_pem}: ошибка при открытии")

    def read_private_key(self) :

        try:
            with open(self.private_pem, 'rb') as pem_in:
                private_bytes = pem_in.read()
            private_key = load_pem_private_key(private_bytes, password=None,)
            logging(f"Файл {self.private_pem} успешно прочитан")
            return private_key
        except:
            logging.error(f"Файл {self.public_pem}: ошибка при чтении")

    def ciphed_text_to_file(self, c_text: bytes):

        try:
            with open(self.ciphed_file, 'wb') as file:
                file.write(c_text)
            logging.info(f"Файл {self.ciphed_file} записан")
        except:
            logging.error(f"Файл {self.ciphed_file}: ошибка при записи")

    def decrypted_text_to_file(self, data: str):

        try:
            with open(self.decrypted_file, 'wb') as file:
                file.write(data)
            logging.info(f"{self.ciphed_file} ")
        except:
            logging.error(f"Файл {self.ciphed_file}: ошибка при записи ")

    def read_ciphed_text(self) :

        try:
            with open(self.ciphed_file, 'rb') as file:
                c_text = file.read()
            logging.info(f"Файл {self.ciphed_file} прочитан")    
            return c_text
        except:
            logging.error(f"Файл {self.ciphed_file} : ошибка при открытии")

    def encrypt(self):

        data = str()
        with open(self.decrypted_file, 'rb') as file:
            data = file.read()

        if type(data) != bytes:
            text = bytes(data, "UTF-8")
        else:
            text = data

        public_key = self.read_public_key()
        c_text = public_key.encrypt(text, padding.OAEP(mgf=padding.MGF1(
            algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None))
        self.ciphed_text_to_file(c_text)

    def decrypt(self):
        private_key = self.read_private_key(self.private_pem)
        c_text = self.read_ciphed_text()
        dc_text = private_key.decrypt(c_text, padding.OAEP(mgf=padding.MGF1(
            algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None))

        self.decrypted_text_to_file(dc_text)