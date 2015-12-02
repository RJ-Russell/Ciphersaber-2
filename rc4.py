# Copyright (C) 2015 RJ Russell
# Created with in collaboration:
# Jacob Martin:
# Rachael Johnson:
# Andrew Wood:
#
#
# rc4.py


import random
import string
import time
import datetime


# Key scheduling
def rc4(input, key, rounds=20):
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
    for byte in input:
        i = (i + 1) % 256
        j = (j + state[i]) % 256
        state[i], state[j] = state[j], state[i]
        xor_bytes = (state[i] + state[j]) % 256
        alt_message.append(byte ^ state[xor_bytes])

    return alt_message


def get_time():
    timestamp = time.time()
    timestamp = datetime.datetime.fromtimestamp(timestamp).strftime(%Y-%m-%d @ %H:%M:%S')
    return timestamp


def encrypt(plain_message, key, iv=""):
    print "ENCRYPTING..."
    plain_message += "\n" + "Sent on: " + get_time() + "\n"

    iv_rand = random.SystemRandom()
    while len(iv) < 10:
        iv += chr(int(iv_rand.random()))
    bytes = rc4(map(ord, plain_message), map(ord, key + iv))
    return iv + string.join(map(chr, bytes), "")


def decrypt(cipher_mess, key):
    print "DECRYPTING..."

    iv = cipher_mess[0:10]
    cipher_mess = cipher_mess[10:]
    bytes = rc4(map(ord, cipher_mess), map(ord, key + iv))
    return string.join(map(chr, bytes), "") + "Received on: " + get_time() + "\n"


if __name__ == "__main__":
    # key = "asdfg"
    # infile = open("testfiles/cstest.cs2", "r")
    # e = infile.read()
    # d = decrypt(e, key)
    # print "D: ", d, "\n"

    # key1 = "asdfg"
    # jfile = open("cstest1.cs1", "r")
    # f = jfile.read()
    # g = decrypt(f, key1)
    # print "D: ", g

    key2 = "SecretMessageforCongress"
    # ifile = open("testfiles/cstest2.cs1", "r")
    # i = ifile.read()
    # print "BEFORE DECRYPT: ", i

    # j = decrypt(i, key2)
    # print "AFTER DECRYPT: ", j

    # e = encrypt(message, key)
    # print "E: ", e

    f = open("testfiles/test.cs1", "w")
    message = raw_input("Enter your message: ")
    z = encrypt(message, key2)
    f.write(z)
    f.close()

    l = open("testfiles/test.cs1", "r")
    message = l.read()
    m = decrypt(message, key2)
    print "Message: ", m, "\n"
    l.close()


# filename = sys.argv[1]
# a_file = open(filename, "r")
# encrypted = a_file.readline().rstrip()
# decrypted = decrypt(encrypted,key)

# f = d.decode("ASCII")
# print("F: ", f)

# m = rc4(message, key)
# print("M: ", m)
# c = key_scheduling(key)
# print("C: ", c, '\n')
# d = key_scheduling(key)
# print("D: ", d, '\n')
# e = key_scheduling(key)
# print("E: ", e, '\n')
# f = key_scheduling(key)
# print("F: ", f, '\n')

# z = generate_stream(c,message,key)
# print("Z: ",z,'\n')

# enc_mess = encrypt(message, key)
# print("ENCRYPTED MESSAGE: ", enc_mess)

# dec_message = decrypt(enc_mess, key)
# print("DECRYPTED MESSAGE: ", dec_message)
