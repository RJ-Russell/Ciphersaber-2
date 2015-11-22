# RJ Russell CS300 
# RC4.py
# code excerpts taken from www.github.com/keiyakins
# the "Kitty of Men" helped with all of my code skillz
from base64 import b64encode
import os
from random import randint
import sys


def swap(state, i, j):
	temp = state[i]
	state[i] = state[j]
	state[j] = temp

	return state


# RC4 uses two arrays of eight bit bytes. The "state" array is 256 bytes long and holds a
# permutation of the numbers 0 through 255. The "key" array can be of any length up to 256 bytes.
# RC4 also uses two index variables i and j that start off as zero. All variables are eight bits
# long and all addition is performed modulo 256.

# The state array is then subjected to 256 mixing operations using a loop that steps i through the
# values from zero to 255. Each mixing operation consists of two steps:

# Key scheduling
def key_scheduling(key, rounds=200):
# Add to the variable j the contents of the ith element of the state array and the nth element of
# the key, where n is equal to i modulo the length of the key.
	state = list(range(256))
	length_key = len(key)
	j = 0
	for num_times in range(rounds):
		for i in range(256):
			j = (j + state[i] + ord(key[i % length_key])) % 256   
		# Swap the ith and jth elements of the state array. 
			key_scheduler = swap(state,i,j)
	print("KEYSCHED: ", key_scheduler)
	return key_scheduler

# Generate Stream
def generate_stream(state, key):
	
	length_key = len(key)
	key_stream = list(range(length_key))
	print("KEY STREAM (BEFORE): ", key_stream)
	j = 0
	for i in range(length_key-1):
		i = (i + 1) % 256
		j = (j + state[i]) % 256 
		state[i], state[j] = state[j], state[i]
		key_stream[i] =  state[(state[i] + state[j]) % 256]
	print("KEYSTREAM (AFTER): ", key_stream)
	return key_stream


def encrypt(message, key):
	iv = os.urandom(10)
	print("IV: ", iv)
	key += b64encode(iv).decode("ASCII")
	print("KEY + IV: ", key)

	key_scheduler = key_scheduling(key)
	key_stream = generate_stream(key_scheduler,key)
	
	cipher = list(range(len(message) + 10))
	cipher_txt = b""
	for i in range(10):
		cipher[i] += iv[i]
	for j in range(len(message)):
		cipher[i] += ord(message[i]) ^ key_stream[i]
	
	for index in cipher:
		cipher_txt += chr(index).encode()
	
	return cipher_txt



def decrypt(message, key):
	message_length = len(message)
	iv = message[0:10]
	print("IV LEN: ", len(iv))
	key += b64encode(iv).decode("ASCII")
	print("KEY + IV: ", key)
	
	message = message[10:]
	key_scheduler = key_scheduling(key)
	key_stream = generate_stream(key_scheduler,key)
	plain = list(range(message_length-10))
	print("PLAIN: ",plain)
	print("MESSAGE: ", message)
	print("KEY STREAM: ", key_stream)
	plain_txt = ""
	for i in range(len(message)):
		plain[i] = message[i] ^ key_stream[i]
	
	for index in plain:
		plain_txt += str(plain)

	return plain_txt



if __name__ == "__main__":
	message = "this is a message"
	key = "password"

	#d = decrypt(enc,key)
	#print("DECRYPTED MESSAGE: ", d)
	
	
	iv = os.urandom(10)
	key += b64encode(iv).decode("ASCII")
	print("KEY + IV: ", key)

	keys = key_scheduling(key)
	print("KEYS: ", keys)
	stream = generate_stream(keys,key)
	print("STREAM: ", stream)
	#c = key_scheduling(key)
	#print("C: ", c, '\n')
	#d = key_scheduling(key)
	#print("D: ", d, '\n')
	#e = key_scheduling(key)
	#print("E: ", e, '\n')
	#f = key_scheduling(key)
	#print("F: ", f, '\n')

	#z = generate_stream(c,message,key)
	#print("Z: ",z,'\n')

	#enc_mess = encrypt(message, key)
	#print("ENCRYPTED MESSAGE: ", enc_mess)

	#dec_message = decrypt(enc_mess, key)
	#print("DECRYPTED MESSAGE: ", dec_message)

