# RJ Russell CS300 
# RC4.py
# code excerpts taken from www.github.com/keiyakins

from os import urandom
from random import randint
import sys

message = "What the fuck am I doing"

def swap(state, i, j):
    temp = state[i]
    state[i] = state[j]
    state[j] = temp

def gen_cipher(message, key="password", rounds=20):
    print("cipher things go here")


def encrypt(message, key="password"):
    iv = urandom(10)
    key += iv
    key_stream = rc4(message,key)
    cipher_message = iv + key_stream
    
    return cipher_message



def decrypt(message, key="password"):
    message_length = len(message)
    iv = message[0:10]
    key += iv
    message = message[10:]
    deciphered_message = rc4(message,key)
    
    return deciphered_message




iv = list(range(255))

iv = bytes(iv)
print(sys.getsizeof(iv))
