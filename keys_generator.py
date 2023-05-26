from assymetric import Assymetric
from symmetric import Symmetric


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