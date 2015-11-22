# RJ Russell CS300 
# RC4.py
# code excerpts taken from www.github.com/keiyakins
# the "Kitty of Men" helped with all of my code skillz

from os import urandom
from random import randint
import sys


def swap(state, i, j):
	temp = state[i]
	state[i] = state[j]
	state[j] = temp

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
	for num_times in range(rounds):
		for i in range(len(state)):
				j = (state[i] + key[i % length_key]) % 256   
				stream = swap(state,i,j)

	return state
# Swap the ith and jth elements of the state array. 

# Generate Stream
def generate_stream(message, key):
#After the entire mixing loop is completed, i and j are set to zero.
#	key += iv
	i = 0
	j = 0
	byte_message = b""
	length_message = len(message)
	for i in range(length_message):
		j = (j + state[i%256]) % 256 
		state = swap(state,i,j)
		n = state[i] + j
		message_byte = message[i] ^ n
		print(message_byte)
		byte_message += message_byte
	return message


def encrypt(message, key):
	iv = urandom(10)
	key += iv

	key_stream = gen_stream(message,key)
	cipher_message = iv + key_stream
	
	return cipher_message



def decrypt(message, key):
#	message_length = len(message)
	iv = message[0:10]
	key += iv
	message = message[10:]
	deciphered_message = gen_stream(message,key)
	
	return deciphered_message



if __name__ == "__main__":
	message = "this is a message"
	key = str.encode("password")
	message = str.encode(message)
	iv = urandom(10)
	key += iv
	c = key_scheduling(key)
	d = key_scheduling(key)
	e = key_scheduling(key)
	f = key_scheduling(key)
	print("C: ", c, '\n')
	print("D: ", d, '\n')
	print("E: ", e, '\n')
	print("F: ", f, '\n')

