from assymetric import Assymetric
from symmetric import Symmetric


def decrypt(encrypted_file: str, private_key: str,
            symmetric_key: str, decrypted_file, symmetric_key_decrypted: str, size: int) -> None:
    """Запускает режим расшифровки

    Args:
        encrypted_file (str): файл с зашифрованным текстом 
        private_key (str): файл с приватным ключом 
        symmetric_key (str): _description_
        decrypted_file (_type_): файл с расшифрованным текстом
        symmetric_key_decrypted (str): файл с симметричным расшифрованным ключем 
        size (int): размер ключа
    """
    assym_SYM = Assymetric(
        private_k_file=private_key, decrypted_file=symmetric_key_decrypted, ciphed_file=symmetric_key)

    assym_SYM.decrypt()

    sym = Symmetric(size, symmetric_key_decrypted,
                    encrypted_file, decrypted_file)
    sym.decrypt()


def encrypt(decrypted_file: str, private_key: str, symmetric_key:
            str, encrypted_file: str, symmetric_key_decrypted: str, size: int) -> None:
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


def keys_generator(private_key: str, public_key: str, symmetric_key: str, symmetric_key_decrypted: str, size: int) -> None:
    """Функцияя запускает режим генерации ключей

    Args:
        private_key (str): путь до приватного ключа 
        public_key (str): путь до публичного ключа
        symmetric_key (str): путь до симметричного ключа 
        symmetric_key_decrypted (str): путь до симметричного рас ключа 
        size (int): размер ключа
    """
    assym = Assymetric(
        public_key, private_key, symmetric_key_decrypted, symmetric_key)

    assym.generate_pair()

    symm = Symmetric(size, symmetric_key_decrypted)
    symm.gernerate()

    assym.encrypt()
