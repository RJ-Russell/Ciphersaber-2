# Copyright (C) 2015 RJ Russell
# Created with in collaboration:
# Jacob Martin:
# Rachel Johnson:
# Andrew Wood:
#
#
# RC4.py

import random, sys, string


# Key scheduling
def rc4(input, key, rounds=10):
	state = range(256)
	#key_list = list(range(256))
	
	len_state = len(state)
	len_key = len(key)
	
	j = 0
	for num_round in range(rounds):
		for i in range(len_state):
			j = (j + state[i] + key[i % len_key]) % 256
			state[i],state[j] = state[j], state[i]
	
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


def encrypt(plain_message, key, iv=""):
	
	while len(iv) < 10:
		iv = iv + chr(random.randint(0,255))
	bytes = rc4(map(ord, plain_message), map(ord, key+iv))
	return iv + string.join(map(chr, bytes), "")
	

def decrypt(cipher_mess, key):
	
	iv = cipher_mess[0:10]
	cipher_mess = cipher_mess[10:]
	bytes = rc4(map(ord, cipher_mess), map(ord, key+iv))
	return string.join(map(chr, bytes), "")
	

if __name__ == "__main__":
	
	#message = "FUcking fuck fuck fuck this is a stupid fucking program and I hate it very very very very much."
	key = "asdfg"
	
	infile = open("cstest.cs2", "r")
	e = infile.read()
	
	d = decrypt(e, key)
	print("D: ", d)
	




	
	#filename = sys.argv[1]
	#a_file = open(filename, "r")
	#encrypted = a_file.readline().rstrip()
	#decrypted = decrypt(encrypted,key)
	
	


	#f = d.decode("ASCII")
	#print("F: ", f)


		
	
	#m = encrypt(message, key)
	#print("'\n'CM: ", m)

	#d = d.decode("ASCII")
	#print("'\n'D: ", d)
	
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

