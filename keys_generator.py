from assymetric import assymetric
from symmetric import symmetric


def keys_generator(private_key, public_key, symmetric_key, symmetric_key_decrypted, size):

    assym = assymetric(
        public_key, private_key, symmetric_key_decrypted, symmetric_key)

    assym.generate_pair()

    symm = symmetric(size, symmetric_key_decrypted)
    symm.gernerate()

    assym.encrypt()