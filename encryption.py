from assymetric import assymetric
from symmetric import symmetric


def encrypt(decrypted_file, private_key, symmetric_key, encrypted_file, symmetric_key_decrypted, size) :


    assym_SYM = assymetric(
        private_k_file=private_key, decrypted_file=symmetric_key_decrypted, ciphed_file=symmetric_key)

    assym_SYM.decrypt()

    sym = symmetric(size, symmetric_key_decrypted,
                           encrypted_file, decrypted_file)
    sym.encrytp()