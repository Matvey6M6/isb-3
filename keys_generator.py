from assymetric import Assymetric
from symmetric import Symmetric


def keys_generator(private_key, public_key, symmetric_key, symmetric_key_decrypted, size):

    assym = Assymetric(
        public_key, private_key, symmetric_key_decrypted, symmetric_key)

    assym.generate_pair()

    symm = Symmetric(size, symmetric_key_decrypted)
    symm.gernerate()

    assym.encrypt()