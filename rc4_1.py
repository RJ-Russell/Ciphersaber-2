from sys import argv
from os import urandom
from random import randint
from warnings import warn

class CryptoWarning(Warning):
    
    """Warning raised for cryptography issues.
       For instance, raised if the internal PRNG is used.
    """

    def __init__(self, msg):
        self.msg = msg

    
def sbytes(stream):
    """Generator to iterate over bytes in a stream."""
    byte = stream.read(1)
    while len(byte) > 0:
        yield ord(byte)
        byte = stream.read(1)

def swap(l, a, b):
    """Swap entries a and b in list l."""
    temp = l[a]
    l[a] = l[b]
    l[b] = temp

def ciphersaber(instream, outstream, key, reps, iv=None):
    """An implementation of CipherSaber-2.
    This implements a simple encryption method known as CipherSaber-2:
    * The encryption algorithm is RC4.
    * Repeat the key setup N times (usually N=20. For CipherSaber-1, N=1)
    * Encrypted files consist of a ten byte IV followed by the ciphertext.
    * A new, random IV is used for each message.
    * The cipher key is the user key as an ASCII string followed by the IV.
    It attempts to use the system's urandom, but will fall back to the random
    module if needed. If it does so, it will raise a CryptoWarning.
    
    Arguments:
    instream: The input stream. This is either the plain data to be enciphered
              or the ciphered data (without IV!) to be deciphered. It's OK if
              the IV is at the start of the stream, as long as it's before the
              current location.
    outstream: The output stream. Where the en/deciphered data goes. If a
               random IV was generated, it will be output as the first ten
               bytes, otherwise the IV will not be output.
    key: The user key.
    iv: Optional. If omitted, a random IV will be used to encipher the input.
        If included, will be used to decipher the input.
    """
    
    if iv == None:
        try:
            iv = urandom(10)
        except NotImplementedError:
            iv = []
            for i in range(10):
                iv.append(randint(0, 255))
            warn("CipherSaber using Python PRNG", CryptoWarning)
            iv = bytes(iv)
        outstream.write(iv)
        
    state = list(range(256))
    key += iv
    i = 0
    j = 0

    for k in range(reps):
        for i in range(256):
            j = (j + state[i] + key[i % len(key)]) % 256
            swap(state, i, j)
    
    i = 0
    j = 0
    
    for byte in sbytes(instream):
        i = (i + 1) % 256
        j = (j + state[i]) % 256
        swap(state, i, j)
        n = (state[i] + state[j]) % 256
        outstream.write(bytes([byte ^ state[n]]))

if __name__ == '__main__':
    if len(argv) >= 6 and argv[1] == 'e':
        try:
            infile = open(argv[2], 'rb')
            outfile = open(argv[3], 'wb')
            ciphersaber(infile, outfile, argv[4].encode('ascii'), int(argv[5]))
        finally:
            infile.close()
            outfile.close()
    elif len(argv) >= 6 and argv[1] == 'd':
        try:
            infile = open(argv[2], 'rb')
            outfile = open(argv[3], 'wb')
            ciphersaber(infile, outfile, argv[4].encode('ascii'),
                        int(argv[5]), infile.read(10))
        finally:
            infile.close()
            outfile.close()
    else:
        print("Usage:")
        print("Encrypt: ciphersaber.py e <input> <output> <key> <N>")
        print("Decrypt: ciphersaber.py d <input> <output> <key> <N>")
        print("To handle CipherSaber-1 messages, use N=1")
