# RJ Russell CS300 
# RC4.py
# code excerpts taken from www.github.com/keiyakins
# the "Kitty of Men" helped with all of my code skillz
from os import urandom
import sys


def swap(state, i, j):
	"""
		Takes in list and two integers, swaps state[i] with state[j]
		and returns the list.
	"""
	temp = state[i]
	state[i] = state[j]
	state[j] = temp

	return state


# Key scheduling
def key_scheduling(key, rounds=200):

	state = list(range(256))
	key_list = list(range(256))
	
	len_state = len(state)
	len_key = len(key)
	
	j = 0
	for num_round in range(rounds):
		for i in range(len(state)):
			t_byte = key[i % len_key:(i % len_key)+1]
			key_list[i] = ord(t_byte)
			j = (j + state[i] + key_list[i]) % 256
			key_scheduler = swap(state,i,j)
	return key_scheduler

# Generate Stream
def generate_stream(state, key):
	
	length_key = len(key)
	key_stream = list(range(length_key))
	alt_message = b""
	print("KEY STREAM (BEFORE): ", key_stream)
	i = 0
	j = 0
	for byte in range(length_key):
		i = (i + 1) % 256
		j = (j + state[i]) % 256 
		key_stream = swap(state, i, j)
		key_stream[byte] =  state[(state[i] + state[j]) % 256]
	print("KEYSTREAM (AFTER): ", key_stream)
	return key_stream

def encrypt(message, key):
	iv = urandom(10)
	print("IV: ", iv)
	key = str.encode(key)
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
	key = str.encode('key')
	key += iv
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
	
	
	iv = urandom(10)
	key = str.encode('key')
	key += iv
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

