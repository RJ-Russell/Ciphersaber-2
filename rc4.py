# Copyright (C) 2015 RJ Russell
# Created with in collaboration:
# Rachel Johnson:
# Andrew Wood:
#
# RC4.py

from os import urandom

# Key scheduling
def key_scheduling(key, rounds=20):

	state = list(range(256))
	key_list = list(range(256))
	
	len_state = len(state)
	len_key = len(key)
	
	j = 0
	for num_round in range(rounds):
		for i in range(len_state):
			j = (j + state[i] + ord(key[i % len_key:(i % len_key)+1])) % 256
			key_scheduler = swap(state,i,j)
	
	return key_scheduler


# Generate Stream
def rc4(message, key):
	
	len_key = len(key)
	
	len_message = len(message)

	key_list = list(range(256))
	len_key_list = len(key_list)
	key_list = key_scheduling(key)
	
	alt_message = b""
	i = 0
	j = 0
	for byte in range(len_message):
		i = (i + 1) % 256
		j = (j + key_list[i]) % 256 
		key_list = swap(key_list, i, j)
		xor_bytes = key_list[(key_list[i] + key_list[j]) % len_key_list]
		cipher_byte = ord(message[byte:byte+1]) ^ key_list[byte]
		cipher_byte = bytes([cipher_byte])
		alt_message += cipher_byte 
	
	return alt_message


def swap(state, i, j):
	"""
		Takes in list and two integers, swaps state[i] with state[j]
		and returns the list.
	"""
	temp = state[i]
	state[i] = state[j]
	state[j] = temp

	return state



def encrypt(message, key):
	
	key = str.encode(key)
	iv = urandom(10)
	key += iv
	
	cipher_txt = iv + rc4(message,key) 
	return cipher_txt



def decrypt(message, key):
	
	key = str.encode(key)
	iv = message[0:10]
	key += iv
	
	message = message[10:]
	
	plain_txt = rc4(message,key)
	
	return plain_txt



if __name__ == "__main__":
	
	message = "FUcking fuck fuck fuck this is a stupid fucking program and I hate it very very very very much."
	key = "password"

	m = encrypt(message, key)
	print("'\n'CM: ", m)

	d = decrypt(m, key)
	print("'\n'DM: ", d)

	d = d.decode("ASCII")
	print("'\n'D: ", d)
	
	#print("--- %s seconds ---" % (time.time() - start_time))
	#d = decrypt(enc,key)
	
	
	#iv = urandom(10)
	#key = str.encode('key')
	#key += iv
	#print("KEY + IV: ", key)

	#m = rc4(message, key)
	#print("M: ", m)
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

