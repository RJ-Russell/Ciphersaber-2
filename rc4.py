# RJ Russell CS300 
# RC4.py
from os import urandom
from random import randint
import sys

key = "asdfqwer09"
message = "What the fuck am I doing"

iv = list(range(222))

iv = bytes(iv)
print(sys.getsizeof(iv))


