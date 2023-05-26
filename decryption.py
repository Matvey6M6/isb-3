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