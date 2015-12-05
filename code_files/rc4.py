# Copyright (C) 2015 RJ Russell
# Created with in collaboration:
# Jacob Martin:
# Rachael Johnson:
# Andrew Wood:
#
# CipherSaber2 algorithm provided by Bart Massey
# https://github.com/BartMassey/ciphersaber2/blob/master/README.md
"""
rc4.py

This file is responsible for encrypting/decrypting a message using the CipherSaber2 algorithm.
Takes in either an encrypted or plain text message. Combines the key with the IV to be used
in the CipherSaber2 algorithm. Generates a key scheduling, key stream, and xor's each byte of the
message with the key stream. Returns the result.
"""


import random
import string
import time
import datetime


def rc4(message, key, rounds=20):
    """
    :param input: A string of converted integers (this happens in the encrypt/decrypt methods)
    :param key: key+iv sent in, also converted to integers
    :param rounds: Default 20, may pass in other values if needed.
    :return: newly generated list of xor'd bytes.
    """
    state = range(256)

    len_state = len(state)
    len_key = len(key)

    j = 0
    for num_round in range(rounds):
        for i in range(len_state):
            j = (j + state[i] + key[i % len_key]) % 256
            state[i], state[j] = state[j], state[i]

    alt_message = []
    i = 0
    j = 0
    for byte in message:
        i = (i + 1) % 256
        j = (j + state[i]) % 256
        state[i], state[j] = state[j], state[i]
        xor_bytes = (state[i] + state[j]) % 256
        alt_message.append(byte ^ state[xor_bytes])

    return alt_message


def get_time():
    """
    :return: timestamp containing the formatted timestamp string
    """
    timestamp = time.time()
    timestamp = datetime.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d @ %H%M')
    return timestamp


def encrypt(plain_message, key, iv=""):
    """
    :param plain_message: Message sent in from the client
    :param key: value used  for all encryption/decryption
    :param iv: stores first ten 'bytes' of the plain message
    :return: joined list in string format of the encrypted message
    """
    # addes time stamp to message
    plain_message += "\n" + "Sent on: " + get_time() + "\n"
    print "ENCRYPTING..."
    iv_rand = random.SystemRandom()
    # Creates the IV
    while len(iv) < 10:
        iv += chr(int(iv_rand.random()))
    # maps each character to an integer value and sends to be xor'd.
    encrypted_message = rc4(map(ord, plain_message), map(ord, key + iv))

    # joins the list in string format and converts each int to a string representation
    return iv + string.join(map(chr, encrypted_message), "")


def decrypt(cipher_mess, key):
    """
    :param cipher_mess: encrypted message sent in from the server
    :param key: value used for encryption/decryption
    :return: joined list in string format of the plain text message
    """
    print "DECRYPTING..."
    # Takes the IV from the messages
    iv = cipher_mess[0:10]
    # Stores the message portion of the encrypted message
    cipher_mess = cipher_mess[10:]
    # maps each byte to an integer value and sends to be xor'd
    plain_text = rc4(map(ord, cipher_mess), map(ord, key + iv))
    # jonis the list in string format and converts each int to a string representation
    return string.join(map(chr, plain_text), "") + "\nReceived on: " + get_time()


